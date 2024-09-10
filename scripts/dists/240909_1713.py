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


def set_parameter(c: str) -> str:
  return f'![](https://via.placeholder.com/16/{c[1:]}/FFFFFF/?text=%20)`{c}`'


def create_markdown_data(_theme_data: dict[dict]) -> str:
  new_line = '\n'
  separate = '|'

  def _rowline(*args) -> str:
    # xxx: スペースがあっちこっち行くの気持ち悪いな
    return f'{separate} ' + f' {separate} '.join(
      args) + f' {separate}' + new_line

  headers = [
    ['color_code', 'palette', 'key_name'],
    ['---', '---', '---'],
  ]
  # xxx: `join` キモい
  markdown_format_str = ''.join([_rowline(*h) for h in headers])
  for name, terminal_key_value in _theme_data.items():
    markdown_format_str = f'### {name}' + (new_line * 3) + markdown_format_str
    # xxx: いまさら愚直に
    ansi_list = []
    other_list = []
    for k, v in terminal_key_value.items():
      if ansi_regexp.match(k):
        ansi_list.append([v, set_parameter(v), k])
      else:
        other_list.append([v, set_parameter(v), k])
    markdown_format_str += ''.join([_rowline(*r) for r in ansi_list])
    markdown_format_str += ''.join([_rowline(*r) for r in other_list])

  return markdown_format_str


def create_themes_markdown_data(_themes_data: list[dict[dict]]) -> str:
  new_lines = '\n' * 2
  return new_lines.join(
    [create_markdown_data(theme) for theme in _themes_data])


if __name__ == '__main__':
  json_dir = './vscodeThemes'
  vs_themes_dir_path = get_target_path(json_dir)

  terminal_data_array = [{
    p.name:
    dict(get_terminal_key_value(get_json_path_to_dict(p)))
  } for p in vs_themes_dir_path.iterdir()]

  output_markdown = create_themes_markdown_data(terminal_data_array)
  print(output_markdown)

