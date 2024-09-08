"""
note: VSCode のtheme の要素出現調査

各Theme ごとの突き合わせ
"""

from pathlib import Path
import json
from itertools import chain


def get_target_path(path: Path | str) -> Path:
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


def get_all_keys(theme_dict: dict):

  def _yield_keys(_keys: str, maybe_scope: None | list | str = None):
    # todo: key が`scope` の場合、value を捕捉
    if maybe_scope:
      # xxx: 配列格納に揃える
      scopes = maybe_scope if isinstance(maybe_scope, list) else [maybe_scope]
      for scope in scopes:
        yield f'{_keys}>{scope}'
    else:
      yield f'{_keys}'

  def _for_type_list(_list: list, parent: str):
    for n, v in enumerate(_list):
      if isinstance(v, dict):
        yield from _for_type_dict(v, f'{parent}||')
      elif isinstance(v, list):
        yield from _for_type_list(v, f'{parent}||')
      else:
        yield from _yield_keys(f'{parent}', None)

  def _for_type_dict(_dict: dict, parent: str):
    for k, v in _dict.items():
      if k == 'scope':
        yield from _yield_keys(f'{parent + k}', v)
      elif isinstance(v, dict):
        yield from _for_type_dict(v, f'{parent + k}::')
      elif isinstance(v, list):
        yield from _for_type_list(v, f'{parent + k}::')
      else:
        yield from _yield_keys(f'{parent + k}', None)

  if isinstance(theme_dict, dict):
    yield from _for_type_dict(theme_dict, '')


def theme_path_to_theme_data(path: Path) -> dict[str, list]:
  name = path.name
  json_dict = get_json_path_to_dict(path)
  all_keys = get_all_keys(json_dict)
  set_sorted_keys = sorted(set(all_keys))
  #set_sorted_keys = list(set(all_keys))
  return {name: set_sorted_keys}


def get_primary_keys(_name_keys_array: list) -> list:
  set_keys: set
  for n, name_keys in enumerate(_name_keys_array):
    for name, keys in name_keys.items():
      set_keys = set_keys & set(keys) if n else set(keys)
  list_keys = sorted(list(set_keys))
  return list_keys


if __name__ == '__main__':
  json_dir = './vscodeThemes'
  vs_themes_dir_path = get_target_path(json_dir)
  # todo: 各theme を辞書で取得
  name_keys_array = [
    theme_path_to_theme_data(p) for p in vs_themes_dir_path.iterdir()
  ]

  primary_keys = get_primary_keys(name_keys_array)

  print(primary_keys[69])

