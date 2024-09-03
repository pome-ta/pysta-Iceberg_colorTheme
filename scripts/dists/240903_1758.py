from pathlib import Path
import json
import re

themes_path = Path(Path(__file__).parent, './vscodeThemes')

# for p in theme_path.iterdir():
#   print(p.name)

theme_path = list(themes_path.iterdir())[0]
theme_dict = json.loads(theme_path.read_text())

file_name = theme_path.name

#color_regex = re.compile(r'^#([\da-fA-F]{6}|[\da-fA-F]{3}||[\da-fA-F]{8})')
#color_regex = re.compile(r'^#[0-9a-fA-F]{3,6,8}')
color_regex = re.compile(r'^#[\da-fA-F]{3,8}')
# todo: `value` を一覧として、初手取り出し
def get_all_values(d: dict):
  for k, v in d.items():
    #print(v)
    if isinstance(v, str) and color_regex.match(v):
      print(v)
    elif isinstance(v, dict):
      get_all_values(v)


# todo: `key` でのテスト
# これだと、配列時の処理ができていない
def all_keys(a, parent=''):
  for key, value in a.items():
    yield parent + key
    if isinstance(value, dict):
      yield from all_keys(value, parent + key + '.')


# print(theme_path.name)

#vs = list(all_keys(theme_dict))
get_all_values(theme_dict)

x = 1
