from pathlib import Path
import json

from tmpDict import tmp_theme_dict

vscode_theme_path = Path(
  Path(__file__).parent, './vscodeThemes/iceberg.color-theme.json')
vscode_theme_dict = json.loads(vscode_theme_path.read_text())



def call_dict_value(key:str, dic:dict)->str:
  pass



convert_items = [
  ['name', ['name']],
  ['background', ['colors', 'editor.background']]
]


for item in convert_items:
  py_key, vs_keys = item
  value = call_dict_value()
  print(vs_keys)






x = 1