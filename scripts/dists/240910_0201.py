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


def unique_color_code_array(theme_data: dict) -> list:

  def _get_color_codes(_theme_data: dict):

    def _yield_value(vl: str | bool | None):
      if isinstance(vl, str) and color_regex.match(vl):
        yield vl.upper()

    def _for_type_list(lst: list):
      for v in lst:
        if isinstance(v, dict):
          yield from _for_type_dict(v)
        elif isinstance(v, list):
          yield from _for_type_list(v)
        else:
          yield from _yield_value(v)

    def _for_type_dict(dct: dict):
      for k, v in dct.items():
        if isinstance(v, dict):
          yield from _for_type_dict(v)
        elif isinstance(v, list):
          yield from _for_type_list(v)
        else:
          yield from _yield_value(v)

    if isinstance(_theme_data, dict):
      yield from _for_type_dict(_theme_data)

  set_codes = set(_get_color_codes(theme_data))
  return sorted(set_codes)


if __name__ == '__main__':
  json_dir = './vscodeThemes'
  json_name = 'iceberg.color-theme.json'
  vs_theme_path = get_target_path(Path(json_dir, json_name))

  json_data = get_json_path_to_dict(vs_theme_path)
  unique_color_codes = unique_color_code_array(json_data)

