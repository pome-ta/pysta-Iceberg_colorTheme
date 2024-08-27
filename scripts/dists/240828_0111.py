from pathlib import Path
import re
import itertools
import copy
import json

from objc_util import ObjCClass
import pdbg

NSBundle = ObjCClass('NSBundle')
PA2UITheme = ObjCClass('PA2UITheme')

regex = re.compile(r'^.*?___comment$')


def get_json2dict(path: Path) -> dict:
  with open(path, mode='r', encoding='utf-8') as f:
    return json.load(f)


def remove_comment_dict(target: dict) -> dict:
  parent = {}
  for k, v in target.items():
    if regex.match(k):
      continue

    parent[k] = remove_comment_dict(v) if isinstance(v, dict) else v
  return parent


def merge_list(a, b):
  m = copy.copy(a if a else [])
  for i, value in enumerate(b):
    if isinstance(value, dict):
      m[i] = merge_dict(a[i], b[i])
    elif isinstance(value, list):
      m[i] = merge_list(a[i], b[i])
    else:
      m.append(value)
  return m


def merge_dict(a, b):
  m = copy.copy(a if a else {})
  for item in b:
    if isinstance(b.get(item), dict):
      m[item] = merge_dict(a.get(item), b.get(item))
    elif isinstance(b.get(item), list):
      m[item] = merge_list(a.get(item), b.get(item))
    else:
      m[item] = b.get(item)
  return m


def print_len(d: dict, name: str, deep: int = 0) -> None:
  indent = '  '
  print(f'{indent * deep}- {name}: {len(d)}')
  deep += 1
  for k, v in d.items():
    if not isinstance(v, dict):
      print(f'{indent * deep}- {k}:')
      continue
    print_len(v, k, deep)


def to_dumps(dict_data: dict) -> str:
  return json.dumps(dict_data, indent=1, sort_keys=True, ensure_ascii=False)


def write_dumps(data: str, name: str, dir: Path) -> None:
  json_path = Path(dir, f'{name}.json')
  if not json_path.exists():
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.touch()
  json_path.write_text(data, encoding='utf-8')


if __name__ == '__main__':
  dumps_path = Path('./dumps')

  root_theme_path = Path(str(NSBundle.mainBundle().resourcePath()), 'Themes2')

  user_theme_path = Path(str(PA2UITheme.sharedTheme().userThemesPath()))

  paths_iter = itertools.chain(root_theme_path.iterdir(),
                               user_theme_path.iterdir())

  tmp_dict = {}

  for p in paths_iter:
    if not p.suffix == '.json':
      continue
    _theme_dict = get_json2dict(p)
    theme_dict = remove_comment_dict(_theme_dict)

    _dump = to_dumps(theme_dict)
    '''
    write_dumps(_dump, p.stem, dumps_path)
    '''

    print_len(json.loads(_dump), p.stem)
    print('')

    tmp_dict = merge_dict(theme_dict, tmp_dict)

  _dump = to_dumps(tmp_dict)
  '''
  write_dumps(_dump, 'tmpMergeDumps', dumps_path)
  '''
  print_len(json.loads(_dump), 'tmpMergeDumps')

