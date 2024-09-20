"""
note: GitHub 取り込みと、dump 取り込み双方での設計
  - 制限考えるのはAPI 使う時のみか
"""

from pathlib import Path

import requests


class ThemeInterpretation:

  def __init__(self):
    pass


class ThemeData:

  def __init__(self, github_url: str, use_local: bool = False):

    self.use_local = use_local
    self.__name: str
    self.__data: dict
    self.__info: dict
    self.info_attribute_keys = [
      '___html_url',
      '___author',
      '___license',
      '___pushed_at',
    ]

    if self.use_local:
      pass
    else:
      tokens = self.__api_tokens(github_url)

      _html_url = tokens.get('html_url')
      _author = tokens.get('owner').get('login')
      _license = l.get('name') if (
        l := tokens.get('license')) is not None else str(l)
      _pushed_at = tokens.get('pushed_at')

      info = {
        '___html_url': _html_url,
        '___author': _author,
        '___license': _license,
        '___pushed_at': _pushed_
      }

  class DictDotNotation(dict):

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.__dict__ = self

  @property
  def name(self) -> str:
    return self.__name

  @name.setter
  def name(self, name: str):
    pass
    

  @property
  def data(self) -> dict:
    return self.__data

  @data.setter
  def data(self, data: dict):
    pass

  @property
  def info(self) -> dict:
    return self.__info

  @info.setter
  def info(self, info: dict):
    pass
    
  def setup_info(self):
    pass

  def __api_tokens(self, github_url: str) -> dict:
    _, _, owner_name, repo_name, *_ = Path(github_url).parts

    api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'
    # wip: 制限かかった時の処理
    response = requests.get(api_url)
    return response.json()


if __name__ == '__main__':
  #target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'

