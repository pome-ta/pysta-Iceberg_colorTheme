"""
note: それぞれの値の適応の仕方を考える
テンプレを持ってきて書き換えるか？
"""

from pathlib import Path
import json
from dataclasses import dataclass, field


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


@dataclass
class ThemeTemplate:
  __url: str = 'url'
  background: str = '#ff0000'
  bar_background: str = ' #ff0000'
  dark_keyboard: bool = True
  default_text: str = '#ff0000'
  editor_actions_icon_background: str = '#ff0000'
  editor_actions_icon_tint: str = '#ff0000'
  editor_actions_popover_background: str = '#ff0000'
  error_text: str = '#ff0000'
  #font_family: str = 'Menlo-Regular'
  #font_size: float = 15.0
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


def create_theme(convert_pallet: dict):
  p = ThemeTemplate(**convert_pallet)


if __name__ == '__main__':
  # xxx: 後にGitHub から持ってくる
  vs_dir = './vscodeThemes'
  vs_name = 'iceberg.color-theme.json'

  tmp_dir = './dumps'
  tmp_name = 'tmpFormatDump.json'

  tsdc = {'background': '#000000'}

  tt = ThemeTemplate(**tsdc)

