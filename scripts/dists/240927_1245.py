"""
note: [Copy Theme(URL)] の検証
  - 逆の流れ
"""

import base64
import urllib.parse
import zlib

from pathlib import Path
#import difflib

from objc_util import ObjCClass


def str_json_to_url_scheme(theme_str_json: str) -> str:
  param = 'pythonista3://?action=add-theme&theme-data='


url_scheme = 'pythonista3://?action=add-theme&theme-data=eNqtVU1v2zAMvedXBN61BtrutvPQ2y5r7wYt0Y5mSQxkCmtW9L9Plu1lij8SF80tpN_jI8WPt91-nzGURQmiqR15K7P9t3329HQfftnd6GbFGicerSwW1psS3cTXCjpi25nfwt9gkCRadsrWZ1uwCtI0AUdPRZbzlk9DXMWglcii973_KBMHFE1Jr7kkiynt4OmM7Dz-Yx2_7Iwpl4a2XZD2paqittngq3FTBMlU5bno-TTY3VmHs-hyB1L5qPAxYW3w9JucXK9qgjhgoLJ1_pBgLupdkpbZtEISq4-935Svs-TDs14Rks-9fkXOAPNyR80-25j8123JR8smxPXM5pIKI9UkGMZXziWGJgBWZCMwNAy6bvhS7NHRLxS8TSZDfTWepctQ56G_secqb8XIdyOEoW1mJnt5UOakdyunQfI83wWP24o1ZvGZU-CVDj38gfp066TUJJrAD4437S4yBi1_3iY2JL3GDeJvOQUJIJQcvOZbELsBFfarWztsMa8KjNKn6PuBVlP-E2uvwf33Sav-xNQe7vt7qPrKJVwrYQblRdeeE2ftmTGoDBt87ojiEUIzkyvitE_vb-nAnVaP9yFMqgWll0KMApYpLJg-tFFWGW9e0Bw1MH7v83o5oMFnCDYcQoY8ixY1xoYuLsu1e_8LEW0lgg~~'

# theme-dataを取得
parse_result = urllib.parse.urlparse(url_scheme)
query_params = urllib.parse.parse_qs(parse_result.query)
_b64string = query_params['theme-data'][0]

# 文字を置換してBase64デコード

# wip: [#base64.urlsafe_b64decode](https://docs.python.org/ja/3/library/base64.html#base64.urlsafe_b64decode)
b64string = _b64string.replace('-', '+').replace('_', '/').replace('~', '=')
compressed_data = base64.b64decode(b64string)

# zlibで展開
#decompressed_data = zlib.decompress(compressed_data)
scheme_bytes_json = zlib.decompress(compressed_data)
scheme_str_json = scheme_bytes_json.decode()


ROOT_PATH =Path(__file__).parent
path_objc = ObjCClass('PA2UITheme').sharedTheme().userThemesPath()

local_json_name = 'iceberg.color-theme.json'
#local_json_name = 'minimumTemplateDefaultThemeSample.json'
local_theme_path = Path(str(path_objc), local_json_name)
#local_theme_path = Path(ROOT_PATH, './dumps', local_json_name)
local_bytes_json = local_theme_path.read_bytes()
local_str_json = local_theme_path.read_text()


#minimumTemplateDefaultThemeSample
#utf-8

#scheme_compressed = zlib.compress(scheme_bytes_json, level=9)
scheme_compressed = zlib.compress(local_bytes_json, level=9)
#scheme_b64bytes = base64.b64encode(scheme_compressed)
scheme_b64bytes = base64.urlsafe_b64encode(scheme_compressed)
scheme_b64str = scheme_b64bytes.decode('utf-8').replace('=', '~')



param = 'pythonista3://?action=add-theme&theme-data='
print(f'{param}{scheme_b64str}')


