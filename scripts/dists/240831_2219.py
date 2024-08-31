from pathlib import Path
import json
from collections import namedtuple
from types import SimpleNamespace


class DictDotNotation(dict):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__dict__ = self


# class DictDotNotation(dict):
#   def __getattr__(self, key):
#     return self.__getitem__(key)

#   def __setattr__(self, key, value):
#     self.__setitem__(key, value)

#   def __delattr__(self, key):
#     self.__delitem__(key)

vscode_theme_path = Path(
  Path(__file__).parent, './vscodeThemes/iceberg.color-theme.json')
vscode_theme_dict = json.loads(vscode_theme_path.read_text())

theme = DictDotNotation(vscode_theme_dict)
# print(theme.colors['list.hoverBackground'])
# ns = SimpleNamespace(**vscode_theme_dict)

x = 1

