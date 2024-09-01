from pathlib import Path
import json

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


# todo: 辞書生成もっとシュッとできるといいけど、、、
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
}

