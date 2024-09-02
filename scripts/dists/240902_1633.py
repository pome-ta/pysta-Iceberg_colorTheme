from pathlib import Path
import json
from dataclasses import dataclass

import requests

from objc_util import ObjCClass

root_path = Path(__file__).parent

vscode_theme_path = Path(root_path, './vscodeThemes/iceberg.color-theme.json')
file_name = vscode_theme_path.name
vscode_theme_dict = json.loads(vscode_theme_path.read_text())
'''
url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'
params = {
  'raw': 'true',
}

response = requests.get(url, params)
vscode_theme_dict = response.json()
file_name = Path(url).name
'''

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
  dict(colors='tab.activeBackground'),
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
_library_tint = [
  {
    'colors': 'sideBar.border',
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
  'library_tint': _library_tint,
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


# xxx: `None` が存在するか確認したいけど
#     存在すれば、`True` ? `False` ? どっちだ？
#     今回は、存在すれば、`True` （やはり逆か？）
def check_dict_none(d: dict | str | None, parent: str = '') -> bool:
  for k, v in d.items():
    if isinstance(v, dict):
      if check_dict_none(v, k):
        return False
    else:
      if v == None:
        print(f'value が、{parent},{v} です\nkey->{k}: value->{v}')
        return True
  return False


def create_theme_json(convert_pallet: dict) -> str:
  p = DataPalette(**convert_pallet)
  _theme_dict = {
    'background': p.background,
    'bar_background': p.bar_background,
    'dark_keyboard': p.dark_keyboard,
    'default_text': p.default_text,
    'font-family': 'Menlo-Regular',
    'font-size': 12.0,
    'gutter_background': p.gutter_background,
    'gutter_border': p.gutter_border,
    'library_background': p.library_background,
    'library_tint': p.library_tint,
    'line_number': p.line_number,
    'name': p.name,
    'scopes': {
      'bold': {
        'font-style': 'bold',
      },
      'bold-italic': {
        'font-style': 'bold-italic',
      },
      'builtinfunction': {
        'color': p.scopes_builtinfunction_color,
      },
      'checkbox': {
        'checkbox': True,
      },
      'checkbox-done': {
        'checkbox': True,
        'done': True,
      },
      'class': {
        'color': p.scopes_class_color,
      },
      'classdef': {
        'color': p.scopes_classdef_color,
        'font-style': 'bold',
      },
      'code': {
        'background-color': p.scopes_code_backgroundColor,
        'corner-radius': 2.0,
      },
      'codeblock-start': {
        'color': p.scopes_codeblockStart_color,
      },
      'comment': {
        'color': p.scopes_comment_color,
        'font-style': 'italic',
      },
      'default': {
        'color': p.scopes_default_color,
      },
      'docstring': {
        'color': p.scopes_docstring_color,
        'font-style': 'italic',
      },
      'formatting': {
        'color': p.scopes_formatting_color,
      },
      'function': {
        'color': p.scopes_function_color,
      },
      'functiondef': {
        'color': p.scopes_functiondef_color,
        'font-style': 'bold',
      },
      'heading-1': {
        'font-style': 'bold',
      },
      'heading-2': {
        'font-style': 'bold',
      },
      'heading-3': {
        'font-style': 'bold',
        # 'font-style': None,
      },
      'italic': {
        'font-style': 'italic',
      },
      'keyword': {
        'color': p.scopes_keyword_color,
      },
      'link': {
        'text-decoration': 'underline',
      },
      'module': {
        'color': p.scopes_module_color,
      },
      'number': {
        'color': p.scopes_number_color,
      },
      'project': {
        'font-style': 'bold',
      },
      'string': {
        'color': p.scopes_string_color,
      },
      'tag': {
        'text-decoration': 'none',
      },
      'task-done': {
        'color': p.scopes_taskDone_color,
        'text-decoration': 'strikeout',
      },
    },
    'separator_line': p.separator_line,
    'tab_background': p.tab_background,
    'tab_title': p.tab_title,
    'text_selection_tint': p.text_selection_tint,
    'thumbnail_border': p.thumbnail_border,
    'tint': p.tint,
  }

  if not check_dict_none(_theme_dict):
    json_str = json.dumps(_theme_dict,
                          indent=1,
                          sort_keys=True,
                          ensure_ascii=False)
    return json_str
  else:
    print('None の値があるため、変換できません')


theme_json = create_theme_json(convert_dict)


def export_theme(json_data: str, json_name: str, target: Path) -> None:
  json_path = Path(target, json_name)
  json_path.write_text(json_data, encoding='utf-8')


userThemesPath_objc = ObjCClass('PA2UITheme').sharedTheme().userThemesPath()
user_themes_path = Path(str(userThemesPath_objc))
testThemes_path = Path(root_path, './testThemes')

for p in [user_themes_path, testThemes_path]:
  export_theme(theme_json, file_name, p)

