'''
VSCode のtheme の要素出現調査
'''

from pathlib import Path
import json


def get_target_path(path: Path) -> Path:
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


def get_all_keys(theme_dict: dict):

  def _for_type_list(_list: list, parent: str):
    for n, v in enumerate(_list):
      if isinstance(v, dict):
        yield from _for_type_dict(v, f'{parent}|::')
      elif isinstance(v, list):
        yield from _for_type_list(v, f'{parent}|::')
      else:
        yield f'{parent}|'

  def _for_type_dict(_dict: dict, parent: str):
    for k, v in _dict.items():
      if isinstance(v, dict):
        yield from _for_type_dict(v, f'{parent + k}::')
      elif isinstance(v, list):
        yield from _for_type_list(v, f'{parent + k}::')
      else:
        yield f'{parent + k}'

  if isinstance(theme_dict, dict):
    yield from _for_type_dict(theme_dict, '')


def merge_keys_list(theme_path: Path) -> list:
  pass


if __name__ == '__main__':
  json_dir = './vscodeThemes'
  vs_theme_jdon_path = get_target_path(json_dir)

  dmy_theme_path = list(vs_theme_jdon_path.iterdir())[2]
  dmy_theme_name = dmy_theme_path.name
  dmy_theme_dict = get_json_path_to_dict(dmy_theme_path)
  theme_keys_list = sorted(list(set(get_all_keys(dmy_theme_dict))))

