"""
note: GitHub のパラメータ周り調査
raw は取れてるから、他の情報
  - リポジトリ名
  - 作者
  - license
"""

from urllib.parse import urlparse
import requests
import json

params = {
  'licenses': 'true',
}


def get_repo_author_license(full_url: str) -> dict:
  _scheme, _netloc, path, *_ = urlparse(url)
  [owner_name, repo_name, *_] = [p for p in path.split('/') if p]
  api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'
  res = requests.get(api_url)
  res_dict = res.json()
  #html_url = res_dict['html_url']
  #author = res_dict['owner']['login']
  #license = res_dict['license']['name']
  #return [html_url, author, license]
  return {
    'html_url': res_dict['html_url'],
    'author': res_dict['owner']['login'],
    'license': res_dict['license']['name'],
  }


if __name__ == '__main__':
  from pprint import pprint
  #url = 'https://github.com/pome-ta/pystaColorThemeDev/blob/main/scripts/dists/dumps/myOceanic.json'
  #url = 'https://github.com/pome-ta/pystaColorThemeDev/'

  url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'

  a = get_repo_author_license(url)

