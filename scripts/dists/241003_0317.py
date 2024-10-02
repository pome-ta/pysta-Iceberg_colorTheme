"""
note: とりあえず分割せずに全部ここに
  - 後々分割か?
  - エラーハンドリング
  - comment つける
  - エラー処理
  - markdown のmodule 関係使えるかな？
    - jinja2 でもいいかも
"""

from pathlib import Path
import json
import base64
import zlib

import requests
# ref: [Pythonのrequestsライブラリで学ぶHTTPエラー処理の基本 - 社内SE 〜しゃちくによる社内IT化計画〜](https://shanai-se.blog/python/library-requests-error/)
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout

# todo: Pythonista3 以外での`Path` 挙動クッション用
ROOT_PATH: Path = Path(__file__).parent

#VS_LOCAL = Path(ROOT_PATH, './VSCodeThemeDump')
#PY_LOCAL = Path(ROOT_PATH, './Pythonista3ThemeDump')
VS_LOCAL = Path(ROOT_PATH, './vscodeThemes')
PY_LOCAL = Path(ROOT_PATH, './testThemes')


class VSCodeThemeServer:
  file_name: str
  tmp_dir: Path
  data: dict
  info: dict
  dump: str
  info_keys: list[str] = [
    '_repository_url',
    '_author_name',
    '_license_kind',
    '_pushed_at',
    '_file_name',
    '_file_url',
  ]

  def __init__(self,
               theme_json_url: str,
               use_local: bool = False,
               tmp_dir: Path = VS_LOCAL):

    self.__json_url = theme_json_url
    self.file_name = self.__get_file_name(theme_json_url)
    self.tmp_dir = tmp_dir

    if use_local:
      self.data, self.info = self.__get_tmp_data_info()
    else:
      self.data = self.__get_data()
      self.info = self.__get_info()

    self.dump = to_dump(self.data, self.info)

  def get_value(
      self,
      top_name: str = '',
      colors: str | None = None,
      tokenColors: list[str] | None = None) -> str | bool | int | float | None:
    value = None

    if top_name:
      value = self.data.get(top_name)
    elif colors is not None and isinstance(colors, str):
      value = self.__for_colors(colors)
    elif tokenColors is not None and isinstance(tokenColors, list):
      value = self.__for_token_colors(tokenColors)

    if value is None:
      raise ValueError(
        f'value の値が`{value}` です:\n- {top_name=}\n- {colors=}\n- {tokenColors=}'
      )
    return value

  def __for_colors(self, key: str) -> str | bool | int | float | None:
    return self.data['colors'].get(key)

  def __for_token_colors(self,
                         keys: list[str]) -> str | bool | int | float | None:
    scope, settings = keys
    for tokenColor in self.data.get('tokenColors'):
      _scope = tokenColor.get('scope')
      # xxx: 配列格納に合わせる
      scopes = _scope if isinstance(_scope, list) else [_scope]
      if scope in scopes:
        return tokenColor.get('settings').get(settings)

  @staticmethod
  def __get_file_name(url: str) -> str:
    path = Path(url)  # xxx: 取り出し方が乱暴
    if path.suffix == '.json':
      return path.name
    else:
      raise ValueError(f'`.json` 形式のファイルではありません\n\turl:{url}')

  def __get_tmp_data_info(self) -> list[dict]:
    data_text = Path(self.tmp_dir, self.file_name).read_text()
    loads = json.loads(data_text)

    info = self.__create_info(*[loads.get(key) for key in self.info_keys])

    return [
      loads,
      info,
    ]

  def __get_data(self) -> dict | None:
    params = {
      'raw': 'true',
    }

    try:
      response = requests.get(self.__json_url, params=params)
      response.raise_for_status()
    except ConnectionError as e:
      print(f'Connection Error:{e}')
      raise
    except HTTPError as e:
      print(f'HTTP Error:{e}')
      raise
    except Timeout as e:
      print(f'Timeout Error:{e}')
      raise
    except RequestException as e:
      print(f'Error:{e}')
      raise
    # xxx: iceberg には、comment なし
    # wip: `.jsonc` (JSON with Comments) 対応
    return response.json()

  def __get_info(self) -> dict | None:
    tokens = self.__api_tokens()

    _url = tokens.get('html_url')
    _name = tokens.get('owner').get('login')
    _license = l.get('name') if (l :=
                                 tokens.get('license')) is not None else str(l)
    _pushed_at = tokens.get('pushed_at')

    # xxx: `None` は許容？
    pre_info = [
      _url,
      _name,
      _license,
      _pushed_at,
    ]

    info = self.__create_info(*pre_info)
    return info

  def __api_tokens(self) -> dict:
    _, _, owner_name, repo_name, *_ = Path(
      self.__json_url).parts  # xxx: 取り出し方が乱暴
    api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'

    try:
      response = requests.get(api_url)
      response.raise_for_status()
    except ConnectionError as e:
      print(f'Connection Error:{e}')
      raise
    except HTTPError as e:
      print(f'HTTP Error:{e}')
      raise
    except Timeout as e:
      print(f'Timeout Error:{e}')
      raise
    except RequestException as e:
      print(f'Error:{e}')
      raise

    return response.json()

  def __create_info(self,
                    repository_url: str,
                    author_name: str,
                    license_kind: str,
                    pushed_at: str,
                    file_name: str | None = None,
                    file_url: str | None = None) -> dict:
    values = [
      repository_url,
      author_name,
      license_kind,
      pushed_at,
      self.file_name if file_name is None else file_name,
      self.__json_url if file_url is None else file_url,
    ]
    info = {key: value for key, value in zip(self.info_keys, values)}

    return info


def convert(ts: VSCodeThemeServer) -> dict:

  def is_dict_in_none_value(dct: dict | str | None, parent: str = '') -> bool:
    for ky, vl in dct.items():
      if isinstance(vl, dict):
        if is_dict_in_none_value(vl, f'{parent}.{ky}' if parent else ky):
          return True
      else:
        if vl is None:
          print(f'値に`None` が存在します')
          print(f'{parent=}:\n\tkey={ky}: value={vl}')
          return True
    return False

  main = dict()
  # GitHub Repository Data
  main |= ts.info
  d = dict()
  # Pythonista3 Color Theme
  d['background'] = ts.get_value(colors='editor.background')
  d['bar_background'] = ts.get_value(colors='tab.activeBackground')
  d['dark_keyboard'] = True
  d['default_text'] = ts.get_value(tokenColors=[
    'text',
    'foreground',
  ])
  d['editor_actions_icon_background'] = ts.get_value(
    colors='menu.selectionBackground')
  d['editor_actions_icon_tint'] = ts.get_value(
    colors='menu.selectionForeground')
  d['editor_actions_popover_background'] = ts.get_value(
    colors='menu.background')
  d['error_text'] = ts.get_value(colors='editorError.foreground')

  # d['font-family'] = 'Menlo-Regular'
  # d['font-siz'] = 15.0

  d['gutter_background'] = ts.get_value(colors='editorGutter.background')
  d['gutter_border'] = ts.get_value(colors='tab.border')
  d['interstitial'] = '#ff00ff'  # xxx: 仮
  d['library_background'] = ts.get_value(colors='sideBar.background')
  d['library_tint'] = ts.get_value(colors='sideBarSectionHeader.foreground')
  d['line_number'] = ts.get_value(colors='editorLineNumber.foreground')
  d['name'] = ts.get_value('name')
  d['separator_line'] = ts.get_value(colors='focusBorder')
  d['tab_background'] = ts.get_value(colors='tab.inactiveBackground')
  d['tab_title'] = ts.get_value(colors='tab.inactiveForeground')
  d['text_selection_tint'] = ts.get_value(
    colors='editorLineNumber.activeForeground')
  d['thumbnail_border'] = ts.get_value(colors='sideBar.border')
  d['tint'] = ts.get_value(colors='editorCursor.foreground')

  s = dict()  # scopes
  s['bold'] = {
    'font-style': 'bold',
  }
  s['bold-italic'] = {
    'font-style': 'bold-italic',
  }
  s['builtinfunction'] = {
    'color': ts.get_value(tokenColors=[
      'entity.name.function',
      'foreground',
    ]),
  }
  s['checkbox'] = {
    'checkbox': True,
  }
  s['checkbox-done'] = {
    'checkbox': True,
    'done': True,
  }
  s['class'] = {
    'color': ts.get_value(tokenColors=[
      'entity.name.class',
      'foreground',
    ]),
  }
  s['classdef'] = {
    'color': ts.get_value(tokenColors=[
      'entity.name.class',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['code'] = {
    'background-color':
    ts.get_value(tokenColors=[
      'markup.fenced_code.block',
      'foreground',
    ]),
    'corner-radius':
    2.0,
  }
  s['codeblock-start'] = {
    'color':
    ts.get_value(tokenColors=[
      'markup.inline.raw.string',
      'foreground',
    ]),
  }
  s['comment'] = {
    'color': ts.get_value(tokenColors=[
      'comment',
      'foreground',
    ]),
    'font-style': 'italic',
  }
  s['decorator'] = {
    'color': ts.get_value(tokenColors=[
      'meta.type.annotation',
      'foreground',
    ]),
  }
  s['default'] = {
    'color': ts.get_value(tokenColors=[
      'text',
      'foreground',
    ]),
  }
  s['docstring'] = {
    'color':
    ts.get_value(tokenColors=[
      'entity.other.attribute-name',
      'foreground',
    ]),
    'font-style':
    'italic',
  }
  s['escape'] = {
    'background-color': ts.get_value(tokenColors=[
      'support',
      'foreground',
    ]),
  }
  s['formatting'] = {
    'color':
    ts.get_value(tokenColors=[
      'markup.fenced_code.block',
      'foreground',
    ]),
  }
  s['function'] = {
    'color':
    ts.get_value(tokenColors=[
      'entity.name.function.method',
      'foreground',
    ]),
  }
  s['functiondef'] = {
    'color':
    ts.get_value(tokenColors=[
      'entity.name.function.method',
      'foreground',
    ]),
    'font-style':
    'bold',
  }
  s['heading-1'] = {
    'color': ts.get_value(tokenColors=[
      'markup.heading',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['heading-2'] = {
    'color': ts.get_value(tokenColors=[
      'markup.heading',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['heading-3'] = {
    'color': ts.get_value(tokenColors=[
      'markup.heading',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['italic'] = {
    'font-style': 'italic',
  }
  s['keyword'] = {
    'color': ts.get_value(tokenColors=[
      'keyword',
      'foreground',
    ]),
  }
  s['link'] = {
    'text-decoration': 'underline',
    'color': ts.get_value(tokenColors=[
      'markup.underline.link',
      'foreground',
    ]),
  }
  s['marker'] = {
    'box-background-color':
    ts.get_value(colors='editorMarkerNavigation.background'),
    'box-border-color':
    ts.get_value(colors='inputOption.activeBorder'),
    'box-border-type':
    4,
  }
  s['module'] = {
    'color': ts.get_value(tokenColors=[
      'entity.name.import.go',
      'foreground',
    ]),
  }
  s['number'] = {
    'color': ts.get_value(tokenColors=[
      'constant',
      'foreground',
    ]),
  }
  s['project'] = {
    'font-style': 'bold',
  }
  s['string'] = {
    'color': ts.get_value(tokenColors=[
      'string',
      'foreground',
    ]),
  }
  s['tag'] = {
    'text-decoration': 'none',
  }
  s['task-done'] = {
    'color': ts.get_value(colors='notificationsInfoIcon.foreground'),
    'text-decoration': 'strikeout',
  }

  d['scopes'] = s

  if is_dict_in_none_value(d):
    raise ValueError('設定する値に`None` が存在するため変換できません')
  main |= d
  return main


def get_user_theme_dir() -> Path | None:
  try:
    # xxx: 一応
    from objc_util import ObjCClass
  except ModuleNotFoundError as e:
    print(f'{e}:')
    return None
  _path_objc = ObjCClass('PA2UITheme').sharedTheme().userThemesPath()
  _path = Path(str(_path_objc))
  return _path


def to_dump(json_data: dict, info_data: dict | None = None) -> str:
  dump_data = json_data if info_data is None else json_data | info_data
  kwargs = {
    'indent': 1,
    'sort_keys': True,
    'ensure_ascii': False,
  }
  return json.dumps(dump_data, **kwargs)


def export(dump_theme: str, theme_file_name: str,
           target_dir: Path | None) -> None:
  if target_dir is None or not isinstance(target_dir, Path):
    raise ValueError(f'`target_dir` の値が不正です')

  if not target_dir.is_dir():
    target_dir.mkdir(parents=True)
  json_file = Path(target_dir, theme_file_name)
  json_file.write_text(dump_theme, encoding='utf-8')


def build(ts: VSCodeThemeServer,
          save_vscode: bool = True,
          vscode_dir: Path = None,
          save_pythonista: bool = True,
          pythonista_dir: Path = PY_LOCAL) -> str:
  converted = convert(ts)
  theme_dump = to_dump(converted)

  if save_vscode:
    export(ts.dump, ts.file_name,
           ts.tmp_dir if vscode_dir is None else vscode_dir)
  if save_pythonista:
    export(theme_dump, ts.file_name, pythonista_dir)

  if (user_theme_dir := get_user_theme_dir()) is not None:
    export(theme_dump, ts.file_name, user_theme_dir)

  return theme_dump


def create_url_scheme(json_data: bytes) -> str:
  compressed = zlib.compress(json_data, level=9)
  b64bytes = base64.urlsafe_b64encode(compressed)
  param_body = b64bytes.decode('utf-8').replace('=', '~')
  scheme_header = 'pythonista3://?action=add-theme&theme-data='
  return f'{scheme_header}{param_body}'


# ref: [Pythonで短縮URLを自動生成するサンプルコード|Python自動化研究所](https://note.com/python_lab/n/n1635a2f56b99)
def create_short_url(long_url: str) -> str:
  api_url = 'http://tinyurl.com/api-create.php'
  params = {'url': long_url}

  try:
    response = requests.get(api_url, params=params)
    response.raise_for_status()
  except ConnectionError as e:
    print(f'Connection Error:{e}')
    raise
  except HTTPError as e:
    print(f'HTTP Error:{e}')
    raise
  except Timeout as e:
    print(f'Timeout Error:{e}')
    raise
  except RequestException as e:
    print(f'Error:{e}')
    raise
  return response.text


def out_for_print(ts: VSCodeThemeServer,
                  save_vscode: bool = True,
                  vscode_dir: Path = None,
                  save_pythonista: bool = True,
                  pythonista_dir: Path = PY_LOCAL) -> str:

  builded_theme = build(ts, save_vscode, vscode_dir, save_pythonista,
                        pythonista_dir)

  bytes_theme = builded_theme.encode(encoding='utf-8')
  compiled_scheme = create_url_scheme(bytes_theme)
  short_url = create_short_url(compiled_scheme)

  new_line = '\n'

  name_header = f'### {ts.get_value("name")}'
  link_header = f'#### Link(URL scheme)'
  link_tag = f'[{ts.file_name}]({short_url})'
  scheme_header = f'#### scheme raw'
  scheme_tag = f'```{new_line}{compiled_scheme}{new_line}```'

  out_text = (new_line * 2).join([
    name_header,
    link_header,
    link_tag,
    scheme_header,
    scheme_tag,
    new_line * 2,
  ])

  return out_text


if __name__ == '__main__':
  dark_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  light_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'

  urls = [
    dark_url,
    light_url,
  ]

  for u in urls:
    t = VSCodeThemeServer(u, use_local=False)
    #aaa = convert(t)
    #build(t)
    print(out_for_print(t))

