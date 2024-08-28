from pathlib import Path
import json

from objc_util import ObjCClass

NSBundle = ObjCClass('NSBundle')

def get_json2dict(path: Path) -> dict:
  with open(path, mode='r', encoding='utf-8') as f:
    return json.load(f)

def to_dumps(dict_data: dict) -> str:
  return json.dumps(dict_data, indent=1, sort_keys=True, ensure_ascii=False)

def print_len(d: dict, name: str, deep: int = 0) -> None:
  indent = '  '
  print(f'{indent * deep}- {name}: {len(d)}')
  deep += 1
  for k, v in d.items():
    if not isinstance(v, dict):
      print(f'{indent * deep}- {k}:')
      continue
    print_len(v, k, deep)


root_themes_path = Path(str(NSBundle.mainBundle().resourcePath()), 'Themes2')

light_path = Path(root_themes_path, 'Default.json')
dark_path = Path(root_themes_path, 'PythonistaDark.json')

if __name__ == '__main__':
  for p in [light_path, dark_path]:
    theme_dict = get_json2dict(p)
    print_len(json.loads(to_dumps(theme_dict)), p.stem)
    print('')
