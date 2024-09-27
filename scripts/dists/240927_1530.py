"""
note: [Copy Theme(URL)] の検証
  - 吐き出しを関数化
"""

import base64
import zlib
from pathlib import Path

from objc_util import ObjCClass


# Pythonista3 内部の`userThemesPath`
def get_user_themes_path() -> str:
  _objc_path = ObjCClass('PA2UITheme').sharedTheme().userThemesPath()
  return str(_objc_path)


def create_url_scheme(target_json_path: Path) -> str:
  if target_json_path.suffix != '.json':
    # wip: とりあえず
    #raise Exception('あ')
    raise print('あ')
  bytes_json = target_json_path.read_bytes()
  compressed = zlib.compress(bytes_json, level=9)
  b64bytes = base64.urlsafe_b64encode(compressed)
  param_body = b64bytes.decode('utf-8').replace('=', '~')

  scheme_header = 'pythonista3://?action=add-theme&theme-data='
  return f'{scheme_header}{param_body}'


ROOT_PATH = Path(__file__).parent
path_objc = get_user_themes_path()

local_json_name = 'iceberg.color-theme.json'
#local_json_name = 'minimumTemplateDefaultThemeSample.json'
local_theme_path = Path(str(path_objc), local_json_name)

url_scheme = create_url_scheme(local_theme_path)

