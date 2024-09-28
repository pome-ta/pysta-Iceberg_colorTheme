"""
note: 直接dict に書き込む形式。シンプルに
"""

from pathlib import Path
import json

import requests

# todo: Pythonista3 以外での`Path` 挙動差分用
ROOT_PATH: Path = Path(__file__).parent


class ThemeObject:
  # xxx: この宣言だと無意味か
  json_url: str
  file_name: str | None
  tmp_dir: Path
  data: dict | None
  info: dict | None

  def get_file_name(self, url: str) -> str | None:
    path = Path(url)  # xxx: 取り出し方が乱暴
    if path.suffix == '.json':
      return path.name
    # wip: `None` 時、エラー吐く
    return None

  def get_tmp_dir(self, tmp_dir: Path | str | None) -> Path:
    if tmp_dir is None:
      return Path(ROOT_PATH, './vscodeThemes')
    elif isinstance(tmp_dir, Path):
      return tmp_dir
    else:
      return Path(tmp_dir)

  def get_tmp_data_info(self) -> list[dict]:
    data_text = Path(self.tmp_dir, self.file_name).read_text()
    loads = json.loads(data_text)

    # xxx: key をclass 内に2回書いてる(ちょっと違うけど)
    _url = loads.get('_repository_url')
    _name = loads.get('_author_name')
    _license = loads.get('_license_kind')
    _pushed_at = loads.get('_pushed_at')

    info = self.__create_info(_url, _name, _license, _pushed_at)
    return [
      loads,
      info,
    ]

  def get_data(self) -> dict | None:
    params = {
      'raw': 'true',
    }
    response = requests.get(self.json_url, params)
    if response.status_code == 200:
      # xxx: iceberg には、comment なし
      # wip: comment 削除処理
      return response.json()
    # wip: `None` 時、エラー吐く
    return None

  def get_info(self) -> dict | None:
    tokens = self.__api_tokens()
    if tokens is None:
      # wip: `None` 時、エラー吐く
      return None
    _url = tokens.get('html_url')
    _name = tokens.get('owner').get('login')
    _license = l.get('name') if (l :=
                                 tokens.get('license')) is not None else str(l)
    _pushed_at = tokens.get('pushed_at')

    info = self.__create_info(_url, _name, _license, _pushed_at)
    return info

  def __api_tokens(self) -> dict | None:
    _, _, owner_name, repo_name, *_ = Path(
      self.json_url).parts  # xxx: 取り出し方が乱暴
    api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'

    # wip: 制限かかった時の処理
    response = requests.get(api_url)
    if response.status_code == 200:
      return response.json()
    # wip: `None` 時、エラー吐く
    return None

  def __create_info(self,
                    repository_url: str,
                    author_name: str,
                    license_kind: str,
                    pushed_at: str,
                    file_name: str | None = None) -> dict:
    # xxx: key をclass 内に2回書いてる（ちょっと違うけど）
    info = {
      '_repository_url': repository_url,
      '_author_name': author_name,
      '_license_kind': license_kind,
      '_pushed_at': pushed_at,
      '_file_name': self.file_name if file_name is None else file_name,
      '_file_url': self.json_url,
    }
    return info


class VSCodeThemeObject(ThemeObject):

  def __init__(self,
               theme_json_url: str,
               use_local: bool = False,
               tmp_dir: Path | str | None = None):
    self.json_url = theme_json_url
    self.file_name = self.get_file_name(theme_json_url)
    self.tmp_dir = self.get_tmp_dir(tmp_dir)

    if use_local:
      self.data, self.info = self.get_tmp_data_info()
    else:
      self.data = self.get_data()
      self.info = self.get_info()

    # xxx: `None` の時ここで弾く?


if __name__ == '__main__':
  dark_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  light_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'

  iceberg_dark = VSCodeThemeObject(dark_url)

