import requests
#import json

url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
url = 'https://github.com/pome-ta/pysta-Iceberg_colorTheme/blob/main/Default%20Theme%20Commented.ja.json'
params = {
  'raw': 'true',
}

response = requests.get(url, params)
r_json = response.json()

