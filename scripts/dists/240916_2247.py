"""
note: GitHub のパラメータ周り調査
raw は取れてるから、他の情報
  - リポジトリ名
  - 作者
"""

from urllib.parse import urlparse
import requests
import json

params = {
  'licenses': 'true',
}

if __name__ == '__main__':
  from pprint import pprint
  url = 'https://github.com/pome-ta/pystaColorThemeDev/blob/main/scripts/dists/dumps/myOceanic.json'
  #url = 'https://github.com/pome-ta/pystaColorThemeDev/'

  _scheme, _netloc, path, *_ = urlparse(url)
  #ur = urlparse(url)

  [owner_name, repo_name, *_] = [p for p in path.split('/') if p]
  
  api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'
  
  aaa = requests.get(api_url)
  
  j = aaa.json()
  #author

  #api_url = 'https://api.github.com/'
  '''
  api_params = {
  'owner':owner_name,
  'repo': repo_name,
  'license': True
  }

  response = requests.get(api_url, api_params)
  dump = json.loads(response.text)
  hd = response.headers
  pprint(hd)
  '''

  #response = requests.get(url, params)
  #pprint(response.headers)

