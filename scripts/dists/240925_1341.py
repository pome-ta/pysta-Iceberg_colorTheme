"""
note: 直接dict に書き込む形式。シンプルに
"""

from pathlib import Path
import re

# todo: Pythonista3 以外での`Path` 挙動差分用
ROOT_PATH: Path = Path(__file__).parent


class ThemeObject:

  def get_file_name(self, url: str) -> str | None:
    if re.match(r'.*\.json',)


class VSCodeThemeObject:

  def __init__(self,
               theme_json_url: str,
               use_local: bool = False,
               local_dir: Path | str | None = None):
    self.json_url = theme_json_url
    '''
    self.file_name: str | None = file_name if (
      file_name := Path(theme_json_url).name) else None
    self.data: dict | None = None
    self.info: dict | None = None
    self.local_dir: Path | None = None
    '''
    self.file_name = name if re.match(r'.*\.json',
                                      (name := Path(theme_json_url).name),
                                      re.IGNORECASE) else None


if __name__ == '__main__':
  dark_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  light_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'

  iceberg_dark = VSCodeThemeObject(dark_url)

