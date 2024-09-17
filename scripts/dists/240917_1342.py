"""
note: GitHub のパラメータ周り調査
raw は取れてるから、他の情報
  - リポジトリ名
  - 作者
  - license
"""

from urllib.parse import urlparse
import requests

params = {
  'licenses': 'true',
}


def get_repository_tokens(github_url: str) -> dict:
  _scheme, _netloc, path, *_ = urlparse(github_url)
  [owner_name, repo_name, *_] = [p for p in path.split('/') if p]
  api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'
  # wip: 制限かかった時の処理
  res = requests.get(api_url)
  return res.json()


def get_repo_author_license_pushed_at(github_url: str) -> dict:
  tokens = get_repository_tokens(github_url)
  '''
  return {
    'html_url':
    tokens['html_url'],
    'author':
    tokens['owner']['login'],
    'license':
    tokens['license']
    if tokens['license'] is None else tokens['license']['name'],
    'pushed_at':
    tokens['pushed_at'],
  }
  '''
  _html_url = tokens.get('html_url')
  _author = tokens.get('owner').get('login')
  # _license = tokens.get('license').get('name') if tokens.get('license') is not None else str(tokens.get('license'))
  _license = l.get('name') if (l := tokens.get('license')) is not None else str(l)
  
  _pushed_at = tokens.get('pushed_at')
  
  return {
    'html_url': _html_url,
    'author': _author,
    'license': _license,
    'pushed_at': _pushed_at,
  }


if __name__ == '__main__':
  # url = 'https://github.com/pome-ta/pystaColorThemeDev/blob/main/scripts/dists/dumps/myOceanic.json'
  # url = 'https://github.com/pome-ta/pystaColorThemeDev/'
  
  url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  # url = 'https://github.com/pome-ta/bnnGenArtPE'
  
  api_info = get_repo_author_license_pushed_at(url)
  # api_info = get_repository_tokens(url)
  print(api_info)
  x = 1

