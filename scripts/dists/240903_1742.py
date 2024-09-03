from pathlib import Path
import json

import requests

src_path = ''

json_path = Path(src_path)
file_name = json_path.name

json_data = json_path.read_text()
json_loads = json.loads(json_data)
json_str = json.dumps(json_loads, indent=1, sort_keys=True, ensure_ascii=False)

root_path = Path('./vscodeThemes')
theme_path = Path(root_path, file_name)
theme_path.write_text(json_str, encoding='utf-8')
'''
url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'

params = {
  'raw': 'true',
}

response = requests.get(url, params)
file_name = Path(url).name

try:
  vscode_theme_dict = response.json()
except requests.exceptions.JSONDecodeError:
  import re
  regex = re.compile(r'/\*[\s\S]*?\*/|//.*')
  res_comment_json = regex.sub('', response.text)
  vscode_theme_dict = json.loads(res_comment_json)

json_str = json.dumps(_theme_dict,
                      indent=1,
                      sort_keys=True,
                      ensure_ascii=False)

root_path = Path('./vscodeThemes')
theme_path = Path(root_path, file_name)
theme_path.write_text(json_str, encoding='utf-8')

'''

