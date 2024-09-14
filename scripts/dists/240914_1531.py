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
  
  def __for_token_colors(self,
                         keys: list[str]) -> str | bool | int | float | None:
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
      tokenColors: list[str] | None = None) -> str | bool | int | float | None:
    value = None
    
    if search_value:
      value = self.base_theme.get(search_value)
    elif colors is not None and isinstance(colors, str):
      value = self.__for_colors(colors)
    elif tokenColors is not None and isinstance(tokenColors, list):
      value = self.__for_token_colors(tokenColors)
    
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
  scopes_classdef_font_style: str = 'bold'
  scopes_code_backgroundColor: str = '#ff0000'
  scopes_code_corner_radius: float = 2.0
  scopes_codeblockStart_color: str = '#ff0000'
  scopes_decorator_color: str = '#ff0000'
  scopes_comment_color: str = '#ff0000'
  scopes_comment_font_style: str = 'italic'
  scopes_default_color: str = '#ff0000'
  scopes_docstring_color: str = '#ff0000'
  scopes_docstring_font_style: str = 'italic'
  scopes_escape_color: str = '#ff0000'
  scopes_formatting_color: str = '#ff0000'
  scopes_function_color: str = '#ff0000'
  scopes_functiondef_color: str = '#ff0000'
  scopes_functiondef_font_style: str = 'bold'
  scopes_heading1_font_style: str = 'bold'
  scopes_heading2_font_style: str = 'bold'
  scopes_heading3_font_style: str = 'bold'
  scopes_italic_font_style: str = 'italic'
  scopes_keyword_color: str = '#ff0000'
  scopes_link_text_decoration: str = 'underline'
  scopes_marker_box_background_color: str = '#ff0000'
  scopes_marker_box_border_color: str = '#ff0000'
  scopes_marker_box_border_type: int = 4
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
    'default_text': p.default_text,
    'editor_actions_icon_background': p.editor_actions_icon_background,
    'editor_actions_icon_tint': p.editor_actions_icon_tint,
    'editor_actions_popover_background': p.editor_actions_popover_background,
    'error_text': p.error_text,
    'font-family': 'Menlo-Regular',
    'font-size': 15.0,
    'gutter_background': p.gutter_background,
    'gutter_border': p.gutter_border,
    'interstitial': p.interstitial,
    'library_background': p.library_background,
    'library_tint': p.library_tint,
    'line_number': p.line_number,
    'name': p.name,
    'scopes': {
      'bold': {
        'font-style': p.scopes_bold_font_style,
      },
      'bold-italic': {
        'font-style': p.scopes_bold_italic_font_style,
      },
      'builtinfunction': {
        'color': p.scopes_builtinfunction_color,
      },
      'checkbox': {
        'checkbox': p.scopes_checkbox_checkbox,
      },
      'checkbox-done': {
        'checkbox': p.scopes_checkbox_done_checkbox,
        'done': p.scopes_checkbox_done_done,
      },
      'class': {
        'color': p.scopes_class_color,
      },
      'classdef': {
        'color': p.scopes_classdef_color,
        'font-style': p.scopes_classdef_font_style,
      },
      'code': {
        'background-color': p.scopes_code_backgroundColor,
        'corner-radius': p.scopes_code_corner_radius,
      },
      'codeblock-start': {
        'color': p.scopes_codeblockStart_color,
      },
      'comment': {
        'color': p.scopes_comment_color,
        'font-style': p.scopes_comment_font_style,
      },
      'decorator': {
        'color': p.scopes_decorator_color,
      },
      'default': {
        'color': p.scopes_default_color,
      },
      'docstring': {
        'color': p.scopes_docstring_color,
        'font-style': p.scopes_docstring_font_style,
      },
      'escape': {
        'background-color': p.scopes_escape_color,
      },
      'formatting': {
        'color': p.scopes_formatting_color,
      },
      'function': {
        'color': p.scopes_function_color,
      },
      'functiondef': {
        'color': p.scopes_functiondef_color,
        'font-style': p.scopes_functiondef_font_style,
      },
      'heading-1': {
        'font-style': p.scopes_heading1_font_style,
      },
      'heading-2': {
        'font-style': p.scopes_heading2_font_style,
      },
      'heading-3': {
        'font-style': p.scopes_heading3_font_style,
      },
      'italic': {
        'font-style': p.scopes_italic_font_style,
      },
      'keyword': {
        'color': p.scopes_keyword_color,
      },
      'link': {
        'text-decoration': p.scopes_link_text_decoration,
      },
      'marker': {
        'box-background-color': p.scopes_marker_box_background_color,
        'box-border-color': p.scopes_marker_box_border_color,
        'box-border-type': p.scopes_marker_box_border_type,
      },
      'module': {
        'color': p.scopes_module_color,
      },
      'number': {
        'color': p.scopes_number_color,
      },
      'project': {
        'font-style': p.scopes_project_font_style,
      },
      'string': {
        'color': p.scopes_string_color,
      },
      'tag': {
        'text-decoration': p.scopes_tag_text_decoration,
      },
      'task-done': {
        'color': p.scopes_taskDone_color,
        'text-decoration': p.scopes_taskDone_text_decoration,
      },
    },
    'separator_line': p.separator_line,
    'tab_background': p.tab_background,
    'tab_title': p.tab_title,
    'text_selection_tint': p.text_selection_tint,
    'thumbnail_border': p.thumbnail_border,
    'tint': p.tint,
  }
  
  if is_dict_in_none_value(dict_theme):
    raise print('None の値があるため、変換できません')
  
  json_theme = json.dumps(dict_theme,
                          indent=1,
                          sort_keys=True,
                          ensure_ascii=False)
  return json_theme


def get_vs_theme_base(path: Path) -> VSTheme:
  vs_path = get_target_path(path)
  return VSTheme(vs_path)


def export_theme(json_theme: str,
                 file_name: str,
                 tmp_dir: Path | None = None) -> None:
  def get_user_themes_dir() -> Path | None:
    try:
      # todo: 一応
      from objc_util import ObjCClass
    except ModuleNotFoundError:
      return None
    _path_objc = ObjCClass('PA2UITheme').sharedTheme().userThemesPath()
    _path = Path(str(_path_objc))
    return _path if _path.exists() else None
  
  user_themes_dir = get_user_themes_dir()
  for n, p in enumerate([user_themes_dir, tmp_dir]):
    if p is None:
      continue
    
    # todo: `tmp_dir` の場合のみ
    #dir_path = p.mkdir(parents=True, exist_ok=True) if n else p
    dir_path = p
    json_path = Path(dir_path, file_name)
    json_path.write_text(json_theme, encoding='utf-8')


if __name__ == '__main__':
  # xxx: 後にGitHub から持ってくる
  vs_dir = './vscodeThemes'
  vs_name = 'iceberg.color-theme.json'
  vs_target = Path(vs_dir, vs_name)
  vs_filename = vs_target.name
  
  
  
  vsc = get_vs_theme_base(vs_target)
  
  color_pallet = {
    'url':
      'url',
    'background':
      vsc.get_value(colors='editor.background'),
    'bar_background':
      vsc.get_value(colors='tab.activeBackground'),
    'dark_keyboard':
      True,
    'default_text':
      vsc.get_value(tokenColors=['text', 'foreground']),
    'editor_actions_icon_background':
      '#ff0000',
    'editor_actions_icon_tint':
      '#ff0000',
    'editor_actions_popover_background':
      '#ff0000',
    'error_text':
      vsc.get_value(colors='editorError.foreground'),
    # 'font_family': 'Menlo-Regular'
    # 'font_size': 15.0
    'gutter_background':
      vsc.get_value(colors='editorGutter.background'),
    'gutter_border':
      vsc.get_value(colors='tab.border'),
    'interstitial':
      '#ff0000',
    'library_background':
      vsc.get_value(colors='sideBar.background'),
    'library_tint':
      vsc.get_value(colors='sideBar.foreground'),
    'line_number':
      vsc.get_value(colors='editorLineNumber.foreground'),
    'name':
      vsc.get_value('name'),
    'scopes_bold_font_style':
      'bold',
    'scopes_bold_italic_font_style':
      'bold-italic',
    'scopes_builtinfunction_color':
      vsc.get_value(tokenColors=['entity.name.function', 'foreground']),
    'scopes_checkbox_checkbox':
      True,
    'scopes_checkbox_done_checkbox':
      True,
    'scopes_checkbox_done_done':
      True,
    'scopes_class_color':
      vsc.get_value(tokenColors=['entity.name.class', 'foreground']),
    'scopes_classdef_color':
      vsc.get_value(tokenColors=['entity.name.class', 'foreground']),
    'scopes_classdef_font_style':
      'bold',
    'scopes_code_backgroundColor':
      vsc.get_value(tokenColors=['markup.fenced_code.block', 'foreground']),
    'scopes_code_corner_radius':
      2.0,
    'scopes_codeblockStart_color':
      vsc.get_value(tokenColors=['markup.inline.raw.string', 'foreground']),
    'scopes_decorator_color':
      vsc.get_value(tokenColors=['text', 'foreground']),
    'scopes_comment_color':
      vsc.get_value(tokenColors=['comment', 'foreground']),
    'scopes_comment_font_style':
      0,
    'scopes_default_color':
      vsc.get_value(tokenColors=['text', 'foreground']),
    'scopes_docstring_color':
      vsc.get_value(tokenColors=['punctuation.definition.template-expression', 'foreground']),
    'scopes_docstring_font_style': 'italic',
    'scopes_escape_color':
      vsc.get_value(tokenColors=['entity.other.attribute-name', 'foreground']),
    'scopes_formatting_color':
      vsc.get_value(tokenColors=['markup.fenced_code.block', 'foreground']),
    'scopes_function_color':
      vsc.get_value(tokenColors=['entity.name.function', 'foreground']),
    'scopes_functiondef_color':
      vsc.get_value(tokenColors=['entity.name.function', 'foreground']),
    'scopes_functiondef_font_style': 'bold',
    'scopes_heading1_font_style':
      'bold',
    'scopes_heading2_font_style':
      'bold',
    'scopes_heading3_font_style':
      'bold',
    'scopes_italic_font_style':
      'italic',
    'scopes_keyword_color':
      vsc.get_value(tokenColors=['keyword', 'foreground']),
    'scopes_link_text_decoration':
      'underline',
    'scopes_marker_box_background_color':
      vsc.get_value(colors='editorMarkerNavigation.background'),
    'scopes_marker_box_border_color':
      vsc.get_value(colors='inputOption.activeBorder'),
    'scopes_marker_box_border_type':
      4,
    'scopes_module_color':
      vsc.get_value(tokenColors=['entity.name.import.go', 'foreground']),
    'scopes_number_color':
      vsc.get_value(tokenColors=['constant', 'foreground']),
    'scopes_project_font_style':
      'bold',
    'scopes_string_color':
      vsc.get_value(tokenColors=['string', 'foreground']),
    'scopes_tag_text_decoration':
      'none',
    'scopes_taskDone_color':
      vsc.get_value(colors='notificationsInfoIcon.foreground'),
    'scopes_taskDone_text_decoration':
      'strikeout',
    'separator_line':
      vsc.get_value(colors='focusBorder'),
    'tab_background':
      vsc.get_value(colors='tab.inactiveBackground'),
    'tab_title':
      vsc.get_value(colors='tab.inactiveForeground'),
    'text_selection_tint':
      vsc.get_value(colors='selection.background'),
    'thumbnail_border':
      vsc.get_value(colors='sideBar.border'),
    'tint':
      vsc.get_value(colors='editorCursor.foreground'),
  }
  
  out_json = create_theme_json(color_pallet)
  export_dir = Path('./testThemes')
  export_theme(out_json, vs_filename, export_dir)
