from pathlib import Path
import requests
#import json

root_path = Path('./vscodeThemes')


url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
#url = 'https://github.com/pome-ta/pysta-Iceberg_colorTheme/blob/main/Default%20Theme%20Commented.ja.json'
params = {
  'raw': 'true',
}

response = requests.get(url, params)
r_json = response.json()
#b_json = response.content
file_name = Path(url).name



theme_path = Path(root_path, file_name)
theme_path.write_bytes(response.content)

