from pathlib import Path
import json

from dataclasses import dataclass

vscode_theme_path = Path(
  Path(__file__).parent, './vscodeThemes/iceberg.color-theme.json')
vscode_theme_dict = json.loads(vscode_theme_path.read_text())


def get_top_value(k: str, vs: dict) -> str | bool | None:
  return vs.get(k)


def get_colors_value(k: str, colors: dict) -> str | None:
  return colors.get(k)


def get_tokenColors_value(d: dict, tokenColors: list) -> str | None:
  scope = d.get('scope')
  settings = d.get('settings')
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
      #value = get_colors_value(v, theme_main.get(k)) if k == 'colors' else get_tokenColors_value(v, theme_main.get(k)) if k == 'tokenColors' else get_top_value(v, theme_main)
      if k == 'colors':
        value = get_colors_value(v, theme_main.get(k))
      elif k == 'tokenColors':
        value = get_tokenColors_value(v, theme_main.get(k))
      else:
        value = get_top_value(v, theme_main)
    if not value == None:
      return value


# todo: 辞書生成もっとシュッとできるといいけど、、、
_background = [
  dict(colors='editor.background'),
]
_bar_background = [
  {
    'colors': 'tab.activeBackground',
  },
]
_default_text = [
  dict(tokenColors=dict([
    ('scope', 'text'),
    ('settings', 'foreground'),
  ])),
]

_gutter_background = [
  {
    'colors': 'editorGutter.background',
  },
]

_gutter_border = [
  {
    'colors': 'tab.border',
  },
]

_library_background = [
  {
    'colors': 'sideBar.background',
  },
]
_line_number = [
  {
    'colors': 'editorLineNumber.foreground',
  },
]
_name = [
  {
    'top': 'name',
  },
]
_scopes_builtinfunction_color = [
  dict(tokenColors=dict([
    ('scope', 'entity.name.function'),
    ('settings', 'foreground'),
  ])),
]
_scopes_class_color = [
  dict(tokenColors=dict([
    ('scope', 'entity.name.class'),
    ('settings', 'foreground'),
  ])),
]
_scopes_classdef_color = [
  dict(tokenColors=dict([
    ('scope', 'entity.name.class'),
    ('settings', 'foreground'),
  ])),
]
_scopes_code_backgroundColor = [
  dict(tokenColors=dict([
    ('scope', 'markup.inline.raw.string'),
    ('settings', 'foreground'),
  ])),
]
_scopes_codeblockStart_color = [
  dict(tokenColors=dict([
    ('scope', 'markup.fenced_code.block'),
    ('settings', 'foreground'),
  ])),
]
_scopes_comment_color = [
  dict(tokenColors=dict([
    ('scope', 'comment'),
    ('settings', 'foreground'),
  ])),
]
_scopes_default_color = [
  dict(tokenColors=dict([
    ('scope', 'text'),
    ('settings', 'foreground'),
  ])),
]
_scopes_docstring_color = [
  dict(tokenColors=dict([
    ('scope', 'punctuation.definition.template-expression'),
    ('settings', 'foreground'),
  ])),
]
_scopes_formatting_color = [
  dict(tokenColors=dict([
    ('scope', 'markup.fenced_code.block'),
    ('settings', 'foreground'),
  ])),
]
_scopes_function_color = [
  dict(tokenColors=dict([
    ('scope', 'entity.name.function'),
    ('settings', 'foreground'),
  ])),
]
_scopes_functiondef_color = [
  dict(tokenColors=dict([
    ('scope', 'entity.name.function'),
    ('settings', 'foreground'),
  ])),
]
_scopes_keyword_color = [
  dict(tokenColors=dict([
    ('scope', 'keyword'),
    ('settings', 'foreground'),
  ])),
]
_scopes_module_color = [
  dict(tokenColors=dict([
    ('scope', 'entity.name.import.go'),
    ('settings', 'foreground'),
  ])),
]
_scopes_number_color = [
  dict(tokenColors=dict([
    ('scope', 'constant'),
    ('settings', 'foreground'),
  ])),
]
_scopes_string_color = [
  dict(tokenColors=dict([
    ('scope', 'string'),
    ('settings', 'foreground'),
  ])),
]
_scopes_taskDone_color = [
  dict(tokenColors=dict([
    ('scope', 'entity.other.attribute-name'),
    ('settings', 'foreground'),
  ])),
]
_separator_line = [
  {
    'colors': 'menu.separatorBackground',
  },
]
_tab_background = [
  {
    'colors': 'tab.inactiveBackground',
  },
]
_tab_title = [
  {
    'colors': 'tab.activeForeground',
  },
]
_text_selection_tint = [
  {
    'colors': 'editor.selectionBackground',
  },
]
_thumbnail_border = [
  {
    'colors': 'sideBar.border',
  },
]
_tint = [
  {
    'colors': 'activityBarBadge.background',
  },
]

set_keys = {
  'background': _background,
  'bar_background': _bar_background,
  'default_text': _default_text,
  'gutter_background': _gutter_background,
  'gutter_border': _gutter_border,
  'library_background': _library_background,
  'line_number': _line_number,
  'name': _name,
  'scopes_builtinfunction_color': _scopes_builtinfunction_color,
  'scopes_class_color': _scopes_class_color,
  'scopes_classdef_color': _scopes_classdef_color,
  'scopes_code_backgroundColor': _scopes_code_backgroundColor,
  'scopes_codeblockStart_color': _scopes_codeblockStart_color,
  'scopes_comment_color': _scopes_comment_color,
  'scopes_default_color': _scopes_default_color,
  'scopes_docstring_color': _scopes_docstring_color,
  'scopes_formatting_color': _scopes_formatting_color,
  'scopes_function_color': _scopes_function_color,
  'scopes_functiondef_color': _scopes_functiondef_color,
  'scopes_keyword_color': _scopes_keyword_color,
  'scopes_module_color': _scopes_module_color,
  'scopes_number_color': _scopes_number_color,
  'scopes_string_color': _scopes_string_color,
  'scopes_taskDone_color': _scopes_taskDone_color,
  'separator_line': _separator_line,
  'tab_background': _tab_background,
  'tab_title': _tab_title,
  'text_selection_tint': _text_selection_tint,
  'thumbnail_border': _thumbnail_border,
  'tint': _tint,
}

convert_dict = {
  k: get_vsdict_value(v, vscode_theme_dict)
  for k, v in set_keys.items()
}


@dataclass
class DataPalette:
  background: str = '#ff0000'
  bar_background: str = '#ff0000'
  dark_keyboard: bool = True
  default_text: str = '#ff0000'
  gutter_background: str = '#ff0000'
  gutter_border: str = '#ff0000'
  library_background: str = '#ff0000'
  library_tint: str = '#ff0000'
  line_number: str = '#ff0000'
  name: str = 'templateDefaultThemeSample'

  scopes_builtinfunction_color: str = '#ff0000'
  scopes_class_color: str = '#ff0000'
  scopes_classdef_color: str = '#ff0000'
  scopes_code_backgroundColor: str = '#ff0000'
  scopes_codeblockStart_color: str = '#ff0000'
  scopes_comment_color: str = '#ff0000'
  scopes_default_color: str = '#ff0000'
  scopes_docstring_color: str = '#ff0000'
  scopes_formatting_color: str = '#ff0000'
  scopes_function_color: str = '#ff0000'
  scopes_functiondef_color: str = '#ff0000'
  scopes_keyword_color: str = '#ff0000'
  scopes_module_color: str = '#ff0000'
  scopes_number_color: str = '#ff0000'
  scopes_string_color: str = '#ff0000'
  scopes_taskDone_color: str = '#ff0000'

  separator_line: str = '#ff0000'
  tab_background: str = '#ff0000'
  tab_title: str = '#ff0000'
  text_selection_tint: str = '#ff0000'
  thumbnail_border: str = '#ff0000'
  tint: str = '#ff0000'


def create_theme():
  pass


aa = DataPalette(**convert_dict)

