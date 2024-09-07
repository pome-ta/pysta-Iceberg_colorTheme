'''
VSCode のtheme の要素出現調査

出現したすべての`key`
'''

from pathlib import Path
import json
from itertools import chain


def get_target_path(path: Path) -> Path:
  root_path = Path(__file__).parent
  return Path(root_path, path)


def get_json_path_to_dict(json_path: Path) -> dict:
  text_data = json_path.read_text()
  try:
    json_data = json.loads(text_data)
  except json.decoder.JSONDecodeError as e:
    import re
    regex = re.compile(r'/\*[\s\S]*?\*/|//.*')
    res_comment_json = regex.sub('', text_data)
    json_data = json.loads(res_comment_json)
    print(f'{e}\n\t-> json ファイル内のコメントを除去してデータ作成')
  return json_data

def get_all_theme_dict(themes_dir:Path):
  pass



def get_all_keys(theme_dict: dict):

  def _for_type_list(_list: list, parent: str):
    for n, v in enumerate(_list):
      if isinstance(v, dict):
        yield from _for_type_dict(v, f'{parent}||')
      elif isinstance(v, list):
        yield from _for_type_list(v, f'{parent}||')
      else:
        yield f'{parent}'

  def _for_type_dict(_dict: dict, parent: str):
    for k, v in _dict.items():
      if isinstance(v, dict):
        yield from _for_type_dict(v, f'{parent + k}::')
      elif isinstance(v, list):
        yield from _for_type_list(v, f'{parent + k}::')
      else:
        # todo: key が`scope` の場合、value を捕捉
        if k == 'scope':
          # xxx: 配列格納に揃える
          scopes = v if isinstance(v, list) else [v]
          for scope in scopes:
            yield f'{parent + k}>{scope}'

        yield f'{parent + k}'

  if isinstance(theme_dict, dict):
    yield from _for_type_dict(theme_dict, '')


def iterdir_loop(iterdir):
  for file_path in iterdir:
    theme_dict = get_json_path_to_dict(file_path)
    all_keys = get_all_keys(theme_dict)

    yield all_keys


def merge_all_keys_list(themes_dir: Path) -> list:
  themes_iter = themes_dir.iterdir()
  theme_keys = iterdir_loop(themes_iter)
  set_keys = set(chain.from_iterable(theme_keys))

  return sorted(list(set_keys))


if __name__ == '__main__':
  json_dir = './vscodeThemes'
  vs_themes_dir_path = get_target_path(json_dir)

  merge_list = merge_all_keys_list(vs_themes_dir_path)

