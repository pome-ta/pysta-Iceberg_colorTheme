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
  url: str = 'github_url'  # 対象のVSCode Color Theme リポジトリURL
  author: str = 'author_name'  # Theme 作者名
  license: str = 'license'  # リポジトリに表記されているライセンス
  pushed_at: str = 'pushed_at'  # main ブランチでの最終コミット日時

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


class SchemeItems(SchemeTemplate):
  pass


class Pythonista3ThemeObject:
  """
  memo:
  `VSCodeThemeObject` 構成と似たような感じにするには。。。
  そもそも、構成として似せた方がええよね？
  """

  def __init__(self, seve_local: bool = True, local: Path | None = None):
    # wip: モジュール化した時のファイルパス扱い
    self.local_path = Path('./testThemes') if local is None else local


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
                    html_url: str,
                    author: str,
                    license: str,
                    pushed_at: str,
                    file_name: str | None = None) -> DictDotNotation:
    # xxx: `_` 3つ
    info = {
      '___html_url': html_url,
      '___author': author,
      '___license': license,
      '___pushed_at': pushed_at,
      '___file_name': self.name if file_name is None else file_name,
    }
    return self.DictDotNotation(info)

  def __get_info_attribute(self) -> DictDotNotation | None:
    tokens = self.__api_tokens()
    if tokens is None:
      return
    _html_url = tokens.get('html_url')
    _author = tokens.get('owner').get('login')
    _license = l.get('name') if (l :=
                                 tokens.get('license')) is not None else str(l)
    _pushed_at = tokens.get('pushed_at')

    info = self.__create_info(_html_url, _author, _license, _pushed_at)

    return info

  def __get_local_data(self) -> list[dict, DictDotNotation] | None:
    data_text = Path(self.local_path, self.name).read_text()
    loads = json.loads(data_text)

    _html_url = loads.get('___html_url')
    _author = loads.get('___author')
    _license = loads.get('___license')
    _pushed_at = loads.get('___pushed_at')

    info = self.__create_info(_html_url, _author, _license, _pushed_at)

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
  #target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  target_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'

  vs_theme = VSCodeThemeObject(target_url, 0)
  # aa = to.to_dump()
  vs_theme.export()
  # tp = ConvertThemeTemplate(url='bar')
  #s = SchemeItems(url='a')

