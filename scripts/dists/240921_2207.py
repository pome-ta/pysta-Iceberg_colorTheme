"""
note: GitHub 取り込みと、dump 取り込み双方での設計
  - 制限考えるのはAPI 使う時のみか
"""

from pathlib import Path
import json
from dataclasses import dataclass

import requests


@dataclass
class SchemeTemplate:
  author_name: str = 'author_name'  # Theme 作者名
  file_name: str = 'json_file_name'  # 参照元`.json` ファイル名
  file_url: str = 'json_file_url'  # 参照元`.json` ファイル名
  license_kind: str = 'license'  # リポジトリに表記されているライセンス
  pushed_at: str = 'pushed_at'  # main ブランチでの最終コミット日時
  repository_url: str = 'github_url'  # 対象のVSCode Color Theme リポジトリURL

  background: str = '#ff0000'  # エディターのデフォルトの背景色
  bar_background: str = ' #ff0000'  # ツールバーとアクティブなタブの背景色
  dark_keyboard: bool = True  # ダーク色のオンスクリーン キーボードを使用するかどうか
  default_text: str = '#ff0000'  # インターフェイステキストのデフォルトの色
  editor_actions_icon_background: str = '#ff0000'
  editor_actions_icon_tint: str = '#ff0000'
  editor_actions_popover_background: str = '#ff0000'
  error_text: str = '#ff0000'
  # fontFamily: str = 'Menlo-Regular'  # デフォルトのエディターおよびコンソールのフォント ファミリ
  # fontSize: float = 15.0  # デフォルトのエディターとコンソールのフォント サイズ
  gutter_background: str = '#ff0000'  # エディターの左側の行番号列の背景色
  gutter_border: str = '#ff0000'  # エディターから余白を区切る境界線の色
  interstitial: str = '#ff0000'
  library_background: str = '#ff0000'  # スクリプト ライブラリの背景色
  library_tint: str = '#ff0000'
  line_number: str = '#ff0000'  # ガター内の行番号の色
  name: str = 'tmpFormatDump'
  # scopes: エディターでのさまざまな種類のテキストの書式設定。書式設定オプションは CSS スタイルに似ています
  scopes_bold_fontStyle: str = 'bold'  # 太字のテキスト
  scopes_boldItalic_fontStyle: str = 'bold-italic'  # 太字と斜体のテキスト
  scopes_builtinfunction_color: str = '#ff0000'  # 関数呼び出しの一部としての組み込み関数
  scopes_checkbox_checkbox: bool = True  # タスクペーパーのチェックボックス
  scopes_checkboxDone_checkbox: bool = True  # タスクペーパーのチェックボックスをオンにします
  scopes_checkboxDone_done: bool = True
  scopes_class_color: str = '#ff0000'  # クラスのインスタンス化の一部としてのクラス名
  scopes_classdef_color: str = '#ff0000'  # クラス定義の一部としてのクラス名
  scopes_classdef_fontStyle: str = 'bold'
  scopes_code_backgroundColor: str = '#ff0000'  # ンラインコードシーケンス
  scopes_code_cornerRadius: float = 2.0
  scopes_codeblockStart_color: str = '#ff0000'  # コードブロック開始後の GitHub スタイルの構文強調表示命令
  scopes_comment_color: str = '#ff0000'  # コメント
  scopes_comment_fontStyle: str = 'italic'
  scopes_decorator_color: str = '#ff0000'  # 関数またはクラスの装飾ステートメント
  scopes_default_color: str = '#ff0000'  # デフォルトのテキスト。プレーン テキスト ファイルまたは特別な意味を持たないテキストの場合
  scopes_docstring_color: str = '#ff0000'  # Python の複数行の文字列リテラル
  scopes_docstring_fontStyle: str = 'italic'
  scopes_escape_backgroundColor: str = '#ff0000'  # おそらく文字列リテラル内のエスケープ文字用であるはずですが、何もしないようです
  scopes_formatting_color: str = '#ff0000'
  scopes_function_color: str = '#ff0000'  # 関数呼び出しの一部としての関数名
  scopes_functiondef_color: str = '#ff0000'  # 関数定義の一部としての関数名
  scopes_functiondef_fontStyle: str = 'bold'
  scopes_heading1_fontStyle: str = 'bold'  # レベル 1 の見出し
  scopes_heading2_fontStyle: str = 'bold'  # レベル 2 の見出し
  scopes_heading3_fontStyle: str = 'bold'  # レベル 3 の見出し
  scopes_italic_fontStyle: str = 'italic'  # 斜体のテキスト
  scopes_keyword_color: str = '#ff0000'  # 言語のキーワード
  scopes_link_textDecoration: str = 'underline'  # タイトルをリンクします
  scopes_marker_boxBackgroundColor: str = '#ff0000'
  scopes_marker_boxBorderColor: str = '#ff0000'
  scopes_marker_boxBorderType: int = 4
  scopes_module_color: str = '#ff0000'  # import ステートメントの一部としての Python モジュール名
  scopes_number_color: str = '#ff0000'  # 数字
  scopes_project_fontStyle: str = 'bold'  # タスクペーパープロジェクト
  scopes_string_color: str = '#ff0000'  # 文字列リテラル
  scopes_tag_textDecoration: str = 'none'  # これは Task paper ですか、HTML ですか、それとも何ですか?
  scopes_taskDone_color: str = '#ff0000'  # タスクペーパーのタスクが完了しました
  scopes_taskDone_textDecoration: str = 'strikeout'

  separator_line: str = '#ff0000'  # ツールバー/タブとエディターの間の区切り線の色
  tab_background: str = '#ff0000'  # 非アクティブなタブの背景色
  tab_title: str = '#ff0000'  # タブのタイトルのテキストの色
  text_selection_tint: str = '#ff0000'  # テキスト選択とカーソルの色合い
  thumbnail_border: str = '#ff0000'  # スクリプト ライブラリ内のファイル間の境界線の色
  tint: str = '#ff0000'  # インターフェースボタンの色合い


class Pythonista3ThemeObject:
  """
  memo:
  `VSCodeThemeObject` 構成と似たような感じにするには。。。
  そもそも、構成として似せた方がええよね?
  
  vscode のtheme 情報をどの状態で持たせるか?
  initialize 時の変数、引数の持たせ方を考えたい
  
  """

  def __init__(self, save_local: bool = True, local: Path | None = None):
    self.sava_local = save_local
    # wip: モジュール化した時のファイルパス扱い
    self.local_path = Path('./testThemes') if local is None else local
    self.name: str
    self.data: dict

  def convert(self, scheme: SchemeItems):
    self.data = {
      '_author_name': scheme.author_name,
      '_file_name': scheme.file_name,
      '_file_url': scheme.file_url,
      '_license_kind': scheme.license_kind,
      '_pushed_at': scheme.pushed_at,
      '_repository_url': scheme.repository_url,


      'background': p.background,
      'bar_background': p.bar_background,
      'dark_keyboard': p.dark_keyboard,
      'default_text': p.default_text,
      'editor_actions_icon_background': p.editor_actions_icon_background,
      'editor_actions_icon_tint': p.editor_actions_icon_tint,
      'editor_actions_popover_background': p.editor_actions_popover_background,
      'error_text': p.error_text,
      'font-family': 'Menlo-Regular',
      'font-size': 15.0,
      'gutter_background': p.gutter_background,
      'gutter_border': p.gutter_border,
      'interstitial': p.interstitial,
      'library_background': p.library_background,
      'library_tint': p.library_tint,
      'line_number': p.line_number,
      'name': p.name,
      'scopes': {
        'bold': {
          'font-style': p.scopes_bold_font_style,
        },
        'bold-italic': {
          'font-style': p.scopes_bold_italic_font_style,
        },
        'builtinfunction': {
          'color': p.scopes_builtinfunction_color,
        },
        'checkbox': {
          'checkbox': p.scopes_checkbox_checkbox,
        },
        'checkbox-done': {
          'checkbox': p.scopes_checkbox_done_checkbox,
          'done': p.scopes_checkbox_done_done,
        },
        'class': {
          'color': p.scopes_class_color,
        },
        'classdef': {
          'color': p.scopes_classdef_color,
          'font-style': p.scopes_classdef_font_style,
        },
        'code': {
          'background-color': p.scopes_code_backgroundColor,
          'corner-radius': p.scopes_code_corner_radius,
        },
        'codeblock-start': {
          'color': p.scopes_codeblockStart_color,
        },
        'comment': {
          'color': p.scopes_comment_color,
          'font-style': p.scopes_comment_font_style,
        },
        'decorator': {
          'color': p.scopes_decorator_color,
        },
        'default': {
          'color': p.scopes_default_color,
        },
        'docstring': {
          'color': p.scopes_docstring_color,
          'font-style': p.scopes_docstring_font_style,
        },
        'escape': {
          'background-color': p.scopes_escape_color,
        },
        'formatting': {
          'color': p.scopes_formatting_color,
        },
        'function': {
          'color': p.scopes_function_color,
        },
        'functiondef': {
          'color': p.scopes_functiondef_color,
          'font-style': p.scopes_functiondef_font_style,
        },
        'heading-1': {
          'font-style': p.scopes_heading1_font_style,
        },
        'heading-2': {
          'font-style': p.scopes_heading2_font_style,
        },
        'heading-3': {
          'font-style': p.scopes_heading3_font_style,
        },
        'italic': {
          'font-style': p.scopes_italic_font_style,
        },
        'keyword': {
          'color': p.scopes_keyword_color,
        },
        'link': {
          'text-decoration': p.scopes_link_text_decoration,
        },
        'marker': {
          'box-background-color': p.scopes_marker_box_background_color,
          'box-border-color': p.scopes_marker_box_border_color,
          'box-border-type': p.scopes_marker_box_border_type,
        },
        'module': {
          'color': p.scopes_module_color,
        },
        'number': {
          'color': p.scopes_number_color,
        },
        'project': {
          'font-style': p.scopes_project_font_style,
        },
        'string': {
          'color': p.scopes_string_color,
        },
        'tag': {
          'text-decoration': p.scopes_tag_text_decoration,
        },
        'task-done': {
          'color': p.scopes_taskDone_color,
          'text-decoration': p.scopes_taskDone_text_decoration,
        },
      },
      'separator_line': p.separator_line,
      'tab_background': p.tab_background,
      'tab_title': p.tab_title,
      'text_selection_tint': p.text_selection_tint,
      'thumbnail_border': p.thumbnail_border,
      'tint': p.tint,
    }

  def build(self, scheme: SchemeItems | None):
    if scheme is not None:
      self.convert(scheme)
    
      

  def export(self):
    pass


class VSCodeThemeObject:
  """
  repository の情報をまるっと持つ
  API 取得と、直のraw 取得の2種類
  dump してローカルに保存
  ダンダーでの変数を外側で使うイメージ
  
  # 今後
  API の制限回避としてローカルdump から持ってくるパターンも考えたい
  """

  def __init__(self,
               github_url: str,
               use_local: bool = False,
               local: Path | None = None):
    self.url = github_url
    # wip: モジュール化した時のファイルパス扱い
    self.local_path = Path('./vscodeThemes') if local is None else local

    self.name: str = Path(github_url).name
    self.data: dict | None
    self.info: dict | None

    if not use_local:
      self.data = self.__get_url_json()
      self.info = self.__get_info_attribute()
    else:
      self.data, self.info = self.__get_local_data()
    # xxx: `None` の時ここで弾く？

  def to_dump(self) -> str:
    data = self.data if self.info is None else self.data | self.info
    kwargs = {
      'indent': 1,
      'sort_keys': True,
      'ensure_ascii': False,
    }
    return json.dumps(data, **kwargs)

  def export(self, vs_themes: Path | None = None):
    vs_themes = self.local_path if vs_themes is None else vs_themes

    # xxx: ディレクトリ周り、存在しない時の処理
    if not vs_themes.is_dir():
      vs_themes.mkdir(parents=True)

    theme_json = self.to_dump()
    json_file = Path(vs_themes, self.name)
    json_file.write_text(theme_json, encoding='utf-8')

  class DictDotNotation(dict):
    """
    ドットアクセスしたいための実装だけど。。。
    整列順序的に先頭に持っていきたいとなると
    先頭に`_` を付けたいけど、PyCharm 的に`protected メンバー` のアクセスとして
    警告出ちゃう。。。（無視で対処したくない）
    """

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.__dict__ = self

  def __get_url_json(self) -> dict | None:
    params = {
      'raw': 'true',
    }
    response = requests.get(self.url, params)
    if response.status_code == 200:
      # xxx: iceberg には、comment ない
      # wip: comment 削除処理
      return response.json()

  def __api_tokens(self) -> dict | None:
    _, _, owner_name, repo_name, *_ = Path(self.url).parts
    api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'

    # wip: 制限かかった時の処理
    response = requests.get(api_url)
    if response.status_code == 200:
      return response.json()

  def __create_info(self,
                    repository_url: str,
                    author_name: str,
                    license_kind: str,
                    pushed_at: str,
                    file_name: str | None = None) -> DictDotNotation:
    info = {
      '_repository_url': repository_url,
      '_author_name': author_name,
      '_license_kind': license_kind,
      '_pushed_at': pushed_at,
      '_file_name': self.name if file_name is None else file_name,
      '_file_url': self.url,
    }
    return self.DictDotNotation(info)

  def __get_info_attribute(self) -> DictDotNotation | None:
    tokens = self.__api_tokens()
    if tokens is None:
      return
    _repository_url = tokens.get('html_url')
    _author_name = tokens.get('owner').get('login')
    _license_kind = l.get('name') if (
      l := tokens.get('license')) is not None else str(l)
    _pushed_at = tokens.get('pushed_at')

    info = self.__create_info(_repository_url, _author_name, _license_kind,
                              _pushed_at)
    return info

  def __get_local_data(self) -> list[dict | DictDotNotation]:
    data_text = Path(self.local_path, self.name).read_text()
    loads = json.loads(data_text)

    _repository_url = loads.get('_repository_url')
    _author_name = loads.get('_author_name')
    _license_kind = loads.get('_license_kind')
    _pushed_at = loads.get('_pushed_at')

    info = self.__create_info(_repository_url, _author_name, _license_kind,
                              _pushed_at)
    return [
      loads,
      info,
    ]


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
      raise print(
        f'{self}: value の値が`{value}` です:\n- {search_value=}\n- {colors=}\n- {tokenColors=}'
      )
    return value


if __name__ == '__main__':

  class SchemeItems(SchemeTemplate):

    def __init__(self, vscode_theme: VSCodeThemeObject):
      vsi = ThemeInterpretation(vscode_theme.data)

      self.author_name = vscode_theme.info['_author_name']
      self.file_name = vscode_theme.info['_file_name']
      self.file_url = vscode_theme.info['_file_url']
      self.license_kind = vscode_theme.info['_license_kind']
      self.repository_url = vscode_theme.info['_repository_url']
      self.pushed_at = vscode_theme.info['_pushed_at']

      self.background = vsi.get_value(colors='editor.background')
      self.bar_background = vsi.get_value(colors='tab.activeBackground')
      self.dark_keyboard = True
      self.default_text = vsi.get_value(tokenColors=[
        'text',
        'foreground',
      ])
      self.editor_actions_icon_background = '#ff0000'
      self.editor_actions_icon_tint = '#00ff00'
      self.editor_actions_popover_background = '#0000ff'
      self.error_text = vsi.get_value(colors='editorError.foreground')

      self.gutter_background = vsi.get_value(colors='editorGutter.background')
      self.gutter_border = vsi.get_value(colors='tab.border')
      self.interstitial = '#ff00ff'
      self.library_background = vsi.get_value(colors='sideBar.background')
      self.library_tint = vsi.get_value(colors='sideBar.foreground')
      self.line_number = vsi.get_value(colors='editorLineNumber.foreground')
      self.name = vscode_theme.name

      self.scopes_bold_fontStyle = 'bold'
      self.scopes_boldItalic_fontStyle = 'bold-italic'
      self.scopes_builtinfunction_color = vsi.get_value(tokenColors=[
        'entity.name.function',
        'foreground',
      ])
      self.scopes_checkbox_checkbox = True
      self.scopes_checkboxDone_checkbox = True
      self.scopes_checkboxDone_done = True
      self.scopes_class_color = vsi.get_value(tokenColors=[
        'entity.name.class',
        'foreground',
      ])
      self.scopes_classdef_color = vsi.get_value(tokenColors=[
        'entity.name.class',
        'foreground',
      ])
      self.scopes_classdef_fontStyle = 'bold'
      self.scopes_code_backgroundColor = vsi.get_value(tokenColors=[
        'markup.fenced_code.block',
        'foreground',
      ])
      self.scopes_code_cornerRadius = 2.0
      self.scopes_codeblockStart_color = vsi.get_value(tokenColors=[
        'markup.inline.raw.string',
        'foreground',
      ])
      self.scopes_comment_color = vsi.get_value(tokenColors=[
        'comment',
        'foreground',
      ])
      self.scopes_comment_fontStyle = 'italic'
      self.scopes_decorator_color = vsi.get_value(tokenColors=[
        'text',
        'foreground',
      ])
      self.scopes_default_color = vsi.get_value(tokenColors=[
        'text',
        'foreground',
      ])
      self.scopes_docstring_color = vsi.get_value(tokenColors=[
        'punctuation.definition.template-expression',
        'foreground',
      ])
      self.scopes_docstring_fontStyle = 'italic'
      self.scopes_escape_backgroundColor = vsi.get_value(tokenColors=[
        'entity.other.attribute-name',
        'foreground',
      ])
      self.scopes_formatting_color = vsi.get_value(tokenColors=[
        'markup.fenced_code.block',
        'foreground',
      ])
      self.scopes_function_color = vsi.get_value(tokenColors=[
        'entity.name.function',
        'foreground',
      ])
      self.scopes_functiondef_color = vsi.get_value(tokenColors=[
        'entity.name.function',
        'foreground',
      ])
      self.scopes_functiondef_fontStyle = 'bold'
      self.scopes_heading1_fontStyle = 'bold'
      self.scopes_heading2_fontStyle = 'bold'
      self.scopes_heading3_fontStyle = 'bold'
      self.scopes_italic_fontStyle = 'italic'
      self.scopes_keyword_color = vsi.get_value(tokenColors=[
        'keyword',
        'foreground',
      ])
      self.scopes_link_textDecoration = 'underline'
      self.scopes_marker_boxBackgroundColor = vsi.get_value(
        colors='editorMarkerNavigation.background')
      self.scopes_marker_boxBorderColor = vsi.get_value(
        colors='inputOption.activeBorder')
      self.scopes_marker_boxBorderType = 4
      self.scopes_module_color = vsi.get_value(tokenColors=[
        'entity.name.import.go',
        'foreground',
      ])
      self.scopes_number_color = vsi.get_value(tokenColors=[
        'constant',
        'foreground',
      ])
      self.scopes_project_fontStyle = 'bold'
      self.scopes_string_color = vsi.get_value(tokenColors=[
        'string',
        'foreground',
      ])
      self.scopes_tag_textDecoration = 'none'
      self.scopes_taskDone_color = vsi.get_value(
        colors='notificationsInfoIcon.foreground')
      self.scopes_taskDone_textDecoration = 'strikeout'

      self.separator_line = vsi.get_value(colors='focusBorder')
      self.tab_background = vsi.get_value(colors='tab.inactiveBackground')
      self.tab_title = vsi.get_value(colors='tab.inactiveForeground')
      self.text_selection_tint = vsi.get_value(
        colors='editorLineNumber.activeForeground')
      self.thumbnail_border = vsi.get_value(colors='sideBar.border')
      self.tint = vsi.get_value(colors='editorCursor.foreground')

  #target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'

  vs_theme = VSCodeThemeObject(target_url, use_local=False)
  #vs_theme.export()

  scheme = SchemeItems(vs_theme)
  # print(scheme.file_url)
  x = 1
  # tp = ConvertThemeTemplate(url='bar')
  # s = SchemeItems(url='a')

