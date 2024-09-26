"""
note: [Copy Theme(URL)] の検証
"""

import base64
import urllib.parse
import zlib


def url_scheme_to_str_json(full_url_scheme: str) -> str:
  # theme-dataを取得
  parse_result = urllib.parse.urlparse(url_scheme)
  query_params = urllib.parse.parse_qs(parse_result.query)
  _b64string = query_params['theme-data'][0]

  # 文字を置換してBase64デコード
  b64string = _b64string.replace('-', '+').replace('_', '/').replace('~', '=')
  #b64string = b64string.replace("_", "/")
  #b64string = b64string.replace("~", "=")
  compressed_data = base64.b64decode(b64string)

  # zlibで展開
  decompressed_data = zlib.decompress(compressed_data)
  decoded = decompressed_data.decode()
  return decoded


def str_json_to_url_scheme(theme_str_json: str) -> str:
  param = 'pythonista3://?action=add-theme&theme-data='


url_scheme = 'pythonista3://?action=add-theme&theme-data=eNqtVk2PmzAQve-viNhraYCwCdnbJptDpfZS9VRFQsYMiYuxI9u0Tav-9xrbSYBAdlftEc-H5703Hub33WTipahWey5ShirwJo8TD3PMD5x57xqrIkyZ0_V8nTyH9pCSTCBxTM_G-WoRJEtrzKFANVWpgp_XkSklGJiEtCQsN9ZPH75MPtpDd-O-rjKGCE0zLnIQxivYhEH4YB12tVIg0gzhcid47fKEmyicRdajb5qHSRSeTNeRLXOORJmWcMw4EsaqRA3GUnCmfEl-GY7CwJydKfuAIQOxcxgFHLgkimuGakGNw16pg3zcTrfTHdEAs_eYV9upY3o7_S4xz8EnNo2v9lA5NiQckEA6l2aO2cuiOFrGgTWDENp0pvoeokWySByRKOtDbdNoABWoIvRohQBGuf8ZdjVFoqvzDcLSglC49I5DoOFRLiyO99_kqZnSQy33kKfIVhsF0cwPQj9cfAmjx3j5-LD46mDlDX0pwopwJlOCObs02z3O8xDmjh_NIMjm_Lf-bBTkWCpB2O5yNml6Wtdjop-C5Wy9MMHGYnVVR-oAKKRb1DPWP9bJw3vAZcZ_-jm3ElzSOku7U1wV1rM57OaiSMqR0u7xHCd5OHz5zXu7EbqVOt4X-fzWZfPs_GZdmGAgfIFyUpsKo05W_Sh-cPsmBkpP4qdgPe9Wvgediu38cAwuRCh2zTokRcZp7l2Tp-fLSMLWoHldvubEd4q3Uw4E-kONARKjw2u4TmIU4B49BRcVUmq8U08KXZX8Uq3DMsz-mwwvMzZElp5f5VgJjp9zCc1A83PQLYmaCWCcNKUgzBDspK30xLY_iYsG-qnaf4d_446WlzpaFeOucVDKEMx_plPDQfBvgNXbdFGoK_wQZsb7cJn-OfbgXs22bpvVDJ_yDYRsoqdG_F5lshyYdS0ql1mCo9tyNUO4BF6rbm7nxccgrOLVJomGOzj6bx18ImV8ljhe3jBLakL1Y36BbjeiruZ1RjkudX4k1BhIpMXFi35oVQEbC2ltZa99pBXPazqme7JcJeueNjf_tUMBbj18DT93Lsr0VyqBgqH2sgmsn5_Dzfyy7SiiHLb2QtpbJg565fp-vT-eHrZbfJheas5PzYvjeLXobDz_sNhtp1rtbDutENEe5khup7c3p6GFqA8gQrPwIenuyMMbtOYPhNRsEWRR3BdFEBSFd_fnL7ohL8Y~'

str_json = url_scheme_to_str_json(url_scheme)

