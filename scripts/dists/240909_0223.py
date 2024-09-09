"""
note: VSCode のtheme `terminal` color 一覧
`ansi〜` は、全部のtheme が持ってるはず
"""

from pathlib import Path
import json
import re

terminal_regexp = re.compile(r'^(?=.*terminal).*$')
ansi_regexp = re.compile(r'^.*\.ansi.*$')


def get_target_path(path: Path | str) -> Path:
  root_path = Path(__file__).parent
  return Path(root_path, path)


def get_json_path_to_dict(json_path: Path) -> dict:
  text_data = json_path.read_text()
  try:
    json_data = json.loads(text_data)
  except json.decoder.JSONDecodeError as e:
    regexp = re.compile(r'/\*[\s\S]*?\*/|//.*')
    res_comment_json = regexp.sub('', text_data)
    json_data = json.loads(res_comment_json)
    print(f'{e}\n\t-> json ファイル内のコメントを除去してデータ作成')
  return json_data


def get_terminal_key_value(_theme_data: dict):
  # xxx: ここまで冗長的にしなくてもいいかも

  def _yield_key_value(_key, _value):
    # xxx: `tuple` にして投げ先で`dict` 化
    yield _key, _value

  def _for_type_list(_list: list):
    for v in _list:
      if isinstance(v, dict):
        yield from _for_type_dict(v)
      elif isinstance(v, list):
        yield from _for_type_list(v)

  def _for_type_dict(_dict: dict):
    for k, v in _dict.items():
      if terminal_regexp.match(k):
        yield from _yield_key_value(k, v)
      elif isinstance(v, dict):
        yield from _for_type_dict(v)
      elif isinstance(v, list):
        yield from _for_type_list(v)

  if isinstance(_theme_data, dict):
    yield from _for_type_dict(_theme_data)


def create_markdown_data(_theme_data: dict[dict]) -> str:

  def _rowline(*args) -> str:
    pass

  new_line = '\n'
  br_tag = ' <br> '
  markdown_format_str = ''
  for name, terminal_key_value in _theme_data.items():
    pass


def create_themes_markdown_data(_themes_data: list[dict[dict]]) -> str:
  new_lines = '\n' * 2
  markdown_format_str = ''


if __name__ == '__main__':
  json_dir = './vscodeThemes'
  vs_themes_dir_path = get_target_path(json_dir)

  terminal_data_array = [{
    p.name:
    dict(get_terminal_key_value(get_json_path_to_dict(p)))
  } for p in vs_themes_dir_path.iterdir()]

  markdown_str = ''

