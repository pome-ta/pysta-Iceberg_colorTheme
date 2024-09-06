'''
VSCode のtheme の要素出現調査
'''

from pathlib import Path
import json


def get_target_path(path: Path) -> Path:
  root_path = Path(__file__).parent
  return Path(root_path, path)


def get_json_to_dict(json_path: Path) -> dict:
  text_data = json_path.read_text()
  try:
    json_data = json.loads(text_data)
  except json.decoder.JSONDecodeError as e:
    regex = re.compile(r'/\*[\s\S]*?\*/|//.*')
    res_comment_json = regex.sub('', text_data)
    json_data = json.loads(res_comment_json)
    print(f'{e}\n\t-> json ファイル内のコメントを除去してデータ作成')
  return json_data
  


if __name__ == '__main__':
  json_dir = './vscodeThemes'
  vs_theme_jdon_path = get_target_path(json_dir)

  for p in vs_theme_jdon_path.iterdir():
    a = get_json_to_dict(p)

