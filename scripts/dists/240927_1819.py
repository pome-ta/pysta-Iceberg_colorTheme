"""
note: 直接dict に書き込む形式。シンプルに
"""

from pathlib import Path
import re

# todo: Pythonista3 以外での`Path` 挙動差分用
ROOT_PATH: Path = Path(__file__).parent


class ThemeObject:

  def get_file_name(self, url: str) -> str | None:
    path = Path(url)  # xxx: 取り出し方が乱暴
    if path.suffix == '.json':
      return path.name

  def get_tmp_dir(self, tmp_dir: Path | str | None) -> Path:
    if tmp_dir is None:
      return Path(ROOT_PATH, './vscodeThemes')
    elif isinstance(tmp_dir, Path):
      return tmp_dir
    else:
      return Path(tmp_dir)


class VSCodeThemeObject(ThemeObject):

  def __init__(self,
               theme_json_url: str,
               use_local: bool = False,
               tmp_dir: Path | str | None = None):
    self.json_url = theme_json_url
    self.file_name = self.get_file_name(theme_json_url)
    self.tmp_dir = self.get_tmp_dir(tmp_dir)

    self.data: dict | None = None
    self.info: dict | None = None


if __name__ == '__main__':
  dark_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  light_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'

  iceberg_dark = VSCodeThemeObject(dark_url)

