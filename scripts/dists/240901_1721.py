from pathlib import Path
import json

vscode_theme_path = Path(
  Path(__file__).parent, './vscodeThemes/iceberg.color-theme.json')
vscode_theme_dict = json.loads(vscode_theme_path.read_text())


def get_top_value(k: str, vs: dict) -> str | bool:
  return vs.get(k)


def get_colors_value(k: str, colors: dict) -> str:
  return colors.get(k)


def get_tokenColors_value(k: str, tokenColors: dict) -> str:
  pass


def get_vsdict_value(keys: list, theme_main: dict) -> str | bool:
  v = None
  for k in keys:
    if k == 'colors':
      pass
    elif k == 'tokenColors':
      pass
    else:
      v = get_top_value(k, theme_main)
    if not v == None:
      return v


d1 = [
  'hoge',
  'name',
]
d2 = [
  {
    'colors',
    'editor.background',
  },
]
a = get_vsdict_value(d1, vscode_theme_dict)

