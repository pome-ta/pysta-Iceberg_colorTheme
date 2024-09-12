"""
note: それぞれの値の適応の仕方を考える
テンプレを持ってきて書き換えるか？
"""

from pathlib import Path
import json
from dataclasses import dataclass, field
'''

{
 scopes: {
  bold: {
   font-style: bold
  },
  bold-italic: {
   font-style: bold-italic
  },
  builtinfunction: {
   color: #ff0000
  },
  checkbox: {
   checkbox: true
  },
  checkbox-done: {
   checkbox: true,
   done: true
  },
  class: {
   color: #ff0000
  },
  classdef: {
   color: #ff0000,
   font-style: bold
  },
  code: {
   background-color: #ff0000,
   corner-radius: 2.0
  },
  codeblock-start: {
   color: #ff0000
  },
  comment: {
   color: #ff0000,
   font-style: italic
  },
  decorator: {
   color: #ff0000
  },
  default: {
   color: #ff0000
  },
  docstring: {
   color: #ff0000,
   font-style: italic
  },
  escape: {
   background-color: #ff0000
  },
  formatting: {
   color: #ff0000
  },
  function: {
   color: #ff0000
  },
  functiondef: {
   color: #ff0000,
   font-style: bold
  },
  heading-1: {
   font-style: bold
  },
  heading-2: {
   font-style: bold
  },
  heading-3: {
   font-style: bold
  },
  italic: {
   font-style: italic
  },
  keyword: {
   color: #ff0000
  },
  link: {
   text-decoration: underline
  },
  marker: {
   box-background-color: #ff0000,
   box-border-color: #ff0000,
   box-border-type: 4
  },
  module: {
   color: #ff0000
  },
  number: {
   color: #ff0000
  },
  project: {
   font-style: bold
  },
  string: {
   color: #ff0000
  },
  tag: {
   text-decoration: none
  },
  task-done: {
   color: #ff0000,
   text-decoration: strikeout
  }
 },
 
}

'''


@dataclass
class BoldTemplate:
  font_style: str = 'bold'


@dataclass
class Bold_ItalicTemplate:
  font_style: str = 'bold-italic'


@dataclass
class ScopesTemplate:
  bold: field(default_factory=dict)


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


if __name__ == '__main__':
  # xxx: 後にGitHub から持ってくる
  vs_dir = './vscodeThemes'
  vs_name = 'iceberg.color-theme.json'

  tmp_dir = './dumps'
  tmp_name = 'tmpFormatDump.json'
  
  
  tsdc = {'background':'#000000'}

  tt = ThemeTemplate(**tsdc)

