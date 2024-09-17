from dataclasses import dataclass


@dataclass
class ThemeTemplate:
  url: str = 'github_url'
  author: str = 'author_name'
  license: str = 'license'
  pushed_at: str = 'pushed_at'

  # xxx: これで全部だっけ？
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

