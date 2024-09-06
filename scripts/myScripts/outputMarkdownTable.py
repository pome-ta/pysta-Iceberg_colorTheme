from pathlib import Path
import json
import re

_vs_name = 'iceberg.color-theme.json'
_py_name = 'iceberg.color-theme.json'

root_path = Path(__file__).parent

themes_path = Path(root_path, '../dists/vscodeThemes')

#theme_path = list(themes_path.iterdir())[0]
theme_path = Path(themes_path, f'./{_vs_name}')
theme_dict = json.loads(theme_path.read_text())
file_name = theme_path.name

pyatas_path = Path(root_path, '../dists/dumps')

pysta_path = Path(pyatas_path, f'./{_py_name}')
pysta_dict = json.loads(pysta_path.read_text())
p_name = pysta_path.name

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


def set_colors_names(theme: dict, color_name: dict, idx: int):

  def _set_value(value: str | bool | None, parent: str, idx: int):
    if isinstance(value, str) and color_regex.match(value):
      color = value.upper()
      if isinstance(color_name.get(color), list):
        color_name[color][idx].append(parent.replace(' ', ''))

  def _for_type_list(lst: list, parent: str):
    for n, v in enumerate(lst):
      if isinstance(v, dict):
        k = v.get('scope')
        _for_type_dict(v, f'{parent}[{k}]::')

      elif isinstance(v, list):
        _for_type_list(v, f'{parent}[{n}]::')
      else:
        _set_value(v, f'{parent}[{v}]::', idx)

  def _for_type_dict(dct: dict, parent: str):
    for k, v in dct.items():
      if isinstance(v, dict):
        _for_type_dict(v, f'{parent + k}::')
      elif isinstance(v, list):
        _for_type_list(v, f'{parent + k}::')
      else:
        _set_value(v, f'{parent + k}', idx)

  if isinstance(theme, dict):
    _for_type_dict(theme, '')
    return color_name


vs_colors = list(set(get_all_values(theme_dict)))
st_colors = list(set(get_all_values(pysta_dict)))

colors = sorted(list(set(vs_colors + st_colors)))

# colors_names = dict.fromkeys(colors, [[],[] for _ in colors])
colors_names = {k: [[], []] for k in colors}

for n, t in enumerate([pysta_dict, theme_dict]):
  # for n, t in enumerate([theme_dict, pysta_dict]):
  colors_names = set_colors_names(t, colors_names, n)

md_fmt = '''
| color | Pythonista3 | VSCode |
| --- | --- | --- |
'''


def set_parameter(c: str) -> str:
  return f'![](https://via.placeholder.com/16/{c[1:]}/FFFFFF/?text=%20)`{c}`'


br = ' <br> '
for k, v in colors_names.items():
  rows = f'| {set_parameter(k)} | {br.join(v[0])} | {br.join(v[1])} |\n'
  md_fmt += rows

print(f'## `{p_name}` `{file_name}`')
print(md_fmt)
x = 1

