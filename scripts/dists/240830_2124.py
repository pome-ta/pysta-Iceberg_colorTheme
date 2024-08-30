from pathlib import Path
import json

# vscode_theme_path = Path('./vscodeThemes/iceberg.color-theme.json')
vscode_theme_path = Path(
  Path(__file__).parent, './vscodeThemes/iceberg.color-theme.json')
vscode_theme_dict = json.loads(vscode_theme_path.read_text())
file_name = vscode_theme_path.name

theme_dict = {
  'font-family': 'Menlo-Regular',
  'font-size': 10,
}

scopes = {
  'bold': {
    'font-style': 'bold',
  },
  'bold-italic': {
    'font-style': 'bold-italic',
  },
  'checkbox': {
    'checkbox': True,
  },
  'checkbox-done': {
    'checkbox': True,
    'done': True,
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
  'link': {
    'text-decoration': 'underline',
  },
  'bold-italic': {
    'font-style': 'bold-italic',
  },
  'project': {
    'font-style': 'bold',
  },
  'tag': {
    'text-decoration': 'none',
  },
  'task-done': {
    'text-decoration': 'strikeout',
  },
  'classdef': {
    'font-style': 'bold',
  },
  'code': {
    'corner-radius': 2,
  },
  'comment': {
    'font-style': 'italic',
  },
  'docstring': {
    'font-style': 'italic',
  },
  'functiondef': {
    'font-style': 'bold',
  },
}

theme_dict.update({
  'scopes': scopes,
})

#theme_dict.update({'name': vscode_theme_dict['name']})



setup_dict = [
  {
    'pysta': 'name',
    'vscode': [
      'name',
    ],
  },
  {
    'pysta': 'background',
    'vscode': [
      'colors',
      'editor.background',
    ],
  },
  {
    'pysta': 'bar_background',
    'vscode': [
      'colors',
      'tab.activeBackground',
    ],
  },
  {
    'pysta': 'default_text',
    'vscode': [
      'colors',
      'tab.activeBackground',
    ],
  },
]

