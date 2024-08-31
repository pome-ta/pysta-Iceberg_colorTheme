from pathlib import Path
import json


# def get_vs_value(value, vs_dict):
#   if isinstance(value, dict):
#     for k, v in value.items():
#       return get_vs_value(v, vs_dict[k])

#   elif isinstance(value, list):
#     for i in value:
#       pass
#   else:
#     return vs_dict[value]


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

# theme_dict.update({
#   'scopes': scopes,
# })

#theme_dict.update({'name': vscode_theme_dict['name']})

setup_dict = [
  {
    'pysta': 'name',
    'vscode': 'name',
  },
  {
    'pysta': 'background',
    'vscode': {
      'colors': 'editor.background',
    },
  },
  {
    'pysta': 'bar_background',
    'vscode': {
      'colors': 'tab.activeBackground',
    },
  },
  {
    'pysta': 'default_text',
    'vscode': {
      'tokenColors': {
        'text': 'foreground',
      },
    },
  },
  {
    'pysta': 'gutter_background',
    'vscode': {
      'colors': 'editorGutter.background',
    },
  },
  {
    'pysta': 'gutter_border',
    'vscode': {
      'colors': 'tab.border',
    },
  },
  {
    'pysta': 'library_background',
    'vscode': {
      'colors': 'sideBar.background',
    },
  },
  {
    'pysta': 'line_number',
    'vscode': {
      'colors': 'editorLineNumber.foreground',
    },
  },
  {
    'pysta': 'separator_line',
    'vscode': {
      'colors': 'menu.separatorBackground',
    },
  },
  {
    'pysta': 'tab_background',
    'vscode': {
      'colors': 'tab.inactiveBackground',
    },
  },
  {
    'pysta': 'tab_title',
    'vscode': {
      'colors': 'tab.activeForeground',
    },
  },
  {
    'pysta': 'text_selection_tint',
    'vscode': {
      'colors': 'editor.selectionBackground',
    },
  },
  {
    'pysta': 'thumbnail_border',
    'vscode': {
      'colors': 'sideBar.border',
    },
  },
  {
    'pysta': 'tint',
    'vscode': {
      'colors': 'activityBarBadge.background',
    },
  },
  {
    'pysta': {
      'scopes': {'builtinfunction':'color',},
    },
    'vscode': {
      'tokenColors': {
        'entity.name.function': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'class',
    },
    'vscode': {
      'tokenColors': {
        'entity.name.class': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'classdef',
    },
    'vscode': {
      'tokenColors': {
        'entity.name.class': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'code',
    },
    'vscode': {
      'tokenColors': {
        'markup.inline.raw.string': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'codeblock-start',
    },
    'vscode': {
      'tokenColors': {
        'markup.fenced_code.block': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'comment',
    },
    'vscode': {
      'tokenColors': {
        'comment': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'default',
    },
    'vscode': {
      'tokenColors': {
        'text': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'docstring',
    },
    'vscode': {
      'tokenColors': {
        'punctuation.definition.template-expression': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'formatting',
    },
    'vscode': {
      'tokenColors': {
        'markup.fenced_code.block': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'function',
    },
    'vscode': {
      'tokenColors': {
        'entity.name.function': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'functiondef',
    },
    'vscode': {
      'tokenColors': {
        'entity.name.function': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'keyword',
    },
    'vscode': {
      'tokenColors': {
        'keyword': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'number',
    },
    'vscode': {
      'tokenColors': {
        'constant': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'string',
    },
    'vscode': {
      'tokenColors': {
        'string': 'foreground',
      },
    },
  },
  {
    'pysta': {
      'scopes': 'task-done ',
    },
    'vscode': {
      'tokenColors': {
        'entity.other.attribute-name': 'foreground',
      },
    },
  },
]


# todo: 依存ゴリゴリで、ネストも深くてきもいけど、とりあえず
def get_vsTheme_value(value, theme_dict):
  if value == 'name':
    return theme_dict[value]
  for k, v in value.items():
    if k == 'colors':
      return theme_dict[k][v]
    if k == 'tokenColors':
      for token in theme_dict[k]:
        token_scopes = token['scope'] if isinstance(
          token['scope'], list) else [token['scope']]
        for _k, _v in v.items():
          for ts in token_scopes:
            if ts == _k:
              return token['settings'][_v]



def set_pystaTheme_value(value):
  pass

for d in setup_dict:
  # v = get_vs_value(d['vscode'], vscode_theme_dict)
  vs_value = get_vsTheme_value(d['vscode'], vscode_theme_dict)
  print(d['pysta'])

x = 1

