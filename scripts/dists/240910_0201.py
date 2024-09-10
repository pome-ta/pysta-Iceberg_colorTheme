"""
note: iceberg 完成を目指す
Pythonista3 もVSCode もわかりやすくやりたい
iceberg の色構成を改めて
"""
from pathlib import Path
import json


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

def get_all_colors_data(theme_dict: dict):

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
        yield from _for_type_dict(v, f'{parent}[]')
      elif isinstance(v, list):
        yield from _for_type_list(v, f'{parent}[]')
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




if __name__ == '__main__':
  json_dir = './vscodeThemes'
  json_name = 'iceberg.color-theme.json'
  vs_theme_path = get_target_path(Path(json_dir, json_name))

  json_data = get_json_path_to_dict(vs_theme_path)
  colors_dict = list(get_all_colors_data(vs_theme_path))

