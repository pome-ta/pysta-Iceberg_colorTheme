from pathlib import Path
import json
import re
import itertools

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

    value = get_deep_dict(v, {}) if isinstance(v, dict) else v

    parent[k] = value
  return parent


root_theme_path = Path(str(NSBundle.mainBundle().resourcePath()), 'Themes2')

user_theme_path = Path(str(PA2UITheme.sharedTheme().userThemesPath()))

paths_iter = itertools.chain(root_theme_path.iterdir(),
                             user_theme_path.iterdir())

tmp_dict = {}

for p in paths_iter:
  theme_dict = get_json2dict(p)
  _tmp_dict = get_deep_dict(theme_dict, theme_dict)
  tmp_dict |= _tmp_dict

pick = list(root_theme_path.iterdir())[0]
pick = list(user_theme_path.iterdir())[0]

d = get_json2dict(pick)
default_dict = get_deep_dict(d, {})

