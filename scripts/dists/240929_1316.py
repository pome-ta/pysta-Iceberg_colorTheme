"""
note: 直接dict に書き込む形式。シンプルに
  - 引数をぐだぐだと考慮しない
  - class の責務を分ける
    - 変数をVSCode とPythonista3 の共通
    - インスタンスメソッドを外だし
"""

from pathlib import Path
import json

import requests

# todo: Pythonista3 以外での`Path` 挙動差分用
ROOT_PATH: Path = Path(__file__).parent

VS_LOCAL = Path(ROOT_PATH, './vscodeThemes')
PY_LOCAL = Path(ROOT_PATH, './testThemes')


class Theme:
  file_name: str | None
  tmp_dir: Path
  data: dict | None
  info: dict | None
  dump: str
  info_keys = [
    '_repository_url',
    '_author_name',
    '_license_kind',
    '_pushed_at',
    '_file_name',
    '_file_url',
  ]

  @staticmethod
  def to_dump(json_data: dict, info_data: dict | None = None) -> str:
    dump_data = json_data if info_data is None else json_data | info_data
    kwargs = {
      'indent': 1,
      'sort_keys': True,
      'ensure_ascii': False,
    }
    return json.dumps(dump_data, **kwargs)

  def export(self, target_dir: Path | None = None):
    dir = self.tmp_dir if target_dir is None else target_dir

    # xxx: ディレクトリ周り、存在しない時の処理
    if not dir.is_dir():
      dir.mkdir(parents=True)

    json_file = Path(dir, self.file_name)
    json_file.write_text(self.dump, encoding='utf-8')


class VSCode(Theme):

  def __init__(self,
               theme_json_url: str,
               use_local: bool = False,
               tmp_dir: Path = VS_LOCAL):
    self.json_url = theme_json_url
    self.file_name = self.get_file_name(theme_json_url)
    self.tmp_dir = tmp_dir

    if use_local:
      self.data, self.info = self.get_tmp_data_info()
    else:
      self.data = self.get_data()
      self.info = self.get_info()

    self.dump = self.to_dump(self.data, self.info)

  @staticmethod
  def get_file_name(url: str) -> str | None:
    path = Path(url)  # xxx: 取り出し方が乱暴
    if path.suffix == '.json':
      return path.name
    # wip: `None` 時、エラー吐く
    return None

  def get_tmp_data_info(self) -> list[dict]:
    data_text = Path(self.tmp_dir, self.file_name).read_text()
    loads = json.loads(data_text)

    info = self.__create_info(*[loads.get(key) for key in self.info_keys])

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
                    file_name: str | None = None,
                    file_url: str | None = None) -> dict:
    values = [
      repository_url,
      author_name,
      license_kind,
      pushed_at,
      self.file_name if file_name is None else file_name,
      self.json_url if file_url is None else file_url,
    ]
    info = {key: value for key, value in zip(self.info_keys, values)}

    return info


class ThemeObject:
  # xxx: この宣言だと無意味か
  json_url: str
  file_name: str | None
  tmp_dir: Path
  data: dict | None
  info: dict | None
  info_keys: list

  @staticmethod
  def get_file_name(url: str) -> str | None:
    path = Path(url)  # xxx: 取り出し方が乱暴
    if path.suffix == '.json':
      return path.name
    # wip: `None` 時、エラー吐く
    return None

  @staticmethod
  def get_tmp_dir(tmp_dir: Path | str | None) -> Path:
    if tmp_dir is None:
      return Path(ROOT_PATH, './vscodeThemes')
    elif isinstance(tmp_dir, Path):
      return tmp_dir
    else:
      return Path(tmp_dir)

  def get_tmp_data_info(self) -> list[dict]:
    data_text = Path(self.tmp_dir, self.file_name).read_text()
    loads = json.loads(data_text)

    info = self.__create_info(*[loads.get(key) for key in self.info_keys])

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
                    file_name: str | None = None,
                    file_url: str | None = None) -> dict:
    values = [
      repository_url,
      author_name,
      license_kind,
      pushed_at,
      self.file_name if file_name is None else file_name,
      self.json_url if file_url is None else file_url,
    ]
    info = {key: value for key, value in zip(self.info_keys, values)}

    return info


class VSCodeThemeObject(ThemeObject):

  def __init__(self,
               theme_json_url: str,
               use_local: bool = False,
               tmp_dir: Path | str | None = None):
    self.info_keys = [
      '_repository_url',
      '_author_name',
      '_license_kind',
      '_pushed_at',
      '_file_name',
      '_file_url',
    ]

    self.json_url = theme_json_url
    self.file_name = self.get_file_name(theme_json_url)
    self.tmp_dir = self.get_tmp_dir(tmp_dir)

    if use_local:
      self.data, self.info = self.get_tmp_data_info()
    else:
      self.data = self.get_data()
      self.info = self.get_info()

    # xxx: `None` の時ここで弾く?

  def to_dump(self) -> str | None:
    if self.data is None:
      # wip: `None` 時、エラー吐く
      return None
    data = self.data if self.info is None else self.data | self.info
    kwargs = {
      'indent': 1,
      'sort_keys': True,
      'ensure_ascii': False,
    }
    return json.dumps(data, **kwargs)

  def export(self, vs_themes_dir: Path | str | None = None):
    themes_dir = self.tmp_dir if vs_themes_dir is None else vs_themes_dir if isinstance(
      vs_themes_dir, Path) else Path(vs_themes_dir)

    # xxx: ディレクトリ周り、存在しない時の処理
    if not themes_dir.is_dir():
      themes_dir.mkdir(parents=True)

    theme_json = self.to_dump()
    json_file = Path(themes_dir, self.file_name)
    json_file.write_text(theme_json, encoding='utf-8')


class ThemeInterpretation:
  """
  VSCode のTheme 情報を指定して取得
  """

  def __init__(self, target: dict):
    self.target = target

  def __for_colors(self, key: str) -> str | bool | int | float | None:
    # xxx: `get` じゃなくて`[key]` の方がいいか?
    return self.target['colors'].get(key)

  def __for_token_colors(self,
                         keys: list[str]) -> str | bool | int | float | None:
    scope, settings = keys
    for tokenColor in self.target.get('tokenColors'):
      _scope = tokenColor.get('scope')
      # xxx: 配列格納に合わせる
      scopes = _scope if isinstance(_scope, list) else [_scope]
      if scope in scopes:
        return tokenColor.get('settings').get(settings)

  def get_value(
      self,
      search_value: str = '',
      colors: str | None = None,
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
      # wip: `None` 時、エラー吐く
      raise print(
        f'{self}: value の値が`{value}` です:\n- {search_value=}\n- {colors=}\n- {tokenColors=}'
      )
    return value


def convert(vs_theme_obj: VSCodeThemeObject) -> dict:
  vt = ThemeInterpretation(vs_theme_obj.data)
  d = dict()

  d |= vs_theme_obj.info
  d['background'] = vt.get_value(colors='editor.background')
  d['bar_background'] = vt.get_value(colors='tab.activeBackground')
  d['dark_keyboard'] = True
  d['default_text'] = vt.get_value(tokenColors=[
    'text',
    'foreground',
  ])
  d['editor_actions_icon_background'] = vt.get_value(
    colors='menu.selectionBackground')
  d['editor_actions_icon_tint'] = vt.get_value(
    colors='menu.selectionForeground')
  d['editor_actions_popover_background'] = vt.get_value(
    colors='menu.background')
  d['error_text'] = vt.get_value(colors='editorError.foreground')

  # d['font-family'] = 'Menlo-Regular'
  # d['font-siz'] = 15.0

  d['gutter_background'] = vt.get_value(colors='editorGutter.background')
  d['gutter_border'] = vt.get_value(colors='tab.border')
  d['interstitial'] = '#ff00ff'  # xxx: 仮
  d['library_background'] = vt.get_value(colors='sideBar.background')
  d['library_tint'] = vt.get_value(colors='sideBarSectionHeader.foreground')
  d['line_number'] = vt.get_value(colors='editorLineNumber.foreground')
  d['name'] = vt.get_value('name')
  d['separator_line'] = vt.get_value(colors='focusBorder')
  d['tab_background'] = vt.get_value(colors='tab.inactiveBackground')
  d['tab_title'] = vt.get_value(colors='tab.inactiveForeground')
  d['text_selection_tint'] = vt.get_value(
    colors='editorLineNumber.activeForeground')
  d['thumbnail_border'] = vt.get_value(colors='sideBar.border')
  d['tint'] = vt.get_value(colors='editorCursor.foreground')

  s = dict()  # scopes
  s['bold'] = {
    'font-style': 'bold',
  }
  s['bold-italic'] = {
    'font-style': 'bold-italic',
  }
  s['builtinfunction'] = {
    'color': vt.get_value(tokenColors=[
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
    'color': vt.get_value(tokenColors=[
      'entity.name.class',
      'foreground',
    ]),
  }
  s['classdef'] = {
    'color': vt.get_value(tokenColors=[
      'entity.name.class',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['code'] = {
    'background-color':
    vt.get_value(tokenColors=[
      'markup.inline.raw.string',
      'foreground',
    ]),
    'corner-radius':
    2.0,
  }
  s['codeblock-start'] = {
    'color':
    vt.get_value(tokenColors=[
      'markup.inline.raw.string',
      'foreground',
    ]),
  }
  s['comment'] = {
    'color': vt.get_value(tokenColors=[
      'comment',
      'foreground',
    ]),
    'font-style': 'italic',
  }
  s['decorator'] = {
    'color': vt.get_value(tokenColors=[
      'meta.type.annotation',
      'foreground',
    ]),
  }
  s['default'] = {
    'color': vt.get_value(tokenColors=[
      'text',
      'foreground',
    ]),
  }
  s['docstring'] = {
    'color':
    vt.get_value(tokenColors=[
      'entity.other.attribute-name',
      'foreground',
    ]),
    'font-style':
    'italic',
  }
  s['escape'] = {
    'background-color': vt.get_value(tokenColors=[
      'support',
      'foreground',
    ]),
  }
  s['formatting'] = {
    'color':
    vt.get_value(tokenColors=[
      'markup.fenced_code.block',
      'foreground',
    ]),
  }
  s['function'] = {
    'color':
    vt.get_value(tokenColors=[
      'entity.name.function.method',
      'foreground',
    ]),
  }
  s['functiondef'] = {
    'color':
    vt.get_value(tokenColors=[
      'entity.name.function.method',
      'foreground',
    ]),
    'font-style':
    'bold',
  }
  s['heading-1'] = {
    'color': vt.get_value(tokenColors=[
      'markup.heading',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['heading-2'] = {
    'color': vt.get_value(tokenColors=[
      'markup.heading',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['heading-3'] = {
    'color': vt.get_value(tokenColors=[
      'markup.heading',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['italic'] = {
    'font-style': 'italic',
  }
  s['keyword'] = {
    'color': vt.get_value(tokenColors=[
      'keyword',
      'foreground',
    ]),
  }
  s['link'] = {
    'text-decoration': 'underline',
    'color': vt.get_value(tokenColors=[
      'markup.underline.link',
      'foreground',
    ]),
  }
  s['marker'] = {
    'box-background-color':
    vt.get_value(colors='editorMarkerNavigation.background'),
    'box-border-color':
    vt.get_value(colors='inputOption.activeBorder'),
    'box-border-type':
    4,
  }
  s['module'] = {
    'color': vt.get_value(tokenColors=[
      'entity.name.import.go',
      'foreground',
    ]),
  }
  s['number'] = {
    'color': vt.get_value(tokenColors=[
      'constant',
      'foreground',
    ]),
  }
  s['project'] = {
    'font-style': 'bold',
  }
  s['string'] = {
    'color': vt.get_value(tokenColors=[
      'string',
      'foreground',
    ]),
  }
  s['tag'] = {
    'text-decoration': 'none',
  }
  s['task-done'] = {
    'color': vt.get_value(colors='notificationsInfoIcon.foreground'),
    'text-decoration': 'strikeout',
  }

  d['scopes'] = s

  return d

'''
- theme を格納
- schema を返す

- export
  - vs のdump 格納
  - pysta のdump 格納



vs は、server として渡す機能
'''
def build(vs_theme, ) -> str:
  pass


if __name__ == '__main__':
  dark_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  light_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'

  #vs_iceberg_dark = VSCodeThemeObject(dark_url, use_local=False)
  vs_iceberg_dark = VSCode(dark_url, use_local=False)
  converted_dict = convert(vs_iceberg_dark)

  x = 1

