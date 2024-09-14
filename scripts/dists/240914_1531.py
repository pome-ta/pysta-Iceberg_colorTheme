"""
note: iceberg 完成を目指す
適応とコメントつける
"""

from pathlib import Path
import json
from dataclasses import dataclass


def get_target_path(path: Path | str) -> Path:
  root_path = Path(__file__).parent
  return Path(root_path, path)


def get_json_path_to_dict(json_path: Path) -> dict:
  text_data = json_path.read_text()
  try:
    json_data = json.loads(text_data)
  except json.decoder.JSONDecodeError as e:
    import re
    regex = re.compile(r'/\*[\s\S]*?\*/|//.*')
    res_comment_json = regex.sub('', text_data)
    json_data = json.loads(res_comment_json)
    print(f'{e}\n\t-> json ファイル内のコメントを除去してデータ作成')
  return json_data


class VSTheme:

  def __init__(self, theme: Path | dict):
    # xxx: 文字列でのurl やjson は考慮しない
    # xxx: Path か、dict(json からの変換) のみ
    if isinstance(theme, dict):
      self.base_theme = theme
    else:
      self.base_theme = get_json_path_to_dict(theme)

  def __for_colors(self, key: str) -> str | bool | int | float | None:
    # xxx: `get` じゃなくて`[key]` の方がいいか?
    return self.base_theme['colors'].get(key)

  def __for_tokenColors(
      self, keys: list[str, str]) -> str | bool | int | float | None:
    scope, settings = keys
    for tokenColor in self.base_theme.get('tokenColors'):
      _scop = tokenColor.get('scope')
      # xxx: 配列格納に合わせる
      scopes = _scop if isinstance(_scop, list) else [_scop]
      if scope in scopes:
        return tokenColor.get('settings').get(settings)

  def get_value(
    self,
    search_value: str = '',
    colors: str | None = None,
    tokenColors: list[str, str] | None = None
  ) -> str | bool | int | float | None:
    value = None

    if search_value:
      value = self.base_theme.get(search_value)
    elif colors is not None and isinstance(colors, str):
      value = self.__for_colors(colors)
    elif tokenColors is not None and isinstance(tokenColors, list):
      value = self.__for_tokenColors(tokenColors)

    if value is None:
      raise print(
        f'VSTheme: value の値が`{value}` です:\n- {search_value=}\n- {colors=}\n- {tokenColors=}'
      )
    return value


@dataclass
class ThemeTemplate:
  url: str = 'url'
  background: str = '#ff0000'
  bar_background: str = ' #ff0000'
  dark_keyboard: bool = True
  default_text: str = '#ff0000'
  editor_actions_icon_background: str = '#ff0000'
  editor_actions_icon_tint: str = '#ff0000'
  editor_actions_popover_background: str = '#ff0000'
  error_text: str = '#ff0000'
  # font_family: str = 'Menlo-Regular'
  # font_size: float = 15.0
  gutter_background: str = '#ff0000'
  gutter_border: str = '#ff0000'
  interstitial: str = '#ff0000'
  library_background: str = '#ff0000'
  library_tint: str = '#ff0000'
  line_number: str = '#ff0000'
  name: str = 'tmpFormatDump'

  scopes_bold_font_style: str = 'bold'
  scopes_bold_italic_font_style: str = 'bold-italic'
  scopes_builtinfunction_color: str = '#ff0000'
  scopes_checkbox_checkbox: bool = True
  scopes_checkbox_done_checkbox: bool = True
  scopes_checkbox_done_done: bool = True
  scopes_class_color: str = '#ff0000'
  scopes_classdef_color: str = '#ff0000'
  scopes_code_backgroundColor: str = '#ff0000'
  scopes_code_corner_radius: float = 2.0
  scopes_codeblockStart_color: str = '#ff0000'
  scopes_decorator_color: str = '#ff0000'
  scopes_comment_color: str = '#ff0000'
  scopes_default_color: str = '#ff0000'
  scopes_docstring_color: str = '#ff0000'
  scopes_escape_color: str = '#ff0000'
  scopes_formatting_color: str = '#ff0000'
  scopes_function_color: str = '#ff0000'
  scopes_functiondef_color: str = '#ff0000'
  scopes_heading1_font_style: str = 'bold'
  scopes_heading2_font_style: str = 'bold'
  scopes_heading3_font_style: str = 'bold'
  scopes_italic_font_style: str = 'italic'
  scopes_keyword_color: str = '#ff0000'
  scopes_link_text_decoration: str = 'underline'
  scopes_marker_box_background_color: str = '#ff0000'
  scopes_marker_box_border_color: str = '#ff0000'
  scopes_marker_box_border: int = 4
  scopes_module_color: str = '#ff0000'
  scopes_number_color: str = '#ff0000'
  scopes_project_font_style: str = 'bold'
  scopes_string_color: str = '#ff0000'
  scopes_tag_text_decoration: str = 'none'
  scopes_taskDone_color: str = '#ff0000'
  scopes_taskDone_text_decoration: str = 'strikeout'

  separator_line: str = '#ff0000'
  tab_background: str = '#ff0000'
  tab_title: str = '#ff0000'
  text_selection_tint: str = '#ff0000'
  thumbnail_border: str = '#ff0000'
  tint: str = '#ff0000'


def create_theme_json(pallet: dict) -> str:

  # xxx: `None` が存在するか確認したいけど
  #     存在すれば、`True` ? `False` ? どっち?
  #     今回は、存在すれば、`True` (逆か?)
  def is_dict_in_none_value(d: dict | str | None, parent: str = '') -> bool:
    for k, v in d.items():
      if isinstance(v, dict):
        if is_dict_in_none_value(v, k):
          return False
      else:
        if v is None:
          print(f'value が、{parent=},{v=} です\nkey->{k=}: value->{v=}')
          return True
    return False

  p = ThemeTemplate(**pallet)
  dict_theme = {
    '__url': 'None',
    'background': p.background,
    'bar_background': p.bar_background,
    'dark_keyboard': p.dark_keyboard,
    'default_text': '#ff0000',
    'editor_actions_icon_background': '#ff0000',
    'editor_actions_icon_tint': '#ff0000',
    'editor_actions_popover_background': '#ff0000',
    'error_text': '#ff0000',
    'font-family': 'Menlo-Regular',
    'font-size': 15.0,
    'gutter_background': '#ff0000',
    'gutter_border': '#ff0000',
    'interstitial': '#ff0000',
    'library_background': '#ff0000',
    'library_tint': '#ff0000',
    'line_number': '#ff0000',
    'name': 'tmpFormatDump',
    'scopes': {
      'bold': {
        'font-style': 'bold',
      },
      'bold-italic': {
        'font-style': 'bold-italic',
      },
      'builtinfunction': {
        'color': '#ff0000',
      },
      'checkbox': {
        'checkbox': True,
      },
      'checkbox-done': {
        'checkbox': True,
        'done': True,
      },
      'class': {
        'color': '#ff0000',
      },
      'classdef': {
        'color': '#ff0000',
        'font-style': 'bold',
      },
      'code': {
        'background-color': '#ff0000',
        'corner-radius': 2.0,
      },
      'codeblock-start': {
        'color': '#ff0000',
      },
      'comment': {
        'color': '#ff0000',
        'font-style': 'italic',
      },
      'decorator': {
        'color': '#ff0000'
      },
      'default': {
        'color': '#ff0000',
      },
      'docstring': {
        'color': '#ff0000',
        'font-style': 'italic',
      },
      'escape': {
        'background-color': '#ff0000',
      },
      'formatting': {
        'color': '#ff0000',
      },
      'function': {
        'color': '#ff0000',
      },
      'functiondef': {
        'color': '#ff0000',
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
      },
      'italic': {
        'font-style': 'italic',
      },
      'keyword': {
        'color': '#ff0000',
      },
      'link': {
        'text-decoration': 'underline',
      },
      'marker': {
        'box-background-color': '#ff0000',
        'box-border-color': '#ff0000',
        'box-border-type': 4,
      },
      'module': {
        'color': '#ff0000',
      },
      'number': {
        'color': '#ff0000',
      },
      'project': {
        'font-style': 'bold',
      },
      'string': {
        'color': '#ff0000',
      },
      'tag': {
        'text-decoration': 'none',
      },
      'task-done': {
        'color': '#ff0000',
        'text-decoration': 'strikeout',
      },
    },
    'separator_line': '#ff0000',
    'tab_background': '#ff0000',
    'tab_title': '#ff0000',
    'text_selection_tint': '#ff0000',
    'thumbnail_border': '#ff0000',
    'tint': '#ff0000',
  }

  if is_dict_in_none_value(dict_theme):
    raise print('None の値があるため、変換できません')

  json_theme = json.dumps(dict_theme,
                          indent=1,
                          sort_keys=True,
                          ensure_ascii=False)
  return json_theme


if __name__ == '__main__':
  # xxx: 後にGitHub から持ってくる
  vs_dir = './vscodeThemes'
  vs_name = 'iceberg.color-theme.json'
  vs_path = get_target_path(Path(vs_dir, vs_name))

  vsc = VSTheme(vs_path)
  color_pallet = {
    'url': 'url',
    'background': vsc.get_value(colors='editor.background'),
    'bar_background': vsc.get_value(colors='tab.activeBackground'),
    'dark_keyboard': True,
    'default_text': vsc.get_value(tokenColors=['text', 'foreground']),
    'editor_actions_icon_background': '#ff0000',
    'editor_actions_icon_tint': '#ff0000',
    'editor_actions_popover_background': '#ff0000',
    'error_text': vsc.get_value(colors='editorError.foreground'),
    # 'font_family': 'Menlo-Regular'
    # 'font_size': 15.0
    'gutter_background': vsc.get_value(colors='editorGutter.background'),
    'gutter_border': vsc.get_value(colors='tab.border'),
    'interstitial': '#ff0000',
    'library_background': vsc.get_value(colors='sideBar.background'),
    'library_tint': vsc.get_value(colors='sideBar.foreground'),
    'line_number': '#ff0000',
    'name': 'tmpFormatDump',
    'scopes_bold_font_style': 'bold',
    'scopes_bold_italic_font_style': 'bold-italic',
    'scopes_builtinfunction_color': '#ff0000',
    'scopes_checkbox_checkbox': True,
    'scopes_checkbox_done_checkbox': True,
    'scopes_checkbox_done_done': True,
    'scopes_class_color': '#ff0000',
    'scopes_classdef_color': '#ff0000',
    'scopes_code_backgroundColor': '#ff0000',
    'scopes_code_corner_radius': 2.0,
    'scopes_codeblockStart_color': '#ff0000',
    'scopes_decorator_color': '#ff0000',
    'scopes_comment_color': '#ff0000',
    'scopes_default_color': '#ff0000',
    'scopes_docstring_color': '#ff0000',
    'scopes_escape_color': '#ff0000',
    'scopes_formatting_color': '#ff0000',
    'scopes_function_color': '#ff0000',
    'scopes_functiondef_color': '#ff0000',
    'scopes_heading1_font_style': 'bold',
    'scopes_heading2_font_style': 'bold',
    'scopes_heading3_font_style': 'bold',
    'scopes_italic_font_style': 'italic',
    'scopes_keyword_color': '#ff0000',
    'scopes_link_text_decoration': 'underline',
    'scopes_marker_box_background_color': '#ff0000',
    'scopes_marker_box_border_color': '#ff0000',
    'scopes_marker_box_border': 4,
    'scopes_module_color': '#ff0000',
    'scopes_number_color': '#ff0000',
    'scopes_project_font_style': 'bold',
    'scopes_string_color': '#ff0000',
    'scopes_tag_text_decoration': 'none',
    'scopes_taskDone_color': '#ff0000',
    'scopes_taskDone_text_decoration': 'strikeout',
    'separator_line': '#ff0000',
    'tab_background': '#ff0000',
    'tab_title': '#ff0000',
    'text_selection_tint': '#ff0000',
    'thumbnail_border': '#ff0000',
    'tint': '#ff0000',
  }

  out_json = create_theme_json(color_pallet)

