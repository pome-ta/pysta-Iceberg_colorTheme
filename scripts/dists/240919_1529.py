"""
note: GitHub 取り込みの処理
とりま、力技でやってる
  - vs のdump
  - url 経由ではなく、内部dump から
"""

from pathlib import Path
import json
from urllib.parse import urlparse
from dataclasses import dataclass

import requests


def get_vs_theme_data(json_url: str) -> list:
  params = {
    'raw': 'true',
  }
  response = requests.get(json_url, params)
  file_name = Path(json_url).name

  try:
    vscode_theme_dict = response.json()
  except requests.exceptions.JSONDecodeError:
    import re
    regex = re.compile(r'/\*[\s\S]*?\*/|//.*')
    res_comment_json = regex.sub('', response.text)
    vscode_theme_dict = json.loads(res_comment_json)

  return [file_name, vscode_theme_dict]


def get_repository_tokens(github_url: str) -> dict:
  _, _, owner_name, repo_name, *_ = Path(github_url).parts
  api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'
  # wip: 制限かかった時の処理
  res = requests.get(api_url)
  return res.json()


# ref: [Pythonの辞書型(dict)でドットアクセス(dot notation)するメモ](https://zenn.dev/kazuhito/articles/dbe6bbf8ce3ef2)
class DictDotNotation(dict):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__dict__ = self


def get_repo_author_license_pushed_at(github_url: str) -> DictDotNotation:
  tokens = get_repository_tokens(github_url)

  _html_url = tokens.get('html_url')
  _author = tokens.get('owner').get('login')
  _license = l.get('name') if (l :=
                               tokens.get('license')) is not None else str(l)
  _pushed_at = tokens.get('pushed_at')

  return DictDotNotation({
    '___html_url': _html_url,
    '___author': _author,
    '___license': _license,
    '___pushed_at': _pushed_at,
  })


if __name__ == '__main__':
  #target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'

  iceberg_name, iceberg_data = get_vs_theme_data(target_url)
  iceberg_info = get_repo_author_license_pushed_at(target_url)

  iceberg_data.update(iceberg_info)
  json_str = json.dumps(iceberg_data,
                        indent=1,
                        sort_keys=True,
                        ensure_ascii=False)

  target_path = Path('./vscodeThemes')
  theme_path = Path(target_path, iceberg_name)
  theme_path.write_text(json_str, encoding='utf-8')

