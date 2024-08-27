from pathlib import Path
import json
import re

from objc_util import ObjCClass
import pdbg

NSBundle = ObjCClass('NSBundle')
PA2UITheme = ObjCClass('PA2UITheme')

regex = re.compile(r'^.*?___comment$')


def get_json2dict(path: Path) -> dict:
  with open(path, mode='r', encoding='utf-8') as f:
    return json.load(f)


def get_deep_dict(target: dict, parent: dict = {}) -> dict:
  for k, v in target.items():
    if regex.match(k):
      continue
    '''
    if isinstance(v, dict):
      v = get_deep_dict(v, {})
      #v_dict = get_deep_dict(v, {})
      #v = v_dict
      #print(k, v_dict)
      #print(v)
      #parent[k] = get_deep_dict(v, k)
      #v = get_deep_dict(v, k)
      #print(get_deep_dict(v, target))
      #i = get_deep_dict(v, target)
      #continue
    '''

    value = get_deep_dict(v, {}) if isinstance(v, dict) else v

    parent[k] = value
  return parent


def merge_dict():
  pass


root_theme_path = Path(str(NSBundle.mainBundle().resourcePath()), 'Themes2')

user_theme_path = Path(str(PA2UITheme.sharedTheme().userThemesPath()))

pick = list(root_theme_path.iterdir())[0]
pick = list(user_theme_path.iterdir())[0]

d = get_json2dict(pick)
#dl = d.keys()

#default_dict = {}
'''
for k, v in d.items():
  #print(type(v))
  print(k, type(k))
'''

default_dict = get_deep_dict(d, {})

