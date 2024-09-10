"""
note: iceberg 完成を目指す
Pythonista3 もVSCode もわかりやすくやりたい
iceberg の色構成を改めて
"""

from pathlib import Path
import json
import re

color_regex = re.compile(r'^#[\da-fA-F]{3,8}')


def get_target_path(path: Path | str) -> Path:
  root_path = Path(__file__).parent
  return Path(root_path, path)


def get_json_path_to_dict(json_path: Path) -> dict:
  text_data = json_path.read_text()
  try:
    json_data = json.loads(text_data)
  except json.decoder.JSONDecodeError as e:
    regex = re.compile(r'/\*[\s\S]*?\*/|//.*')
    res_comment_json = regex.sub('', text_data)
    json_data = json.loads(res_comment_json)
    print(f'{e}\n\t-> json ファイル内のコメントを除去してデータ作成')
  return json_data


def joinkeys_values(theme_dict: dict):

  def _yield_key_value(vl: str, parent: str):
    yield (parent, vl)

  def _for_tokenColors(tokenColors: list, parent: str):

    scope

    for tokenColor in tokenColors:
      scope_name = tokenColor.get('scope')
      
      
      
      
      for k, v in tokenColor.items():
        scope_names = scope_names if isinstance(scope_names, list) else [sco]

  def _type_dict(dct: dict, parent: str):
    for k, v in dct.items():
      if k == 'tokenColors':
        pass
      elif isinstance(v, dict):
        yield from _type_dict(v, f'{parent + k}::')
        '''
      elif isinstance(v, list):
        yield from _type_list(v, f'{parent + k}::')
        '''
      else:
        yield from _yield_key_value(v, f'{parent + k}')

  if isinstance(theme_dict, dict):
    yield from _type_dict(theme_dict, '')


if __name__ == '__main__':
  json_dir = './vscodeThemes'
  json_name = 'iceberg.color-theme.json'

  vs_theme_path = get_target_path(Path(json_dir, json_name))
  vs_theme_data = get_json_path_to_dict(vs_theme_path)
  #colors = {k:v for k,v in joinkeys_values(vs_theme_data)}
  colors = dict(joinkeys_values(vs_theme_data))

