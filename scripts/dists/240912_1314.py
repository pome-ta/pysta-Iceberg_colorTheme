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
  #print(background)
  bar_background: str = ' #ff0000'
  dark_keyboard: bool = True
  default_text: str = '#ff0000' if True else '#00000'
  editor_actions_icon_background: str = '#ff0000'
  editor_actions_icon_tint: str = '#ff0000'
  editor_actions_popover_background: str = '#ff0000'
  error_text: str = '#ff0000'
  font_family: str = 'Menlo-Regular'
  font_size: float = 15.0
  gutter_background: str = '#ff0000'
  gutter_border: str = '#ff0000'
  interstitial: str = '#ff0000'
  library_background: str = '#ff0000'
  library_tint: str = '#ff0000'
  line_number: str = '#ff0000'
  name: str = 'tmpFormatDump'
  #print(scopes)
  #scopes:ScopesTemplate = ScopesTemplate(**scopes)# if scopes else ScopesTemplate()
  def __post_init__(self,**kwargs):
    print(kwargs)
    


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

