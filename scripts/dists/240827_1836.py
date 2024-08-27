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
  m = copy.copy(a)
  for i, value in enumerate(b):
    if isinstance(value, dict):
      m[i] = merge_dict(a[i], b[i])
    elif isinstance(value, list):
      m[i] = merge_list(a[i], b[i])
    else:
      m.append(value)
  return m


'''
def merge_dict(a, b):
  m = copy.copy(a)
  for item in b:
    if isinstance(b[item], dict):
      m[item] = merge_dict(a[item], b[item])
    elif isinstance(b[item], list):
      m[item] = merge_list(a[item], b[item])
    else:
      m[item] = b[item]
  return m
'''


def merge_dict(a, b):
  #print(a)
  m = copy.copy(a if a else {})
  for item in b:
    if isinstance(b.get(item), dict):
      m[item] = merge_dict(a.get(item), b.get(item))
    elif isinstance(b.get(item), list):
      m[item] = merge_list(a.get(item), b.get(item))
    else:
      m[item] = b.get(item)
  return m


root_theme_path = Path(str(NSBundle.mainBundle().resourcePath()), 'Themes2')

user_theme_path = Path(str(PA2UITheme.sharedTheme().userThemesPath()))

paths_iter = itertools.chain(root_theme_path.iterdir(),
                             user_theme_path.iterdir())

tmp_dict = {}

for p in paths_iter:
  _theme_dict = get_json2dict(p)
  theme_dict = remove_comment_dict(_theme_dict)
  tmp_dict = merge_dict(theme_dict, tmp_dict)
  '''
  if not tmp_dict:
    tmp_dict = theme_dict
    continue
  tmp_dict = merge_dict(theme_dict, tmp_dict)
  '''
'''
pick = list(root_theme_path.iterdir())[0]
pick = list(user_theme_path.iterdir())[0]

d = get_json2dict(pick)
default_dict = get_deep_dict(d, {})
'''


json_data = json.dumps(tmp_dict, indent=2, sort_keys=True)
print(json_data)



