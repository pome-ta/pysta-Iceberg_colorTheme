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

    for tokenColor in tokenColors:
      _scope = tokenColor.get('scope')
      scope_names = _scope if isinstance(_scope, list) else [_scope]
      for scope_name in scope_names:
        settings = tokenColor.get('settings')
        for k, v in settings.items():
          yield from _yield_key_value(v, f'{parent}scope::{scope_name}::{k}')

  def _type_dict(dct: dict, parent: str):
    for k, v in dct.items():
      if k == 'tokenColors':
        yield from _for_tokenColors(v, f'{parent + k}::')
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


def get_colorcode_name_array(key_value: dict) -> list:

  # xxx: 2回ブン回してるけど、ええか
  def _filter_color_code(_key_value: dict):
    for k, v in _key_value.items():
      if color_regex.match(v):
        yield (k, v.upper())

  def _match_colorcodes(_key_value: dict) -> list[str, list[str]]:
    _color_pallet = sorted(set([v for v in _key_value.values()]))
    _codes_names = [[_code, []] for _code in _color_pallet]

    for k, v in _key_value.items():
      idx = _color_pallet.index(v)
      _codes_names[idx][1].append(k)
    return _codes_names

  names_codes_dict = dict(_filter_color_code(key_value))
  codes_names = _match_colorcodes(names_codes_dict)
  return codes_names


def create_markdown_table(data_array: list) -> str:
  pass


if __name__ == '__main__':
  json_dir = './vscodeThemes'
  json_name = 'iceberg.color-theme.json'

  # xxx: 関数名と変数名のルールがめちゃくちゃ

  vs_theme_path = get_target_path(Path(json_dir, json_name))
  vs_theme_data = get_json_path_to_dict(vs_theme_path)
  all_key_value = dict(joinkeys_values(vs_theme_data))
  colorcode_name_array = get_colorcode_name_array(all_key_value)

