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


url_scheme = 'pythonista3://?action=add-theme&theme-data=eNqtVk2PmzAQve-viNhraYCwCdnbJptDpfZS9VRFQsYMiYuxI9u0Tav-9xrbSYBAdlftEc-H5703Hub33WTipahWey5ShirwJo8TD3PMD5x57xqrIkyZ0_V8nTyH9pCSTCBxTM_G-WoRJEtrzKFANVWpgp_XkSklGJiEtCQsN9ZPH75MPtpDd-O-rjKGCE0zLnIQxivYhEH4YB12tVIg0gzhcid47fKEmyicRdajb5qHSRSeTNeRLXOORJmWcMw4EsaqRA3GUnCmfEl-GY7CwJydKfuAIQOxcxgFHLgkimuGakGNw16pg3zcTrfTHdEAs_eYV9upY3o7_S4xz8EnNo2v9lA5NiQckEA6l2aO2cuiOFrGgTWDENp0pvoeokWySByRKOtDbdNoABWoIvRohQBGuf8ZdjVFoqvzDcLSglC49I5DoOFRLiyO99_kqZnSQy33kKfIVhsF0cwPQj9cfAmjx3j5-LD46mDlDX0pwopwJlOCObs02z3O8xDmjh_NIMjm_Lf-bBTkWCpB2O5yNml6Wtdjop-C5Wy9MMHGYnVVR-oAKKRb1DPWP9bJw3vAZcZ_-jm3ElzSOku7U1wV1rM57OaiSMqR0u7xHCd5OHz5zXu7EbqVOt4X-fzWZfPs_GZdmGAgfIFyUpsKo05W_Sh-cPsmBkpP4qdgPe9Wvgediu38cAwuRCh2zTokRcZp7l2Tp-fLSMLWoHldvubEd4q3Uw4E-kONARKjw2u4TmIU4B49BRcVUmq8U08KXZX8Uq3DMsz-mwwvMzZElp5f5VgJjp9zCc1A83PQLYmaCWCcNKUgzBDspK30xLY_iYsG-qnaf4d_446WlzpaFeOucVDKEMx_plPDQfBvgNXbdFGoK_wQZsb7cJn-OfbgXs22bpvVDJ_yDYRsoqdG_F5lshyYdS0ql1mCo9tyNUO4BF6rbm7nxccgrOLVJomGOzj6bx18ImV8ljhe3jBLakL1Y36BbjeiruZ1RjkudX4k1BhIpMXFi35oVQEbC2ltZa99pBXPazqme7JcJeueNjf_tUMBbj18DT93Lsr0VyqBgqH2sgmsn5_Dzfyy7SiiHLb2QtpbJg565fp-vT-eHrZbfJheas5PzYvjeLXobDz_sNhtp1rtbDutENEe5khup7c3p6GFqA8gQrPwIenuyMMbtOYPhNRsEWRR3BdFEBSFd_fnL7ohL8Y~'

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
local_json_name = 'minimumTemplateDefaultThemeSample.json'
#local_theme_path = Path(str(path_objc), local_json_name)
local_theme_path = Path(ROOT_PATH, './dumps', local_json_name)
local_bytes_json = local_theme_path.read_bytes()
local_str_json = local_theme_path.read_text()


#minimumTemplateDefaultThemeSample
#utf-8

#scheme_compressed = zlib.compress(scheme_bytes_json, level=9)
scheme_compressed = zlib.compress(local_bytes_json, level=9)
#scheme_b64bytes = base64.b64encode(scheme_compressed)
scheme_b64bytes = base64.urlsafe_b64encode(scheme_compressed)
scheme_b64str = scheme_b64bytes.decode('utf-8').replace('=', '~')

print(_b64string == scheme_b64str)

param = 'pythonista3://?action=add-theme&theme-data='


