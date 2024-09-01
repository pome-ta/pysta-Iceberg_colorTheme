from pathlib import Path
import json

from objc_util import ObjCClass

tmp_theme_dict = {
  'background': '#ff0000',
  'bar_background': '#ff0000',
  'default_text': '#ff0000',
  'font-family': 'Menlo-Regular',
  'font-size': 12.0,
  'gutter_background': '#ff0000',
  'gutter_border': '#ff0000',
  'library_background': '#ff0000',
  'line_number': '#ff0000',
  'name': 'minimumTemplateDefaultThemeSample',
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
    'default': {
      'color': '#ff0000',
    },
    'docstring': {
      'color': '#ff0000',
      'font-style': 'italic',
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
'''
themes_path = Path(str(ObjCClass('PA2UITheme').sharedTheme().userThemesPath()))
'''
json_str = json.dumps(tmp_theme_dict,
                      indent=1,
                      sort_keys=True,
                      ensure_ascii=False)
json_file_name = f'{tmp_theme_dict["name"]}.json'

root_path = Path(__file__).parent
move_path = Path(root_path, './dumps', json_file_name)

move_path.write_text(json_str, encoding='utf-8')
