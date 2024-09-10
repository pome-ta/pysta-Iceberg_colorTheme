from pathlib import Path
import json

import requests

url = 'https://github.com/tokyo-night/tokyo-night-vscode-theme/blob/master/themes/tokyo-night-color-theme.json'


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

json_str = json.dumps(vscode_theme_dict,
                      indent=1,
                      sort_keys=True,
                      ensure_ascii=False)

root_path = Path('./')
target_path = Path('../dists/vscodeThemes')

theme_path = Path(root_path, target_path, file_name)
theme_path.write_text(json_str, encoding='utf-8')

