"""
note: GitHub 取り込みと、dump 取り込み双方での設計
  - 制限考えるのはAPI 使う時のみか
"""

from pathlib import Path
import json

import requests


class ThemeInterpretation:

  def __init__(self):
    pass


class ThemeObject:
  """
  repository の情報をまるっと持つ
  API 取得と、直のraw 取得の2種類
  dump してローカルに保存
  ダンダーでの変数を外側で使うイメージ
  
  # 今後
  API の制限回避としてローカルdump から持ってくるパターンも考えたい
  """

  def __init__(self, github_url: str):
    self._name: str
    self._data: dict | None
    self._info: dict | None

    self.__setup_repository_attributes(github_url)

  def __setup_repository_attributes(self, url: str):
    self.name = url
    self.data = url
    self.info = url

    # xxx: `None` の時ここで弾く？

  def to_dump(self) -> str:
    data = self.data if self.info is None else self.data | self.info

    kwargs = {
      'indent': 1,
      'sort_keys': True,
      'ensure_ascii': False,
    }
    dump_json = json.dumps(data, **kwargs)
    return dump_json

  def export(self, vs_themes: Path):
    if not vs_themes.is_dir():
      vs_themes.mkdir(parents=True)
      
    theme_json = self.to_dump()
    json_file = Path(vs_themes, self.name)
    json_file.write_text(theme_json, encoding='utf-8')

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, url: str):
    self._name = Path(url).name

  @property
  def data(self) -> dict | None:
    return self._data

  @data.setter
  def data(self, url: str):
    self._data = self.__get_json_data(url)

  @property
  def info(self) -> dict | None:
    return self._info

  @info.setter
  def info(self, url: str):
    self._info = self.__get_info_attribute(url)

  class DictDotNotation(dict):

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.__dict__ = self

  def __get_json_data(self, url: str) -> dict | None:
    params = {
      'raw': 'true',
    }
    response = requests.get(url, params)
    if response.status_code == 200:
      # xxx: iceberg には、comment ない
      # wip: comment 削除処理
      return response.json()

  def __get_info_attribute(self, url: str) -> DictDotNotation | None:
    tokens = self.__api_tokens(url)
    if tokens is None:
      return
    _html_url = tokens.get('html_url')
    _author = tokens.get('owner').get('login')
    _license = l.get('name') if (l :=
                                 tokens.get('license')) is not None else str(l)
    _pushed_at = tokens.get('pushed_at')

    # xxx: `_` は3つ
    info = {
      '___html_url': _html_url,
      '___author': _author,
      '___license': _license,
      '___pushed_at': _pushed_at,
    }

    return self.DictDotNotation(info)

  def __api_tokens(self, url: str) -> dict | None:
    _, _, owner_name, repo_name, *_ = Path(url).parts

    api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'
    # wip: 制限かかった時の処理
    response = requests.get(api_url)
    if response.status_code == 200:
      return response.json()


if __name__ == '__main__':
  #target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'

  to = ThemeObject(target_url)
  #aa = to.to_dump()
  to.export(Path('./testThemes'))

