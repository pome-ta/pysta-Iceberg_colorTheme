"""
note: GitHub 取り込みと、dump 取り込み双方での設計
  - 制限考えるのはAPI 使う時のみか
"""

from pathlib import Path
import json

import requests


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
    self.url_path: Path = Path(github_url)
    self.name: str = self.url_path.name
    self.data: dict | None = self.__get_json_data()
    self.info: dict | None = self.__get_info_attribute()
    # xxx: `None` の時ここで弾く？
  
  def to_dump(self) -> str:
    data = self.data if self.info is None else self.data | self.info
    kwargs = {
      'indent': 1,
      'sort_keys': True,
      'ensure_ascii': False,
    }
    return json.dumps(data, **kwargs)
  
  def export(self, vs_themes: Path):
    if not vs_themes.is_dir():
      vs_themes.mkdir(parents=True)
    
    theme_json = self.to_dump()
    json_file = Path(vs_themes, self.name)
    json_file.write_text(theme_json, encoding='utf-8')
  
  class DictDotNotation(dict):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.__dict__ = self
  
  def __get_json_data(self) -> dict | None:
    params = {
      'raw': 'true',
    }
    response = requests.get(str(self.url_path), params)
    if response.status_code == 200:
      # xxx: iceberg には、comment ない
      # wip: comment 削除処理
      return response.json()
  
  def __api_tokens(self) -> dict | None:
    _, _, owner_name, repo_name, *_ = self.url_path.parts
    api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'
    
    # wip: 制限かかった時の処理
    response = requests.get(api_url)
    if response.status_code == 200:
      return response.json()
  
  def __get_info_attribute(self) -> DictDotNotation | None:
    tokens = self.__api_tokens()
    if tokens is None:
      return
    _html_url = tokens.get('html_url')
    _author = tokens.get('owner').get('login')
    _license = l.get('name') if (l := tokens.get('license')) is not None else str(l)
    _pushed_at = tokens.get('pushed_at')
    
    # xxx: `_` は3つ
    info = {
      '___html_url': _html_url,
      '___author': _author,
      '___license': _license,
      '___pushed_at': _pushed_at,
    }
    return self.DictDotNotation(info)


class ThemeInterpretation:
  """
  VSCode のTheme 情報を指定して取得
  """
  
  def __init__(self, target: dict):
    self.target = target
  
  def __for_colors(self, key: str) -> str | bool | int | float | None:
    # xxx: `get` じゃなくて`[key]` の方がいいか?
    return self.target['colors'].get(key)
  
  def __for_token_colors(self, keys: list[str]) -> str | bool | int | float | None:
    scope, settings = keys
    for tokenColor in self.target.get('tokenColors'):
      _scope = tokenColor.get('scope')
      # xxx: 配列格納に合わせる
      scopes = _scope if isinstance(_scope, list) else [_scope]
      if scope in scopes:
        return tokenColor.get('settings').get(settings)
  
  def get_value(self, search_value: str = '', colors: str | None = None,
                tokenColors: list[str] | None = None) -> str | bool | int | float | None:
    value = None
    
    if search_value:
      value = self.target.get(search_value)
    elif colors is not None and isinstance(colors, str):
      value = self.__for_colors(colors)
    elif tokenColors is not None and isinstance(tokenColors, list):
      value = self.__for_token_colors(tokenColors)
    
    if value is None:
      # xxx: `raise` を正しく使いたい
      raise print(
        f'{self}: value の値が`{value}` です:\n- {search_value=}\n- {colors=}\n- {tokenColors=}'
      )
    return value


if __name__ == '__main__':
  target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  # target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'
  
  theme_object = ThemeObject(target_url)
  # aa = to.to_dump()
  # to.export(Path('./vscodeThemes'))
