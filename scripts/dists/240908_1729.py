"""
note: Base64 変換でURL スキーム可能か調査
"""

from pathlib import Path
import json


def get_target_path(path: Path | str) -> Path:
  root_path = Path(__file__).parent
  return Path(root_path, path)


def get_json_path_to_dict(json_path: Path) -> dict:
  text_data = json_path.read_text()
  try:
    json_data = json.loads(text_data)
  except json.decoder.JSONDecodeError as e:
    import re
    regex = re.compile(r'/\*[\s\S]*?\*/|//.*')
    res_comment_json = regex.sub('', text_data)
    json_data = json.loads(res_comment_json)
    print(f'{e}\n\t-> json ファイル内のコメントを除去してデータ作成')
  return json_data


if __name__ == '__main__':
  json_dir = './dumps'
  dumps_dir_path = get_target_path(json_dir)
  
  dump_path= list(dumps_dir_path.iterdir())[17]
  theme_dict = get_json_path_to_dict(dump_path)
  
  x = 1
