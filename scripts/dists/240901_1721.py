from pathlib import Path
import json

vscode_theme_path = Path(
  Path(__file__).parent, './vscodeThemes/iceberg.color-theme.json')
vscode_theme_dict = json.loads(vscode_theme_path.read_text())


def get_top_value(k: str, vs: dict) -> str | bool:
  return vs.get(k)


def get_colors_value(k: str, colors: dict) -> str:
  return colors.get(k)


def get_tokenColors_value(d: dict, tokenColors: list) -> str:
  scope = d.get('scope')
  settings = d.get('settings')
  #print(scope, settings)
  for tokenColor in tokenColors:
    t_scope = tokenColor.get('scope')
    # xxx: 配列格納に合わせる
    t_scope = t_scope if isinstance(t_scope, list) else [t_scope]

    if scope in t_scope:
      return tokenColor.get('settings').get(settings)


def get_vsdict_value(items: list, theme_main: dict) -> str | bool | None:
  value = None
  for item in items:
    for k, v in item.items():
      '''
      if k == 'colors':
        value = get_colors_value(v, theme_main.get(k))
      elif k == 'tokenColors':
        value = get_tokenColors_value(v, theme_main.get(k))
      else:
        value = get_top_value(v, theme_main)
      '''
      value = get_colors_value(
        v, theme_main.get(k)) if k == 'colors' else get_tokenColors_value(
          v, theme_main.get(k)) if k == 'tokenColors' else get_top_value(
            v, theme_main)
    if not value == None:
      return value


d1 = [
  {
    'top': 'name',
  },
]
d2 = [
  {
    'hoge': 'activityBar.foreground',
  },
  {
    'colors': 'editor.background',
  },
]

d3 = [
  {
    'tokenColors': {
      'scope': 'comment',
      'settings': 'foreground',
    },
  },
]

a = get_vsdict_value(d3, vscode_theme_dict)

