from pathlib import Path
import json
import re

themes_path = Path(Path(__file__).parent, './vscodeThemes')

theme_path = list(themes_path.iterdir())[0]
theme_dict = json.loads(theme_path.read_text())

file_name = theme_path.name

color_regex = re.compile(r'^#[\da-fA-F]{3,8}')


# todo: `value` を一覧として、初手取り出し
def get_all_values(vs_theme: dict):
  # color_regex = re.compile(r'^#([\da-fA-F]{6}|[\da-fA-F]{3}||[\da-fA-F]{8})')
  # color_regex = re.compile(r'^#[0-9a-fA-F]{3,6,8}')
  # color_regex = re.compile(r'^#[\da-fA-F]{3,8}')

  def _yield_value(value: str | bool | None):
    if isinstance(value, str) and color_regex.match(value):
      yield value.upper()

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

  if isinstance(vs_theme, dict):
    yield from _for_type_dict(vs_theme)


# todo: `key` でのテスト
# これだと、配列時の処理ができていない
'''
def all_keys(a, parent=''):
  for key, value in a.items():
    yield parent + key
    if isinstance(value, dict):
      yield from all_keys(value, parent + key + '.')
'''


def get_all_keys(vs_theme: dict):

  def _yield_value(value: str | bool | None, parent: str):
    # yield f'{parent + str(value)}'
    # yield parent
    if isinstance(value, str) and color_regex.match(value):
      yield parent

  def _for_type_list(lst: list, parent: str):
    for n, v in enumerate(lst):
      if isinstance(v, dict):
        print('in dic')
        # print(v)
        k = v.get('scope')

        # yield from _for_type_dict(v, f'{parent}[{k[n] if isinstance(k, list) else k}] | ')
        yield from _for_type_dict(v, f'{parent}[{k}] :: ')

      elif isinstance(v, list):
        # xxx: ここのパターン数ない
        print('in list')
        yield from _for_type_list(v, f'{parent}[{n}] :: ')
      else:
        # print('in val')
        yield from _yield_value(v, f'{parent}[{v}] :: ')

  def _for_type_dict(dct: dict, parent: str):
    for k, v in dct.items():
      if isinstance(v, dict):
        yield from _for_type_dict(v, f'{parent + k} :: ')
      elif isinstance(v, list):
        yield from _for_type_list(v, f'{parent + k} :: ')
      else:
        yield from _yield_value(v, f'{parent + k}')

  if isinstance(vs_theme, dict):
    yield from _for_type_dict(vs_theme, '')


# print(theme_path.name)

# vs = list(all_keys(theme_dict))
all_values = sorted(list(set(get_all_values(theme_dict))))
all_keys = list(get_all_keys(theme_dict))

x = 1

