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


def get_all_keys(vs_theme: dict):
  def _yield_value(value: str | bool | None, parent: str):
    # yield f'{parent + str(value)}'
    # yield parent
    if isinstance(value, str) and color_regex.match(value):
      yield parent
  
  def _for_type_list(lst: list, parent: str):
    for n, v in enumerate(lst):
      if isinstance(v, dict):
        # print('in dic')
        # print(v)
        k = v.get('scope')
        
        # yield from _for_type_dict(v, f'{parent}[{k[n] if isinstance(k, list) else k}] | ')
        yield from _for_type_dict(v, f'{parent}[{k}] :: ')
      
      elif isinstance(v, list):
        # xxx: ここのパターン数ない
        # print('in list')
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


def set_colors_names(vs_theme: dict, color_list: list):
  color_name = dict.fromkeys(color_list, [])
  
  def _yield_value(value: str | bool | None, parent: str):
    if isinstance(value, str) and color_regex.match(value):
      color = value.upper()
      if isinstance(color_name.get(color), list):
        color_name[color].append(parent)
  
  def _for_type_list(lst: list, parent: str):
    for n, v in enumerate(lst):
      if isinstance(v, dict):
        k = v.get('scope')
        _for_type_dict(v, f'{parent}[{k}] :: ')
      
      elif isinstance(v, list):
        _for_type_list(v, f'{parent}[{n}] :: ')
      else:
        _yield_value(v, f'{parent}[{v}] :: ')
  
  def _for_type_dict(dct: dict, parent: str):
    for k, v in dct.items():
      if isinstance(v, dict):
        _for_type_dict(v, f'{parent + k} :: ')
      elif isinstance(v, list):
        _for_type_list(v, f'{parent + k} :: ')
      else:
        _yield_value(v, f'{parent + k}')
  
  if isinstance(vs_theme, dict):
    _for_type_dict(vs_theme, '')
    return color_name


colors_set = sorted(list(set(get_all_values(theme_dict))))

colors_names = set_colors_names(theme_dict, colors_set)

x = 1
