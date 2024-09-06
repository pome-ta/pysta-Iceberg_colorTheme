'''
VSCode のtheme の要素出現調査
'''

from pathlib import Path
import json


def get_target_path(path: Path) -> Path:
  root_path = Path(__file__).parent
  return Path(root_path, path)


if __name__ == '__main__':
  json_dir = './vscodeThemes'
  vs_theme_jdon_path = get_target_path(json_dir)
  print(vs_theme_jdon_path.exists())

