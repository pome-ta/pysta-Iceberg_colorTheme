# 📝 2024/09/27

## `zlib` しらべ


[structure - What does a zlib header look like? - Stack Overflow](https://stackoverflow.com/questions/9050260/what-does-a-zlib-header-look-like)

```
78 01 - No Compression/low
78 5E - Fast Compression
78 9C - Default Compression
78 DA - Best Compression 
```




# 📝 2024/09/23


## Class 設計化、佳境

### 引数の`pathlib,Path` 型

`Path` で受け取り予定だったけど、`str` も受けることにして

良きように、型変換させることにした（長くなるけど。。。）

### `None` の弾き方

ちゃんと、やっていきたい


# 📝 2024/09/22


## `pathlib.Path` の挙動

web のURL を`Path` で食わせたら

`https://github.com/` が`https:/github.com/` と、`:` 手前の`/` が消える

まぁ気持ち悪い使い方してたから、ちゃんと処理する


# 📝 2024/09/21

## `getter` と`setter`

ちょっと違うし、長くなるから、素直に書いた


## ここの`markdown`

PC のエディタでフォーマットをかけると、テーブルの整形でめちゃくちゃになるので
フォーマットがかけられなくなった。。。

列幅を無理にスペースや`-` で埋めてくれなくてもいいのだけどな。。。


# 📝 2024/09/20

## class にして、構造的に書いていく

### api の制限

[レート制限用 REST API エンドポイント - GitHub Docs](https://docs.github.com/ja/rest/rate-limit/rate-limit?apiVersion=2022-11-28)

`.json` の取得は問題ないだろうけど、repository 情報を取りたい時に怖いよなぁ


最悪、`license`、`pushed_at` を握りつぶすか


`status_code`


[REST API のトラブルシューティング - GitHub Docs](https://docs.github.com/ja/rest/using-the-rest-api/troubleshooting-the-rest-api?apiVersion=2022-11-28)


適当にAPI 呼び出しと、データ取得を回してみる


```.py
import time
import requests

url = 'https://github.com/pome-ta/dockerReactSample/blob/main/.devcontainer/devcontainer.json'

_, _, owner_name, repo_name, *_ = Path(url).parts
api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'
# wip: 制限かかった時の処理

api_res = requests.get(api_url)
api_json = api_res.json()
'''
for i in range(65):
  api_res = requests.get(api_url)
  api_json = api_res.json()
  print(i)
  time.sleep(0.9)
'''
params = {
  'raw': 'true',
}

res = requests.get(url, params)
res_json = res.json()


```

API 制限がされても、データの取得はできそう



# 📝 2024/09/19


## `pathlib` は便利ですねぇ

URL でもよしなにやってくれる


## 取得情報の保管方法

GitHub から持ってくる情報の格納を`SimpleNamespace` で検討したけど




```.py
class DictDotNotation(dict):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__dict__ = self
```

これにして、ドットアクセスと辞書の情報（`.json` にねじり込む用）を持たせるようにするか


## GitHub からの取り込み時

`class` 作った方が、スッキリまとまる？

アクセスしない時にどうするか？もあるけど

## `raise` の挙動

例外処理とか


# 📝 2024/09/17


## GitHub API

ガチャガチャと、情報は抜き出した。1時間60回くらいの制限あるっぽいけどまぁ大丈夫かな（トークン使わないと）？



### ガリガリと書き直しをローカルでやるか？

更新とか考えるとあまりよくないかも？

そこは、実行者の手に委ねるか、、、情報差を取るか、、、


### `.json` に突っ込む場合

取得した`.json` をローカルに保管予定（`.gitignore` する）。

整形してdump のつもりだけど、API の情報も入れるか？



### 更新情報

`['updated_at']` と`['pushed_at']` とで、微妙に違うのねぇ

[GitHub API V3 : what is the difference between pushed_at and updated_at? - Stack Overflow](https://stackoverflow.com/questions/15918588/github-api-v3-what-is-the-difference-between-pushed-at-and-updated-at)

### とはいえ、、、

`requests` を2回`get` するの筋悪いな、、、



# 📝 2024/09/16

iceberg は、ぼちぼちできてきたかも

## GitHub 上の諸々をとってくる

### `raw` ってどうやって見つけたっけ？

```.py
import requests

params = {
  'raw': 'true',
}

```


# 📝 2024/09/12


## iceberg 集中強化週間

こっちに移動

[pystaColorThemeDev/docs/icebergColorPallet.md at main · pome-ta/pystaColorThemeDev · GitHub](https://github.com/pome-ta/pystaColorThemeDev/blob/main/docs/icebergColorPallet.md)



# 📝 2024/09/09

色々と、テーブルで並べてるけど、訳がわからなくなってきた😇


## terminal

### iceberg.color-theme.json


| color_code | palette | key_name |
| --- | --- | --- |
| #00000000 | ![](https://via.placeholder.com/16/00000000/FFFFFF/?text=%20) | colors::editorBracketHighlight.foreground6 |
| #0E1015 | ![](https://via.placeholder.com/16/0E1015/FFFFFF/?text=%20) | colors::editorGroup.border <br> colors::editorGroupHeader.tabsBackground <br> colors::panel.border <br> colors::sideBar.border <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.noFolderBackground <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::titleBar.activeBackground <br> colors::titleBar.inactiveBackground |
| #0F1117 | ![](https://via.placeholder.com/16/0F1117/FFFFFF/?text=%20) | colors::dropdown.background <br> colors::dropdown.border <br> colors::input.background <br> colors::scrollbar.shadow <br> colors::widget.shadow |
| #161821 | ![](https://via.placeholder.com/16/161821/FFFFFF/?text=%20) | colors::activityBar.background <br> colors::activityBarBadge.foreground <br> colors::breadcrumb.background <br> colors::button.foreground <br> colors::editor.background <br> colors::extensionButton.prominentForeground <br> colors::menu.separatorBackground <br> colors::notifications.border <br> colors::panel.background <br> colors::peekViewEditor.background <br> colors::pickerGroup.border <br> colors::sideBar.background <br> colors::statusBarItem.errorForeground <br> colors::tab.activeBackground |
| #1E2132 | ![](https://via.placeholder.com/16/1E2132/FFFFFF/?text=%20) | colors::breadcrumbPicker.background <br> colors::debugToolBar.background <br> colors::editor.foldBackground <br> colors::editor.lineHighlightBackground <br> colors::editorGutter.background <br> colors::editorHoverWidget.background <br> colors::editorHoverWidget.border <br> colors::editorHoverWidget.statusBarBackground <br> colors::editorMarkerNavigation.background <br> colors::editorWidget.background <br> colors::editorWidget.border <br> colors::list.activeSelectionBackground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::menu.background <br> colors::menubar.selectionBackground <br> colors::notificationCenterHeader.background <br> colors::notifications.background <br> colors::peekViewEditorGutter.background <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::quickInput.background <br> colors::tab.hoverBackground <br> colors::terminal.ansiBlack |
| #242940 | ![](https://via.placeholder.com/16/242940/FFFFFF/?text=%20) | colors::editorIndentGuide.activeBackground <br> colors::editorRuler.foreground <br> colors::editorWhitespace.foreground <br> colors::focusBorder <br> colors::peekView.border <br> colors::sideBarSectionHeader.background <br> colors::tree.indentGuidesStroke |
| #24294040 | ![](https://via.placeholder.com/16/24294040/FFFFFF/?text=%20) | colors::editorIndentGuide.background <br> colors::editorOverviewRuler.border |
| #24294080 | ![](https://via.placeholder.com/16/24294080/FFFFFF/?text=%20) | colors::scrollbarSlider.background |
| #242940A0 | ![](https://via.placeholder.com/16/242940A0/FFFFFF/?text=%20) | colors::scrollbarSlider.hoverBackground |
| #272C42 | ![](https://via.placeholder.com/16/272C42/FFFFFF/?text=%20) | colors::editor.selectionBackground <br> colors::peekViewResult.selectionBackground |
| #2A3158 | ![](https://via.placeholder.com/16/2A3158/FFFFFF/?text=%20) | colors::menu.selectionBackground <br> colors::quickInputList.focusBackground |
| #3F455E | ![](https://via.placeholder.com/16/3F455E/FFFFFF/?text=%20) | colors::editorBracketMatch.background <br> colors::editorBracketMatch.border |
| #444B71 | ![](https://via.placeholder.com/16/444B71/FFFFFF/?text=%20) | colors::editorLineNumber.foreground |
| #4A548266 | ![](https://via.placeholder.com/16/4A548266/FFFFFF/?text=%20) | colors::selection.background <br> colors::terminal.selectionBackground |
| #53353B | ![](https://via.placeholder.com/16/53353B/FFFFFF/?text=%20) | colors::inputValidation.errorBackground |
| #6B7089 | ![](https://via.placeholder.com/16/6B7089/FFFFFF/?text=%20) | colors::activityBar.inactiveForeground <br> colors::badge.foreground <br> colors::breadcrumb.foreground <br> colors::debugIcon.breakpointDisabledForeground <br> colors::debugIcon.breakpointUnverifiedForeground <br> colors::descriptionForeground <br> colors::gitDecoration.ignoredResourceForeground <br> colors::gitDecoration.submoduleResourceForeground <br> colors::gitDecoration.untrackedResourceForeground <br> colors::panelTitle.inactiveForeground <br> colors::peekViewResult.lineForeground <br> colors::peekViewTitleDescription.foreground <br> colors::quickInput.foreground <br> colors::sideBarSectionHeader.foreground <br> colors::statusBar.debuggingForeground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderForeground <br> colors::tab.inactiveForeground <br> colors::tab.unfocusedActiveForeground <br> colors::terminal.ansiBrightBlack <br> colors::terminalCommandDecoration.defaultBackground <br> colors::titleBar.inactiveForeground <br> tokenColors::scope::comment::foreground <br> tokenColors::scope::markup.fenced_code.block::foreground <br> tokenColors::scope::meta.tag.sgml.doctype::foreground |
| #6B708920 | ![](https://via.placeholder.com/16/6B708920/FFFFFF/?text=%20) | colors::badge.background <br> colors::statusBarItem.hoverBackground |
| #6B708980 | ![](https://via.placeholder.com/16/6B708980/FFFFFF/?text=%20) | colors::tab.unfocusedInactiveForeground |
| #84A0C6 | ![](https://via.placeholder.com/16/84A0C6/FFFFFF/?text=%20) | colors::activityBarBadge.background <br> colors::debugIcon.continueForeground <br> colors::debugIcon.pauseForeground <br> colors::debugIcon.stepBackForeground <br> colors::debugIcon.stepIntoForeground <br> colors::debugIcon.stepOutForeground <br> colors::debugIcon.stepOverForeground <br> colors::editorBracketHighlight.foreground1 <br> colors::editorLink.activeForeground <br> colors::inputOption.activeBorder <br> colors::pickerGroup.foreground <br> colors::progressBar.background <br> colors::terminal.ansiBlue <br> colors::terminalCommandDecoration.successBackground <br> colors::textLink.activeForeground <br> colors::textLink.foreground <br> tokenColors::scope::entity.name.tag::foreground <br> tokenColors::scope::keyword::foreground <br> tokenColors::scope::keyword.operator.expression::foreground <br> tokenColors::scope::keyword.operator.new::foreground <br> tokenColors::scope::keyword.function::foreground <br> tokenColors::scope::meta.object-literal.key::foreground <br> tokenColors::scope::punctuation.definition.tag::foreground <br> tokenColors::scope::storage::foreground <br> tokenColors::scope::storage.type.function::foreground <br> tokenColors::scope::support::foreground <br> tokenColors::scope::support.type.property-name::foreground <br> tokenColors::scope::meta.diff.header::foreground <br> tokenColors::scope::markup.underline.link::foreground |
| #84A0C620 | ![](https://via.placeholder.com/16/84A0C620/FFFFFF/?text=%20) | colors::editorGroup.dropBackground <br> colors::list.dropBackground <br> colors::sideBar.dropBackground |
| #84A0C640 | ![](https://via.placeholder.com/16/84A0C640/FFFFFF/?text=%20) | colors::editor.wordHighlightBackground |
| #84A0C680 | ![](https://via.placeholder.com/16/84A0C680/FFFFFF/?text=%20) | colors::editor.wordHighlightStrongBackground <br> colors::editorOverviewRuler.wordHighlightForeground |
| #89B8C2 | ![](https://via.placeholder.com/16/89B8C2/FFFFFF/?text=%20) | colors::debugConsole.infoForeground <br> colors::debugTokenExpression.string <br> colors::editorBracketHighlight.foreground2 <br> colors::editorLightBulbAutoFix.foreground <br> colors::gitDecoration.modifiedResourceForeground <br> colors::gitDecoration.stageModifiedResourceForeground <br> colors::notificationsInfoIcon.foreground <br> colors::problemsInfoIcon.foreground <br> colors::symbolIcon.enumeratorMemberForeground <br> colors::symbolIcon.fieldForeground <br> colors::symbolIcon.interfaceForeground <br> colors::symbolIcon.variableForeground <br> colors::tab.activeModifiedBorder <br> colors::terminal.ansiCyan <br> tokenColors::scope::meta.link::foreground <br> tokenColors::scope::string::foreground <br> tokenColors::scope::meta.diff.range::foreground <br> tokenColors::scope::entity.name.import.go::foreground <br> tokenColors::scope::variable.scss::foreground |
| #89B8C220 | ![](https://via.placeholder.com/16/89B8C220/FFFFFF/?text=%20) | colors::merge.incomingContentBackground |
| #89B8C240 | ![](https://via.placeholder.com/16/89B8C240/FFFFFF/?text=%20) | colors::merge.incomingHeaderBackground |
| #89B8C24C | ![](https://via.placeholder.com/16/89B8C24C/FFFFFF/?text=%20) | colors::settings.modifiedItemIndicator |
| #89B8C280 | ![](https://via.placeholder.com/16/89B8C280/FFFFFF/?text=%20) | colors::tab.inactiveModifiedBorder |
| #91ACD1 | ![](https://via.placeholder.com/16/91ACD1/FFFFFF/?text=%20) | colors::terminal.ansiBrightBlue |
| #95C4CE | ![](https://via.placeholder.com/16/95C4CE/FFFFFF/?text=%20) | colors::terminal.ansiBrightCyan |
| #95C4CE80 | ![](https://via.placeholder.com/16/95C4CE80/FFFFFF/?text=%20) | colors::editorOverviewRuler.infoForeground |
| #A093C7 | ![](https://via.placeholder.com/16/A093C7/FFFFFF/?text=%20) | colors::debugTokenExpression.boolean <br> colors::debugTokenExpression.number <br> colors::debugTokenExpression.value <br> colors::editorBracketHighlight.foreground5 <br> colors::gitDecoration.renamedResourceForeground <br> colors::symbolIcon.functionForeground <br> colors::symbolIcon.methodForeground <br> colors::terminal.ansiMagenta <br> tokenColors::scope::constant::foreground <br> tokenColors::scope::support.constant::foreground <br> tokenColors::scope::entity.other.attribute-name::foreground <br> tokenColors::scope::keyword.other.unit::foreground <br> tokenColors::scope::markup.inline.raw.string::foreground <br> tokenColors::scope::meta.tag.attributes::foreground |
| #A093C720 | ![](https://via.placeholder.com/16/A093C720/FFFFFF/?text=%20) | colors::merge.currentContentBackground |
| #A093C740 | ![](https://via.placeholder.com/16/A093C740/FFFFFF/?text=%20) | colors::merge.currentHeaderBackground |
| #ADA0D3 | ![](https://via.placeholder.com/16/ADA0D3/FFFFFF/?text=%20) | colors::terminal.ansiBrightMagenta |
| #B4BE82 | ![](https://via.placeholder.com/16/B4BE82/FFFFFF/?text=%20) | colors::debugIcon.breakpointStackframeForeground <br> colors::debugIcon.restartForeground <br> colors::debugIcon.startForeground <br> colors::editorBracketHighlight.foreground3 <br> colors::gitDecoration.addedResourceForeground <br> colors::list.highlightForeground <br> colors::terminal.ansiGreen <br> tokenColors::scope::keyword.control.at-rule, keyword.control.content::foreground <br> tokenColors::scope::meta.type.annotation::foreground <br> tokenColors::scope::punctuation.definition.template-expression::foreground <br> tokenColors::scope::variable.language.this::foreground <br> tokenColors::scope::markup.inserted.diff::foreground <br> tokenColors::scope::support.type.class.flowtype::foreground <br> tokenColors::scope::punctuation.definition.block.tag.jsdoc::foreground <br> tokenColors::scope::storage.type.class.jsdoc::foreground <br> tokenColors::scope::variable.interpolation.scss::foreground |
| #B4BE8220 | ![](https://via.placeholder.com/16/B4BE8220/FFFFFF/?text=%20) | colors::diffEditor.insertedTextBackground |
| #B4BE8280 | ![](https://via.placeholder.com/16/B4BE8280/FFFFFF/?text=%20) | colors::editorGutter.addedBackground <br> colors::editorGutter.modifiedBackground <br> colors::editorOverviewRuler.addedForeground <br> colors::editorOverviewRuler.modifiedForeground |
| #C0CA8E | ![](https://via.placeholder.com/16/C0CA8E/FFFFFF/?text=%20) | colors::terminal.ansiBrightGreen |
| #C6C8D1 | ![](https://via.placeholder.com/16/C6C8D1/FFFFFF/?text=%20) | colors::activityBar.foreground <br> colors::breadcrumb.activeSelectionForeground <br> colors::breadcrumb.focusForeground <br> colors::button.background <br> colors::debugConsole.sourceForeground <br> colors::debugConsoleInputIcon.foreground <br> colors::debugTokenExpression.name <br> colors::dropdown.foreground <br> colors::editor.foreground <br> colors::editorCursor.foreground <br> colors::editorHoverWidget.foreground <br> colors::extensionButton.prominentBackground <br> colors::foreground <br> colors::input.foreground <br> colors::list.activeSelectionForeground <br> colors::menu.foreground <br> colors::menubar.selectionForeground <br> colors::notifications.foreground <br> colors::panelTitle.activeForeground <br> colors::peekViewResult.fileForeground <br> colors::peekViewTitleLabel.foreground <br> colors::settings.headerForeground <br> colors::sideBar.foreground <br> colors::tab.activeForeground <br> colors::terminal.ansiWhite <br> colors::terminal.foreground <br> colors::titleBar.activeForeground <br> tokenColors::scope::entity.name.class::foreground <br> tokenColors::scope::entity.name.function::foreground <br> tokenColors::scope::keyword.operator::foreground <br> tokenColors::scope::meta.brace.square::foreground <br> tokenColors::scope::punctuation.definition.block::foreground <br> tokenColors::scope::text::foreground <br> tokenColors::scope::entity.other.attribute-name.class.css, entity.other.attribute-name.parent-selector-suffix.css::foreground <br> tokenColors::scope::variable.other.jsdoc::foreground |
| #C6C8D120 | ![](https://via.placeholder.com/16/C6C8D120/FFFFFF/?text=%20) | colors::editorSuggestWidget.selectedBackground |
| #C6C8D140 | ![](https://via.placeholder.com/16/C6C8D140/FFFFFF/?text=%20) | colors::input.placeholderForeground |
| #CDD1E6 | ![](https://via.placeholder.com/16/CDD1E6/FFFFFF/?text=%20) | colors::editorLineNumber.activeForeground <br> colors::list.focusForeground <br> colors::menu.selectionForeground |
| #D2D4DE | ![](https://via.placeholder.com/16/D2D4DE/FFFFFF/?text=%20) | colors::button.hoverBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::terminal.ansiBrightWhite <br> tokenColors::scope::markup.bold::foreground |
| #E27878 | ![](https://via.placeholder.com/16/E27878/FFFFFF/?text=%20) | colors::debugConsole.errorForeground <br> colors::debugIcon.breakpointForeground <br> colors::debugIcon.stopForeground <br> colors::debugTokenExpression.error <br> colors::editorBracketHighlight.unexpectedBracket.foreground <br> colors::editorError.foreground <br> colors::editorOverviewRuler.errorForeground <br> colors::gitDecoration.deletedResourceForeground <br> colors::gitDecoration.stageDeletedResourceForeground <br> colors::inputValidation.errorBorder <br> colors::list.errorForeground <br> colors::notificationsErrorIcon.foreground <br> colors::problemsErrorIcon.foreground <br> colors::statusBarItem.errorBackground <br> colors::terminal.ansiRed <br> colors::terminalCommandDecoration.errorBackground <br> tokenColors::scope::markup.deleted.diff::foreground |
| #E2787820 | ![](https://via.placeholder.com/16/E2787820/FFFFFF/?text=%20) | colors::diffEditor.removedTextBackground |
| #E278784D | ![](https://via.placeholder.com/16/E278784D/FFFFFF/?text=%20) | colors::debugIcon.disconnectForeground |
| #E2787880 | ![](https://via.placeholder.com/16/E2787880/FFFFFF/?text=%20) | colors::editorGutter.deletedBackground <br> colors::editorOverviewRuler.deletedForeground |
| #E2A478 | ![](https://via.placeholder.com/16/E2A478/FFFFFF/?text=%20) | colors::debugConsole.warningForeground <br> colors::debugIcon.breakpointCurrentStackframeForeground <br> colors::editorBracketHighlight.foreground4 <br> colors::editorLightBulb.foreground <br> colors::editorWarning.foreground <br> colors::gitDecoration.conflictingResourceForeground <br> colors::list.warningForeground <br> colors::notificationsWarningIcon.foreground <br> colors::problemsWarningIcon.foreground <br> colors::symbolIcon.classForeground <br> colors::symbolIcon.constructorForeground <br> colors::symbolIcon.enumeratorForeground <br> colors::symbolIcon.eventForeground <br> colors::terminal.ansiYellow <br> tokenColors::scope::entity.name.section::foreground <br> tokenColors::scope::entity.name.function.method::foreground <br> tokenColors::scope::markup.heading::foreground <br> tokenColors::scope::meta.definition.method::foreground <br> tokenColors::scope::keyword.other.important.scss::foreground |
| #E2A4781A | ![](https://via.placeholder.com/16/E2A4781A/FFFFFF/?text=%20) | colors::editor.rangeHighlightBackground |
| #E2A47840 | ![](https://via.placeholder.com/16/E2A47840/FFFFFF/?text=%20) | colors::editor.findMatchHighlightBackground <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.matchHighlightBackground |
| #E2A47880 | ![](https://via.placeholder.com/16/E2A47880/FFFFFF/?text=%20) | colors::editor.findMatchBackground <br> colors::editorOverviewRuler.warningForeground |
| #E98989 | ![](https://via.placeholder.com/16/E98989/FFFFFF/?text=%20) | colors::terminal.ansiBrightRed |
| #E9B189 | ![](https://via.placeholder.com/16/E9B189/FFFFFF/?text=%20) | colors::terminal.ansiBrightYellow |






### solarized-light-color-theme.json


| color_code | palette | key_name |
| --- | --- | --- |
| #073642 | ![](https://via.placeholder.com/16/073642/FFFFFF/?text=%20)`#073642` | terminal.ansiBlack |
| #268bd2 | ![](https://via.placeholder.com/16/268bd2/FFFFFF/?text=%20)`#268bd2` | terminal.ansiBlue |
| #002b36 | ![](https://via.placeholder.com/16/002b36/FFFFFF/?text=%20)`#002b36` | terminal.ansiBrightBlack |
| #839496 | ![](https://via.placeholder.com/16/839496/FFFFFF/?text=%20)`#839496` | terminal.ansiBrightBlue |
| #93a1a1 | ![](https://via.placeholder.com/16/93a1a1/FFFFFF/?text=%20)`#93a1a1` | terminal.ansiBrightCyan |
| #586e75 | ![](https://via.placeholder.com/16/586e75/FFFFFF/?text=%20)`#586e75` | terminal.ansiBrightGreen |
| #6c71c4 | ![](https://via.placeholder.com/16/6c71c4/FFFFFF/?text=%20)`#6c71c4` | terminal.ansiBrightMagenta |
| #cb4b16 | ![](https://via.placeholder.com/16/cb4b16/FFFFFF/?text=%20)`#cb4b16` | terminal.ansiBrightRed |
| #fdf6e3 | ![](https://via.placeholder.com/16/fdf6e3/FFFFFF/?text=%20)`#fdf6e3` | terminal.ansiBrightWhite |
| #657b83 | ![](https://via.placeholder.com/16/657b83/FFFFFF/?text=%20)`#657b83` | terminal.ansiBrightYellow |
| #2aa198 | ![](https://via.placeholder.com/16/2aa198/FFFFFF/?text=%20)`#2aa198` | terminal.ansiCyan |
| #859900 | ![](https://via.placeholder.com/16/859900/FFFFFF/?text=%20)`#859900` | terminal.ansiGreen |
| #d33682 | ![](https://via.placeholder.com/16/d33682/FFFFFF/?text=%20)`#d33682` | terminal.ansiMagenta |
| #dc322f | ![](https://via.placeholder.com/16/dc322f/FFFFFF/?text=%20)`#dc322f` | terminal.ansiRed |
| #eee8d5 | ![](https://via.placeholder.com/16/eee8d5/FFFFFF/?text=%20)`#eee8d5` | terminal.ansiWhite |
| #b58900 | ![](https://via.placeholder.com/16/b58900/FFFFFF/?text=%20)`#b58900` | terminal.ansiYellow |
| #FDF6E3 | ![](https://via.placeholder.com/16/FDF6E3/FFFFFF/?text=%20)`#FDF6E3` | terminal.background |


### ayu-light-bordered.json


| color_code | palette | key_name |
| --- | --- | --- |
| #000000 | ![](https://via.placeholder.com/16/000000/FFFFFF/?text=%20)`#000000` | terminal.ansiBlack |
| #3199e1 | ![](https://via.placeholder.com/16/3199e1/FFFFFF/?text=%20)`#3199e1` | terminal.ansiBlue |
| #686868 | ![](https://via.placeholder.com/16/686868/FFFFFF/?text=%20)`#686868` | terminal.ansiBrightBlack |
| #399ee6 | ![](https://via.placeholder.com/16/399ee6/FFFFFF/?text=%20)`#399ee6` | terminal.ansiBrightBlue |
| #4cbf99 | ![](https://via.placeholder.com/16/4cbf99/FFFFFF/?text=%20)`#4cbf99` | terminal.ansiBrightCyan |
| #86b300 | ![](https://via.placeholder.com/16/86b300/FFFFFF/?text=%20)`#86b300` | terminal.ansiBrightGreen |
| #a37acc | ![](https://via.placeholder.com/16/a37acc/FFFFFF/?text=%20)`#a37acc` | terminal.ansiBrightMagenta |
| #f07171 | ![](https://via.placeholder.com/16/f07171/FFFFFF/?text=%20)`#f07171` | terminal.ansiBrightRed |
| #d1d1d1 | ![](https://via.placeholder.com/16/d1d1d1/FFFFFF/?text=%20)`#d1d1d1` | terminal.ansiBrightWhite |
| #f2ae49 | ![](https://via.placeholder.com/16/f2ae49/FFFFFF/?text=%20)`#f2ae49` | terminal.ansiBrightYellow |
| #46ba94 | ![](https://via.placeholder.com/16/46ba94/FFFFFF/?text=%20)`#46ba94` | terminal.ansiCyan |
| #6cbf43 | ![](https://via.placeholder.com/16/6cbf43/FFFFFF/?text=%20)`#6cbf43` | terminal.ansiGreen |
| #9e75c7 | ![](https://via.placeholder.com/16/9e75c7/FFFFFF/?text=%20)`#9e75c7` | terminal.ansiMagenta |
| #ea6c6d | ![](https://via.placeholder.com/16/ea6c6d/FFFFFF/?text=%20)`#ea6c6d` | terminal.ansiRed |
| #c7c7c7 | ![](https://via.placeholder.com/16/c7c7c7/FFFFFF/?text=%20)`#c7c7c7` | terminal.ansiWhite |
| #eca944 | ![](https://via.placeholder.com/16/eca944/FFFFFF/?text=%20)`#eca944` | terminal.ansiYellow |
| #f8f9fa | ![](https://via.placeholder.com/16/f8f9fa/FFFFFF/?text=%20)`#f8f9fa` | terminal.background |
| #5c6166 | ![](https://via.placeholder.com/16/5c6166/FFFFFF/?text=%20)`#5c6166` | terminal.foreground |


### iceberg-light.color-theme.json


| color_code | palette | key_name |
| --- | --- | --- |
| #dcdfe7 | ![](https://via.placeholder.com/16/dcdfe7/FFFFFF/?text=%20)`#dcdfe7` | terminal.ansiBlack |
| #2d539e | ![](https://via.placeholder.com/16/2d539e/FFFFFF/?text=%20)`#2d539e` | terminal.ansiBlue |
| #8389a3 | ![](https://via.placeholder.com/16/8389a3/FFFFFF/?text=%20)`#8389a3` | terminal.ansiBrightBlack |
| #22478e | ![](https://via.placeholder.com/16/22478e/FFFFFF/?text=%20)`#22478e` | terminal.ansiBrightBlue |
| #327698 | ![](https://via.placeholder.com/16/327698/FFFFFF/?text=%20)`#327698` | terminal.ansiBrightCyan |
| #598030 | ![](https://via.placeholder.com/16/598030/FFFFFF/?text=%20)`#598030` | terminal.ansiBrightGreen |
| #6845ad | ![](https://via.placeholder.com/16/6845ad/FFFFFF/?text=%20)`#6845ad` | terminal.ansiBrightMagenta |
| #cc3768 | ![](https://via.placeholder.com/16/cc3768/FFFFFF/?text=%20)`#cc3768` | terminal.ansiBrightRed |
| #262a3f | ![](https://via.placeholder.com/16/262a3f/FFFFFF/?text=%20)`#262a3f` | terminal.ansiBrightWhite |
| #b6662d | ![](https://via.placeholder.com/16/b6662d/FFFFFF/?text=%20)`#b6662d` | terminal.ansiBrightYellow |
| #3f83a6 | ![](https://via.placeholder.com/16/3f83a6/FFFFFF/?text=%20)`#3f83a6` | terminal.ansiCyan |
| #668e3d | ![](https://via.placeholder.com/16/668e3d/FFFFFF/?text=%20)`#668e3d` | terminal.ansiGreen |
| #7759b4 | ![](https://via.placeholder.com/16/7759b4/FFFFFF/?text=%20)`#7759b4` | terminal.ansiMagenta |
| #cc517a | ![](https://via.placeholder.com/16/cc517a/FFFFFF/?text=%20)`#cc517a` | terminal.ansiRed |
| #33374c | ![](https://via.placeholder.com/16/33374c/FFFFFF/?text=%20)`#33374c` | terminal.ansiWhite |
| #c57339 | ![](https://via.placeholder.com/16/c57339/FFFFFF/?text=%20)`#c57339` | terminal.ansiYellow |
| #33374c | ![](https://via.placeholder.com/16/33374c/FFFFFF/?text=%20)`#33374c` | terminal.foreground |
| #aeb2c666 | ![](https://via.placeholder.com/16/aeb2c666/FFFFFF/?text=%20)`#aeb2c666` | terminal.selectionBackground |
| #8389a3 | ![](https://via.placeholder.com/16/8389a3/FFFFFF/?text=%20)`#8389a3` | terminalCommandDecoration.defaultBackground |
| #cc517a | ![](https://via.placeholder.com/16/cc517a/FFFFFF/?text=%20)`#cc517a` | terminalCommandDecoration.errorBackground |
| #2d539e | ![](https://via.placeholder.com/16/2d539e/FFFFFF/?text=%20)`#2d539e` | terminalCommandDecoration.successBackground |


### dracula.json


| color_code | palette | key_name |
| --- | --- | --- |
| #21222C | ![](https://via.placeholder.com/16/21222C/FFFFFF/?text=%20)`#21222C` | terminal.ansiBlack |
| #BD93F9 | ![](https://via.placeholder.com/16/BD93F9/FFFFFF/?text=%20)`#BD93F9` | terminal.ansiBlue |
| #6272A4 | ![](https://via.placeholder.com/16/6272A4/FFFFFF/?text=%20)`#6272A4` | terminal.ansiBrightBlack |
| #D6ACFF | ![](https://via.placeholder.com/16/D6ACFF/FFFFFF/?text=%20)`#D6ACFF` | terminal.ansiBrightBlue |
| #A4FFFF | ![](https://via.placeholder.com/16/A4FFFF/FFFFFF/?text=%20)`#A4FFFF` | terminal.ansiBrightCyan |
| #69FF94 | ![](https://via.placeholder.com/16/69FF94/FFFFFF/?text=%20)`#69FF94` | terminal.ansiBrightGreen |
| #FF92DF | ![](https://via.placeholder.com/16/FF92DF/FFFFFF/?text=%20)`#FF92DF` | terminal.ansiBrightMagenta |
| #FF6E6E | ![](https://via.placeholder.com/16/FF6E6E/FFFFFF/?text=%20)`#FF6E6E` | terminal.ansiBrightRed |
| #FFFFFF | ![](https://via.placeholder.com/16/FFFFFF/FFFFFF/?text=%20)`#FFFFFF` | terminal.ansiBrightWhite |
| #FFFFA5 | ![](https://via.placeholder.com/16/FFFFA5/FFFFFF/?text=%20)`#FFFFA5` | terminal.ansiBrightYellow |
| #8BE9FD | ![](https://via.placeholder.com/16/8BE9FD/FFFFFF/?text=%20)`#8BE9FD` | terminal.ansiCyan |
| #50FA7B | ![](https://via.placeholder.com/16/50FA7B/FFFFFF/?text=%20)`#50FA7B` | terminal.ansiGreen |
| #FF79C6 | ![](https://via.placeholder.com/16/FF79C6/FFFFFF/?text=%20)`#FF79C6` | terminal.ansiMagenta |
| #FF5555 | ![](https://via.placeholder.com/16/FF5555/FFFFFF/?text=%20)`#FF5555` | terminal.ansiRed |
| #F8F8F2 | ![](https://via.placeholder.com/16/F8F8F2/FFFFFF/?text=%20)`#F8F8F2` | terminal.ansiWhite |
| #F1FA8C | ![](https://via.placeholder.com/16/F1FA8C/FFFFFF/?text=%20)`#F1FA8C` | terminal.ansiYellow |
| #282A36 | ![](https://via.placeholder.com/16/282A36/FFFFFF/?text=%20)`#282A36` | terminal.background |
| #F8F8F2 | ![](https://via.placeholder.com/16/F8F8F2/FFFFFF/?text=%20)`#F8F8F2` | terminal.foreground |


### iceberg.color-theme.json


| color_code | palette | key_name |
| --- | --- | --- |
| #1e2132 | ![](https://via.placeholder.com/16/1e2132/FFFFFF/?text=%20)`#1e2132` | terminal.ansiBlack |
| #84a0c6 | ![](https://via.placeholder.com/16/84a0c6/FFFFFF/?text=%20)`#84a0c6` | terminal.ansiBlue |
| #6b7089 | ![](https://via.placeholder.com/16/6b7089/FFFFFF/?text=%20)`#6b7089` | terminal.ansiBrightBlack |
| #91acd1 | ![](https://via.placeholder.com/16/91acd1/FFFFFF/?text=%20)`#91acd1` | terminal.ansiBrightBlue |
| #95c4ce | ![](https://via.placeholder.com/16/95c4ce/FFFFFF/?text=%20)`#95c4ce` | terminal.ansiBrightCyan |
| #c0ca8e | ![](https://via.placeholder.com/16/c0ca8e/FFFFFF/?text=%20)`#c0ca8e` | terminal.ansiBrightGreen |
| #ada0d3 | ![](https://via.placeholder.com/16/ada0d3/FFFFFF/?text=%20)`#ada0d3` | terminal.ansiBrightMagenta |
| #e98989 | ![](https://via.placeholder.com/16/e98989/FFFFFF/?text=%20)`#e98989` | terminal.ansiBrightRed |
| #d2d4de | ![](https://via.placeholder.com/16/d2d4de/FFFFFF/?text=%20)`#d2d4de` | terminal.ansiBrightWhite |
| #e9b189 | ![](https://via.placeholder.com/16/e9b189/FFFFFF/?text=%20)`#e9b189` | terminal.ansiBrightYellow |
| #89b8c2 | ![](https://via.placeholder.com/16/89b8c2/FFFFFF/?text=%20)`#89b8c2` | terminal.ansiCyan |
| #b4be82 | ![](https://via.placeholder.com/16/b4be82/FFFFFF/?text=%20)`#b4be82` | terminal.ansiGreen |
| #a093c7 | ![](https://via.placeholder.com/16/a093c7/FFFFFF/?text=%20)`#a093c7` | terminal.ansiMagenta |
| #e27878 | ![](https://via.placeholder.com/16/e27878/FFFFFF/?text=%20)`#e27878` | terminal.ansiRed |
| #c6c8d1 | ![](https://via.placeholder.com/16/c6c8d1/FFFFFF/?text=%20)`#c6c8d1` | terminal.ansiWhite |
| #e2a478 | ![](https://via.placeholder.com/16/e2a478/FFFFFF/?text=%20)`#e2a478` | terminal.ansiYellow |
| #c6c8d1 | ![](https://via.placeholder.com/16/c6c8d1/FFFFFF/?text=%20)`#c6c8d1` | terminal.foreground |
| #4a548266 | ![](https://via.placeholder.com/16/4a548266/FFFFFF/?text=%20)`#4a548266` | terminal.selectionBackground |
| #6b7089 | ![](https://via.placeholder.com/16/6b7089/FFFFFF/?text=%20)`#6b7089` | terminalCommandDecoration.defaultBackground |
| #e27878 | ![](https://via.placeholder.com/16/e27878/FFFFFF/?text=%20)`#e27878` | terminalCommandDecoration.errorBackground |
| #84a0c6 | ![](https://via.placeholder.com/16/84a0c6/FFFFFF/?text=%20)`#84a0c6` | terminalCommandDecoration.successBackground |


### ayu-light.json


| color_code | palette | key_name |
| --- | --- | --- |
| #000000 | ![](https://via.placeholder.com/16/000000/FFFFFF/?text=%20)`#000000` | terminal.ansiBlack |
| #3199e1 | ![](https://via.placeholder.com/16/3199e1/FFFFFF/?text=%20)`#3199e1` | terminal.ansiBlue |
| #686868 | ![](https://via.placeholder.com/16/686868/FFFFFF/?text=%20)`#686868` | terminal.ansiBrightBlack |
| #399ee6 | ![](https://via.placeholder.com/16/399ee6/FFFFFF/?text=%20)`#399ee6` | terminal.ansiBrightBlue |
| #4cbf99 | ![](https://via.placeholder.com/16/4cbf99/FFFFFF/?text=%20)`#4cbf99` | terminal.ansiBrightCyan |
| #86b300 | ![](https://via.placeholder.com/16/86b300/FFFFFF/?text=%20)`#86b300` | terminal.ansiBrightGreen |
| #a37acc | ![](https://via.placeholder.com/16/a37acc/FFFFFF/?text=%20)`#a37acc` | terminal.ansiBrightMagenta |
| #f07171 | ![](https://via.placeholder.com/16/f07171/FFFFFF/?text=%20)`#f07171` | terminal.ansiBrightRed |
| #d1d1d1 | ![](https://via.placeholder.com/16/d1d1d1/FFFFFF/?text=%20)`#d1d1d1` | terminal.ansiBrightWhite |
| #f2ae49 | ![](https://via.placeholder.com/16/f2ae49/FFFFFF/?text=%20)`#f2ae49` | terminal.ansiBrightYellow |
| #46ba94 | ![](https://via.placeholder.com/16/46ba94/FFFFFF/?text=%20)`#46ba94` | terminal.ansiCyan |
| #6cbf43 | ![](https://via.placeholder.com/16/6cbf43/FFFFFF/?text=%20)`#6cbf43` | terminal.ansiGreen |
| #9e75c7 | ![](https://via.placeholder.com/16/9e75c7/FFFFFF/?text=%20)`#9e75c7` | terminal.ansiMagenta |
| #ea6c6d | ![](https://via.placeholder.com/16/ea6c6d/FFFFFF/?text=%20)`#ea6c6d` | terminal.ansiRed |
| #c7c7c7 | ![](https://via.placeholder.com/16/c7c7c7/FFFFFF/?text=%20)`#c7c7c7` | terminal.ansiWhite |
| #eca944 | ![](https://via.placeholder.com/16/eca944/FFFFFF/?text=%20)`#eca944` | terminal.ansiYellow |
| #f8f9fa | ![](https://via.placeholder.com/16/f8f9fa/FFFFFF/?text=%20)`#f8f9fa` | terminal.background |
| #5c6166 | ![](https://via.placeholder.com/16/5c6166/FFFFFF/?text=%20)`#5c6166` | terminal.foreground |


### nord-color-theme.json


| color_code | palette | key_name |
| --- | --- | --- |
| #3b4252 | ![](https://via.placeholder.com/16/3b4252/FFFFFF/?text=%20)`#3b4252` | terminal.ansiBlack |
| #81a1c1 | ![](https://via.placeholder.com/16/81a1c1/FFFFFF/?text=%20)`#81a1c1` | terminal.ansiBlue |
| #4c566a | ![](https://via.placeholder.com/16/4c566a/FFFFFF/?text=%20)`#4c566a` | terminal.ansiBrightBlack |
| #81a1c1 | ![](https://via.placeholder.com/16/81a1c1/FFFFFF/?text=%20)`#81a1c1` | terminal.ansiBrightBlue |
| #8fbcbb | ![](https://via.placeholder.com/16/8fbcbb/FFFFFF/?text=%20)`#8fbcbb` | terminal.ansiBrightCyan |
| #a3be8c | ![](https://via.placeholder.com/16/a3be8c/FFFFFF/?text=%20)`#a3be8c` | terminal.ansiBrightGreen |
| #b48ead | ![](https://via.placeholder.com/16/b48ead/FFFFFF/?text=%20)`#b48ead` | terminal.ansiBrightMagenta |
| #bf616a | ![](https://via.placeholder.com/16/bf616a/FFFFFF/?text=%20)`#bf616a` | terminal.ansiBrightRed |
| #eceff4 | ![](https://via.placeholder.com/16/eceff4/FFFFFF/?text=%20)`#eceff4` | terminal.ansiBrightWhite |
| #ebcb8b | ![](https://via.placeholder.com/16/ebcb8b/FFFFFF/?text=%20)`#ebcb8b` | terminal.ansiBrightYellow |
| #88c0d0 | ![](https://via.placeholder.com/16/88c0d0/FFFFFF/?text=%20)`#88c0d0` | terminal.ansiCyan |
| #a3be8c | ![](https://via.placeholder.com/16/a3be8c/FFFFFF/?text=%20)`#a3be8c` | terminal.ansiGreen |
| #b48ead | ![](https://via.placeholder.com/16/b48ead/FFFFFF/?text=%20)`#b48ead` | terminal.ansiMagenta |
| #bf616a | ![](https://via.placeholder.com/16/bf616a/FFFFFF/?text=%20)`#bf616a` | terminal.ansiRed |
| #e5e9f0 | ![](https://via.placeholder.com/16/e5e9f0/FFFFFF/?text=%20)`#e5e9f0` | terminal.ansiWhite |
| #ebcb8b | ![](https://via.placeholder.com/16/ebcb8b/FFFFFF/?text=%20)`#ebcb8b` | terminal.ansiYellow |
| #2e3440 | ![](https://via.placeholder.com/16/2e3440/FFFFFF/?text=%20)`#2e3440` | terminal.background |
| #d8dee9 | ![](https://via.placeholder.com/16/d8dee9/FFFFFF/?text=%20)`#d8dee9` | terminal.foreground |
| #88c0d0 | ![](https://via.placeholder.com/16/88c0d0/FFFFFF/?text=%20)`#88c0d0` | terminal.tab.activeBorder |




## VSCode color theme 共通key 探し


| name | keys |
| --- | --- |
| primary | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.selectionBackground <br> colors::editorGroup.border <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::progressBar.background <br> colors::selection.background <br> colors::sideBar.background <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::tab.activeBackground <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::titleBar.activeBackground <br> tokenColors::[]scope>comment <br> tokenColors::[]scope>entity.name.function <br> tokenColors::[]scope>entity.name.tag <br> tokenColors::[]scope>entity.other.attribute-name <br> tokenColors::[]scope>keyword <br> tokenColors::[]scope>markup.bold <br> tokenColors::[]scope>markup.heading <br> tokenColors::[]scope>storage <br> tokenColors::[]scope>string <br> tokenColors::[]scope>support.constant <br> tokenColors::[]settings::fontStyle <br> tokenColors::[]settings::foreground |
| solarized-light-color-theme.json | colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::editor.lineHighlightBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.dropBackground <br> colors::editorLineNumber.activeForeground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::ports.iconRunningProcessForeground <br> colors::quickInputList.focusBackground <br> colors::sideBarTitle.foreground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.lastPinnedBorder <br> colors::terminal.background <br> colors::walkThrough.embeddedEditorBackground <br> name <br> semanticHighlighting <br> tokenColors::[]name <br> tokenColors::[]scope>constant.character <br> tokenColors::[]scope>constant.language <br> tokenColors::[]scope>constant.numeric <br> tokenColors::[]scope>constant.other <br> tokenColors::[]scope>entity.name.class <br> tokenColors::[]scope>entity.name.namespace <br> tokenColors::[]scope>entity.name.scope-resolution <br> tokenColors::[]scope>entity.name.type <br> tokenColors::[]scope>entity.other.inherited-class <br> tokenColors::[]scope>invalid <br> tokenColors::[]scope>keyword.other.new <br> tokenColors::[]scope>markup.changed <br> tokenColors::[]scope>markup.deleted <br> tokenColors::[]scope>markup.heading.setext <br> tokenColors::[]scope>markup.inline.raw <br> tokenColors::[]scope>markup.inserted <br> tokenColors::[]scope>markup.italic <br> tokenColors::[]scope>markup.list <br> tokenColors::[]scope>markup.quote <br> tokenColors::[]scope>markup.strikethrough <br> tokenColors::[]scope>meta.diff <br> tokenColors::[]scope>meta.diff.header <br> tokenColors::[]scope>meta.embedded <br> tokenColors::[]scope>meta.preprocessor <br> tokenColors::[]scope>punctuation.definition.tag <br> tokenColors::[]scope>punctuation.definition.variable <br> tokenColors::[]scope>punctuation.section.embedded.begin <br> tokenColors::[]scope>punctuation.section.embedded.end <br> tokenColors::[]scope>punctuation.separator.continuation <br> tokenColors::[]scope>source.groovy.embedded <br> tokenColors::[]scope>string meta.image.inline.markdown <br> tokenColors::[]scope>string.regexp <br> tokenColors::[]scope>support.class <br> tokenColors::[]scope>support.function <br> tokenColors::[]scope>support.function.construct <br> tokenColors::[]scope>support.other.variable <br> tokenColors::[]scope>support.type <br> tokenColors::[]scope>support.type.exception <br> tokenColors::[]scope>support.variable <br> tokenColors::[]scope>variable.language <br> tokenColors::[]scope>variable.legacy.builtin.python <br> tokenColors::[]scope>variable.other <br> tokenColors::[]scope>variable.parameter |
| ayu-light-bordered.json | colors::activityBar.activeBorder <br> colors::activityBar.border <br> colors::activityBar.inactiveForeground <br> colors::activityBarBadge.foreground <br> colors::badge.foreground <br> colors::button.foreground <br> colors::button.hoverBackground <br> colors::button.secondaryBackground <br> colors::button.secondaryForeground <br> colors::button.secondaryHoverBackground <br> colors::debugConsoleInputIcon.foreground <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugIcon.breakpointDisabledForeground <br> colors::debugIcon.breakpointForeground <br> colors::descriptionForeground <br> colors::diffEditor.diagonalFill <br> colors::diffEditor.insertedTextBackground <br> colors::diffEditor.removedTextBackground <br> colors::dropdown.foreground <br> colors::editor.findMatchBackground <br> colors::editor.findMatchBorder <br> colors::editor.findMatchHighlightBackground <br> colors::editor.findMatchHighlightBorder <br> colors::editor.findRangeHighlightBackground <br> colors::editor.inactiveSelectionBackground <br> colors::editor.lineHighlightBackground <br> colors::editor.rangeHighlightBackground <br> colors::editor.selectionHighlightBackground <br> colors::editor.selectionHighlightBorder <br> colors::editor.snippetTabstopHighlightBackground <br> colors::editor.wordHighlightBackground <br> colors::editor.wordHighlightBorder <br> colors::editor.wordHighlightStrongBackground <br> colors::editor.wordHighlightStrongBorder <br> colors::editorBracketMatch.background <br> colors::editorBracketMatch.border <br> colors::editorCodeLens.foreground <br> colors::editorCursor.foreground <br> colors::editorError.foreground <br> colors::editorGroup.background <br> colors::editorGroupHeader.noTabsBackground <br> colors::editorGroupHeader.tabsBorder <br> colors::editorGutter.addedBackground <br> colors::editorGutter.deletedBackground <br> colors::editorGutter.modifiedBackground <br> colors::editorHoverWidget.border <br> colors::editorLineNumber.activeForeground <br> colors::editorLineNumber.foreground <br> colors::editorLink.activeForeground <br> colors::editorMarkerNavigation.background <br> colors::editorOverviewRuler.addedForeground <br> colors::editorOverviewRuler.border <br> colors::editorOverviewRuler.bracketMatchForeground <br> colors::editorOverviewRuler.deletedForeground <br> colors::editorOverviewRuler.errorForeground <br> colors::editorOverviewRuler.findMatchForeground <br> colors::editorOverviewRuler.modifiedForeground <br> colors::editorOverviewRuler.warningForeground <br> colors::editorOverviewRuler.wordHighlightForeground <br> colors::editorOverviewRuler.wordHighlightStrongForeground <br> colors::editorRuler.foreground <br> colors::editorSuggestWidget.background <br> colors::editorSuggestWidget.border <br> colors::editorSuggestWidget.highlightForeground <br> colors::editorSuggestWidget.selectedBackground <br> colors::editorWarning.foreground <br> colors::editorWidget.border <br> colors::errorForeground <br> colors::extensionButton.prominentForeground <br> colors::foreground <br> colors::gitDecoration.conflictingResourceForeground <br> colors::gitDecoration.deletedResourceForeground <br> colors::gitDecoration.ignoredResourceForeground <br> colors::gitDecoration.modifiedResourceForeground <br> colors::gitDecoration.submoduleResourceForeground <br> colors::gitDecoration.untrackedResourceForeground <br> colors::icon.foreground <br> colors::input.border <br> colors::inputOption.activeBackground <br> colors::inputOption.activeForeground <br> colors::inputValidation.errorBackground <br> colors::inputValidation.errorBorder <br> colors::inputValidation.infoBackground <br> colors::inputValidation.infoBorder <br> colors::inputValidation.warningBackground <br> colors::inputValidation.warningBorder <br> colors::keybindingLabel.background <br> colors::keybindingLabel.border <br> colors::keybindingLabel.bottomBorder <br> colors::keybindingLabel.foreground <br> colors::list.deemphasizedForeground <br> colors::list.errorForeground <br> colors::list.filterMatchBackground <br> colors::list.filterMatchBorder <br> colors::list.focusBackground <br> colors::list.focusForeground <br> colors::list.focusOutline <br> colors::list.inactiveSelectionForeground <br> colors::list.invalidItemForeground <br> colors::listFilterWidget.background <br> colors::listFilterWidget.noMatchesOutline <br> colors::listFilterWidget.outline <br> colors::minimap.background <br> colors::minimap.errorHighlight <br> colors::minimap.findMatchHighlight <br> colors::minimap.selectionHighlight <br> colors::minimapGutter.addedBackground <br> colors::minimapGutter.deletedBackground <br> colors::minimapGutter.modifiedBackground <br> colors::panel.background <br> colors::panelTitle.activeBorder <br> colors::panelTitle.activeForeground <br> colors::panelTitle.inactiveForeground <br> colors::peekViewEditor.matchHighlightBorder <br> colors::peekViewResult.fileForeground <br> colors::peekViewResult.lineForeground <br> colors::peekViewResult.matchHighlightBackground <br> colors::peekViewResult.selectionBackground <br> colors::peekViewTitleDescription.foreground <br> colors::peekViewTitleLabel.foreground <br> colors::scrollbar.shadow <br> colors::scrollbarSlider.activeBackground <br> colors::scrollbarSlider.background <br> colors::scrollbarSlider.hoverBackground <br> colors::settings.headerForeground <br> colors::settings.modifiedItemIndicator <br> colors::sideBar.border <br> colors::sideBarSectionHeader.background <br> colors::sideBarSectionHeader.border <br> colors::sideBarSectionHeader.foreground <br> colors::sideBarTitle.foreground <br> colors::statusBar.border <br> colors::statusBar.debuggingForeground <br> colors::statusBarItem.activeBackground <br> colors::statusBarItem.hoverBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::statusBarItem.remoteForeground <br> colors::tab.activeBorder <br> colors::tab.activeBorderTop <br> colors::tab.activeForeground <br> colors::tab.unfocusedActiveBorderTop <br> colors::tab.unfocusedActiveForeground <br> colors::tab.unfocusedInactiveForeground <br> colors::terminal.background <br> colors::terminal.foreground <br> colors::textBlockQuote.background <br> colors::textLink.activeForeground <br> colors::textLink.foreground <br> colors::textPreformat.foreground <br> colors::titleBar.activeForeground <br> colors::titleBar.border <br> colors::titleBar.inactiveBackground <br> colors::titleBar.inactiveForeground <br> colors::tree.indentGuidesStroke <br> colors::walkThrough.embeddedEditorBackground <br> colors::welcomePage.buttonBackground <br> colors::welcomePage.progress.background <br> colors::welcomePage.tileBackground <br> colors::welcomePage.tileShadow <br> colors::widget.shadow <br> semanticHighlighting <br> semanticTokenColors::parameter.label <br> tokenColors::[]name <br> tokenColors::[]scope>constant.character <br> tokenColors::[]scope>constant.language <br> tokenColors::[]scope>constant.numeric <br> tokenColors::[]scope>constant.numeric.line-number.find-in-files - match <br> tokenColors::[]scope>constant.numeric.line-number.match <br> tokenColors::[]scope>constant.other <br> tokenColors::[]scope>constant.other.symbol <br> tokenColors::[]scope>entity.name <br> tokenColors::[]scope>entity.name.filename.find-in-files <br> tokenColors::[]scope>entity.name.import <br> tokenColors::[]scope>entity.name.package <br> tokenColors::[]scope>entity.other.inherited-class <br> tokenColors::[]scope>invalid <br> tokenColors::[]scope>keyword.operator <br> tokenColors::[]scope>markup.bold markup.italic <br> tokenColors::[]scope>markup.changed <br> tokenColors::[]scope>markup.deleted <br> tokenColors::[]scope>markup.heading entity.name <br> tokenColors::[]scope>markup.inserted <br> tokenColors::[]scope>markup.italic <br> tokenColors::[]scope>markup.italic markup.bold <br> tokenColors::[]scope>markup.list punctuation.definition.list.begin <br> tokenColors::[]scope>markup.quote <br> tokenColors::[]scope>markup.raw <br> tokenColors::[]scope>markup.raw.inline <br> tokenColors::[]scope>markup.strike <br> tokenColors::[]scope>markup.table <br> tokenColors::[]scope>markup.underline.link <br> tokenColors::[]scope>message.error <br> tokenColors::[]scope>meta.decorator punctuation.decorator <br> tokenColors::[]scope>meta.decorator variable.other <br> tokenColors::[]scope>meta.diff <br> tokenColors::[]scope>meta.diff.header <br> tokenColors::[]scope>meta.embedded <br> tokenColors::[]scope>meta.function-call.generic <br> tokenColors::[]scope>meta.parameter <br> tokenColors::[]scope>meta.separator <br> tokenColors::[]scope>meta.tag.sgml <br> tokenColors::[]scope>punctuation.accessor <br> tokenColors::[]scope>punctuation.definition.markdown <br> tokenColors::[]scope>punctuation.definition.tag <br> tokenColors::[]scope>punctuation.definition.tag.begin <br> tokenColors::[]scope>punctuation.definition.tag.end <br> tokenColors::[]scope>punctuation.definition.template-expression <br> tokenColors::[]scope>punctuation.section <br> tokenColors::[]scope>punctuation.section.embedded <br> tokenColors::[]scope>punctuation.separator <br> tokenColors::[]scope>punctuation.terminator <br> tokenColors::[]scope>source.c storage.type <br> tokenColors::[]scope>source.css entity.name.tag <br> tokenColors::[]scope>source.css support.type <br> tokenColors::[]scope>source.go storage.type <br> tokenColors::[]scope>source.haskell storage.type <br> tokenColors::[]scope>source.java storage.type <br> tokenColors::[]scope>source.java storage.type.primitive <br> tokenColors::[]scope>source.less entity.name.tag <br> tokenColors::[]scope>source.less support.type <br> tokenColors::[]scope>source.ruby variable.other.readwrite <br> tokenColors::[]scope>source.sass entity.name.tag <br> tokenColors::[]scope>source.sass support.type <br> tokenColors::[]scope>source.scss entity.name.tag <br> tokenColors::[]scope>source.scss support.type <br> tokenColors::[]scope>source.stylus entity.name.tag <br> tokenColors::[]scope>source.stylus support.type <br> tokenColors::[]scope>storage.type.annotation <br> tokenColors::[]scope>storage.type.function <br> tokenColors::[]scope>string.other.link <br> tokenColors::[]scope>string.regexp <br> tokenColors::[]scope>support.class <br> tokenColors::[]scope>support.class.component <br> tokenColors::[]scope>support.function <br> tokenColors::[]scope>support.function.go <br> tokenColors::[]scope>support.macro <br> tokenColors::[]scope>support.type <br> tokenColors::[]scope>support.type.property-name <br> tokenColors::[]scope>text.html.markdown markup.inline.raw <br> tokenColors::[]scope>text.html.markdown meta.dummy.line-break <br> tokenColors::[]scope>variable <br> tokenColors::[]scope>variable.annotation <br> tokenColors::[]scope>variable.function <br> tokenColors::[]scope>variable.language <br> tokenColors::[]scope>variable.member <br> tokenColors::[]scope>variable.parameter <br> tokenColors::[]scope>variable.parameter.function-call <br> tokenColors::[]settings::background <br> type |
| iceberg-light.color-theme.json | colors::activityBar.inactiveForeground <br> colors::activityBarBadge.foreground <br> colors::badge.foreground <br> colors::breadcrumb.activeSelectionForeground <br> colors::breadcrumb.background <br> colors::breadcrumb.focusForeground <br> colors::breadcrumb.foreground <br> colors::breadcrumbPicker.background <br> colors::button.foreground <br> colors::button.hoverBackground <br> colors::debugConsole.errorForeground <br> colors::debugConsole.infoForeground <br> colors::debugConsole.sourceForeground <br> colors::debugConsole.warningForeground <br> colors::debugConsoleInputIcon.foreground <br> colors::debugIcon.breakpointCurrentStackframeForeground <br> colors::debugIcon.breakpointDisabledForeground <br> colors::debugIcon.breakpointForeground <br> colors::debugIcon.breakpointStackframeForeground <br> colors::debugIcon.breakpointUnverifiedForeground <br> colors::debugIcon.continueForeground <br> colors::debugIcon.disconnectForeground <br> colors::debugIcon.pauseForeground <br> colors::debugIcon.restartForeground <br> colors::debugIcon.startForeground <br> colors::debugIcon.stepBackForeground <br> colors::debugIcon.stepIntoForeground <br> colors::debugIcon.stepOutForeground <br> colors::debugIcon.stepOverForeground <br> colors::debugIcon.stopForeground <br> colors::debugTokenExpression.boolean <br> colors::debugTokenExpression.error <br> colors::debugTokenExpression.name <br> colors::debugTokenExpression.number <br> colors::debugTokenExpression.string <br> colors::debugTokenExpression.value <br> colors::descriptionForeground <br> colors::diffEditor.insertedTextBackground <br> colors::diffEditor.removedTextBackground <br> colors::dropdown.foreground <br> colors::editor.findMatchBackground <br> colors::editor.findMatchHighlightBackground <br> colors::editor.foldBackground <br> colors::editor.lineHighlightBackground <br> colors::editor.rangeHighlightBackground <br> colors::editor.wordHighlightBackground <br> colors::editor.wordHighlightStrongBackground <br> colors::editorBracketHighlight.foreground1 <br> colors::editorBracketHighlight.foreground2 <br> colors::editorBracketHighlight.foreground3 <br> colors::editorBracketHighlight.foreground4 <br> colors::editorBracketHighlight.foreground5 <br> colors::editorBracketHighlight.foreground6 <br> colors::editorBracketHighlight.unexpectedBracket.foreground <br> colors::editorBracketMatch.background <br> colors::editorBracketMatch.border <br> colors::editorCursor.foreground <br> colors::editorError.foreground <br> colors::editorGroup.dropBackground <br> colors::editorGutter.addedBackground <br> colors::editorGutter.background <br> colors::editorGutter.deletedBackground <br> colors::editorGutter.modifiedBackground <br> colors::editorHoverWidget.border <br> colors::editorHoverWidget.foreground <br> colors::editorHoverWidget.statusBarBackground <br> colors::editorLightBulb.foreground <br> colors::editorLightBulbAutoFix.foreground <br> colors::editorLineNumber.activeForeground <br> colors::editorLineNumber.foreground <br> colors::editorLink.activeForeground <br> colors::editorMarkerNavigation.background <br> colors::editorOverviewRuler.addedForeground <br> colors::editorOverviewRuler.border <br> colors::editorOverviewRuler.deletedForeground <br> colors::editorOverviewRuler.errorForeground <br> colors::editorOverviewRuler.infoForeground <br> colors::editorOverviewRuler.modifiedForeground <br> colors::editorOverviewRuler.warningForeground <br> colors::editorOverviewRuler.wordHighlightForeground <br> colors::editorRuler.foreground <br> colors::editorSuggestWidget.selectedBackground <br> colors::editorWarning.foreground <br> colors::editorWidget.border <br> colors::extensionButton.prominentForeground <br> colors::foreground <br> colors::gitDecoration.addedResourceForeground <br> colors::gitDecoration.conflictingResourceForeground <br> colors::gitDecoration.deletedResourceForeground <br> colors::gitDecoration.ignoredResourceForeground <br> colors::gitDecoration.modifiedResourceForeground <br> colors::gitDecoration.renamedResourceForeground <br> colors::gitDecoration.stageDeletedResourceForeground <br> colors::gitDecoration.stageModifiedResourceForeground <br> colors::gitDecoration.submoduleResourceForeground <br> colors::gitDecoration.untrackedResourceForeground <br> colors::inputValidation.errorBackground <br> colors::inputValidation.errorBorder <br> colors::list.dropBackground <br> colors::list.errorForeground <br> colors::list.focusForeground <br> colors::list.warningForeground <br> colors::menu.background <br> colors::menu.foreground <br> colors::menu.selectionBackground <br> colors::menu.selectionForeground <br> colors::menu.separatorBackground <br> colors::menubar.selectionBackground <br> colors::menubar.selectionForeground <br> colors::merge.currentContentBackground <br> colors::merge.currentHeaderBackground <br> colors::merge.incomingContentBackground <br> colors::merge.incomingHeaderBackground <br> colors::notificationCenterHeader.background <br> colors::notifications.background <br> colors::notifications.border <br> colors::notifications.foreground <br> colors::notificationsErrorIcon.foreground <br> colors::notificationsInfoIcon.foreground <br> colors::notificationsWarningIcon.foreground <br> colors::panel.background <br> colors::panelTitle.activeForeground <br> colors::panelTitle.inactiveForeground <br> colors::peekViewEditorGutter.background <br> colors::peekViewResult.fileForeground <br> colors::peekViewResult.lineForeground <br> colors::peekViewResult.matchHighlightBackground <br> colors::peekViewResult.selectionBackground <br> colors::peekViewTitleDescription.foreground <br> colors::peekViewTitleLabel.foreground <br> colors::problemsErrorIcon.foreground <br> colors::problemsInfoIcon.foreground <br> colors::problemsWarningIcon.foreground <br> colors::quickInput.background <br> colors::quickInput.foreground <br> colors::quickInputList.focusBackground <br> colors::scrollbar.shadow <br> colors::scrollbarSlider.background <br> colors::scrollbarSlider.hoverBackground <br> colors::settings.headerForeground <br> colors::settings.modifiedItemIndicator <br> colors::sideBar.border <br> colors::sideBar.dropBackground <br> colors::sideBar.foreground <br> colors::sideBarSectionHeader.background <br> colors::sideBarSectionHeader.foreground <br> colors::statusBar.debuggingForeground <br> colors::statusBar.noFolderForeground <br> colors::statusBarItem.errorBackground <br> colors::statusBarItem.errorForeground <br> colors::statusBarItem.hoverBackground <br> colors::symbolIcon.classForeground <br> colors::symbolIcon.constructorForeground <br> colors::symbolIcon.enumeratorForeground <br> colors::symbolIcon.enumeratorMemberForeground <br> colors::symbolIcon.eventForeground <br> colors::symbolIcon.fieldForeground <br> colors::symbolIcon.functionForeground <br> colors::symbolIcon.interfaceForeground <br> colors::symbolIcon.methodForeground <br> colors::symbolIcon.variableForeground <br> colors::tab.activeForeground <br> colors::tab.activeModifiedBorder <br> colors::tab.hoverBackground <br> colors::tab.inactiveModifiedBorder <br> colors::tab.unfocusedActiveForeground <br> colors::tab.unfocusedInactiveForeground <br> colors::terminal.foreground <br> colors::terminal.selectionBackground <br> colors::terminalCommandDecoration.defaultBackground <br> colors::terminalCommandDecoration.errorBackground <br> colors::terminalCommandDecoration.successBackground <br> colors::textLink.activeForeground <br> colors::textLink.foreground <br> colors::titleBar.activeForeground <br> colors::titleBar.inactiveBackground <br> colors::titleBar.inactiveForeground <br> colors::tree.indentGuidesStroke <br> colors::widget.shadow <br> name <br> tokenColors::[]scope>constant <br> tokenColors::[]scope>entity.name.class <br> tokenColors::[]scope>entity.name.function.method <br> tokenColors::[]scope>entity.name.import.go <br> tokenColors::[]scope>entity.name.section <br> tokenColors::[]scope>entity.other.attribute-name.class.css, entity.other.attribute-name.parent-selector-suffix.css <br> tokenColors::[]scope>keyword.control.at-rule, keyword.control.content <br> tokenColors::[]scope>keyword.function <br> tokenColors::[]scope>keyword.operator <br> tokenColors::[]scope>keyword.operator.expression <br> tokenColors::[]scope>keyword.operator.new <br> tokenColors::[]scope>keyword.other.important.scss <br> tokenColors::[]scope>keyword.other.unit <br> tokenColors::[]scope>markup.deleted.diff <br> tokenColors::[]scope>markup.fenced_code.block <br> tokenColors::[]scope>markup.inline.raw.string <br> tokenColors::[]scope>markup.inserted.diff <br> tokenColors::[]scope>markup.underline.link <br> tokenColors::[]scope>meta.brace.square <br> tokenColors::[]scope>meta.definition.method <br> tokenColors::[]scope>meta.diff.header <br> tokenColors::[]scope>meta.diff.range <br> tokenColors::[]scope>meta.link <br> tokenColors::[]scope>meta.object-literal.key <br> tokenColors::[]scope>meta.tag.attributes <br> tokenColors::[]scope>meta.tag.sgml.doctype <br> tokenColors::[]scope>meta.type.annotation <br> tokenColors::[]scope>punctuation.definition.block <br> tokenColors::[]scope>punctuation.definition.block.tag.jsdoc <br> tokenColors::[]scope>punctuation.definition.tag <br> tokenColors::[]scope>punctuation.definition.template-expression <br> tokenColors::[]scope>storage.type.class.jsdoc <br> tokenColors::[]scope>storage.type.function <br> tokenColors::[]scope>support <br> tokenColors::[]scope>support.type.class.flowtype <br> tokenColors::[]scope>support.type.property-name <br> tokenColors::[]scope>text <br> tokenColors::[]scope>variable.interpolation.scss <br> tokenColors::[]scope>variable.language.this <br> tokenColors::[]scope>variable.other.jsdoc <br> tokenColors::[]scope>variable.scss |
| dracula.json | $schema <br> author <br> colors::activityBar.activeBackground <br> colors::activityBar.activeBorder <br> colors::activityBar.inactiveForeground <br> colors::activityBarBadge.foreground <br> colors::badge.foreground <br> colors::breadcrumb.activeSelectionForeground <br> colors::breadcrumb.background <br> colors::breadcrumb.focusForeground <br> colors::breadcrumb.foreground <br> colors::breadcrumbPicker.background <br> colors::button.foreground <br> colors::button.secondaryBackground <br> colors::button.secondaryForeground <br> colors::button.secondaryHoverBackground <br> colors::diffEditor.insertedTextBackground <br> colors::diffEditor.removedTextBackground <br> colors::dropdown.foreground <br> colors::editor.findMatchBackground <br> colors::editor.findMatchHighlightBackground <br> colors::editor.findRangeHighlightBackground <br> colors::editor.foldBackground <br> colors::editor.hoverHighlightBackground <br> colors::editor.lineHighlightBorder <br> colors::editor.rangeHighlightBackground <br> colors::editor.selectionHighlightBackground <br> colors::editor.snippetFinalTabstopHighlightBackground <br> colors::editor.snippetFinalTabstopHighlightBorder <br> colors::editor.snippetTabstopHighlightBackground <br> colors::editor.snippetTabstopHighlightBorder <br> colors::editor.wordHighlightBackground <br> colors::editor.wordHighlightStrongBackground <br> colors::editorBracketHighlight.foreground1 <br> colors::editorBracketHighlight.foreground2 <br> colors::editorBracketHighlight.foreground3 <br> colors::editorBracketHighlight.foreground4 <br> colors::editorBracketHighlight.foreground5 <br> colors::editorBracketHighlight.foreground6 <br> colors::editorBracketHighlight.unexpectedBracket.foreground <br> colors::editorCodeLens.foreground <br> colors::editorError.foreground <br> colors::editorGroup.dropBackground <br> colors::editorGutter.addedBackground <br> colors::editorGutter.deletedBackground <br> colors::editorGutter.modifiedBackground <br> colors::editorHoverWidget.border <br> colors::editorLineNumber.foreground <br> colors::editorLink.activeForeground <br> colors::editorMarkerNavigation.background <br> colors::editorOverviewRuler.addedForeground <br> colors::editorOverviewRuler.border <br> colors::editorOverviewRuler.currentContentForeground <br> colors::editorOverviewRuler.deletedForeground <br> colors::editorOverviewRuler.errorForeground <br> colors::editorOverviewRuler.incomingContentForeground <br> colors::editorOverviewRuler.infoForeground <br> colors::editorOverviewRuler.modifiedForeground <br> colors::editorOverviewRuler.selectionHighlightForeground <br> colors::editorOverviewRuler.warningForeground <br> colors::editorOverviewRuler.wordHighlightForeground <br> colors::editorOverviewRuler.wordHighlightStrongForeground <br> colors::editorRuler.foreground <br> colors::editorSuggestWidget.background <br> colors::editorSuggestWidget.foreground <br> colors::editorSuggestWidget.selectedBackground <br> colors::editorWarning.foreground <br> colors::errorForeground <br> colors::extensionButton.prominentForeground <br> colors::foreground <br> colors::gitDecoration.conflictingResourceForeground <br> colors::gitDecoration.deletedResourceForeground <br> colors::gitDecoration.ignoredResourceForeground <br> colors::gitDecoration.modifiedResourceForeground <br> colors::gitDecoration.untrackedResourceForeground <br> colors::inlineChat.regionHighlight <br> colors::input.border <br> colors::inputValidation.errorBorder <br> colors::inputValidation.infoBorder <br> colors::inputValidation.warningBorder <br> colors::list.dropBackground <br> colors::list.errorForeground <br> colors::list.focusBackground <br> colors::list.warningForeground <br> colors::listFilterWidget.background <br> colors::listFilterWidget.noMatchesOutline <br> colors::listFilterWidget.outline <br> colors::merge.currentHeaderBackground <br> colors::merge.incomingHeaderBackground <br> colors::panel.background <br> colors::panelTitle.activeBorder <br> colors::panelTitle.activeForeground <br> colors::panelTitle.inactiveForeground <br> colors::peekViewResult.fileForeground <br> colors::peekViewResult.lineForeground <br> colors::peekViewResult.matchHighlightBackground <br> colors::peekViewResult.selectionBackground <br> colors::peekViewResult.selectionForeground <br> colors::peekViewTitleDescription.foreground <br> colors::peekViewTitleLabel.foreground <br> colors::settings.checkboxBackground <br> colors::settings.checkboxBorder <br> colors::settings.checkboxForeground <br> colors::settings.dropdownBackground <br> colors::settings.dropdownBorder <br> colors::settings.dropdownForeground <br> colors::settings.headerForeground <br> colors::settings.modifiedItemIndicator <br> colors::settings.numberInputBackground <br> colors::settings.numberInputBorder <br> colors::settings.numberInputForeground <br> colors::settings.textInputBackground <br> colors::settings.textInputBorder <br> colors::settings.textInputForeground <br> colors::sideBarSectionHeader.background <br> colors::sideBarSectionHeader.border <br> colors::sideBarTitle.foreground <br> colors::statusBar.debuggingForeground <br> colors::statusBar.noFolderForeground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::statusBarItem.remoteForeground <br> colors::tab.activeBorderTop <br> colors::tab.activeForeground <br> colors::terminal.background <br> colors::terminal.foreground <br> colors::titleBar.activeForeground <br> colors::titleBar.inactiveBackground <br> colors::titleBar.inactiveForeground <br> colors::walkThrough.embeddedEditorBackground <br> dracula::ansi:: <br> dracula::base:: <br> dracula::brightOther:: <br> dracula::other:: <br> maintainers:: <br> name <br> semanticClass <br> semanticHighlighting <br> tokenColors::[]name <br> tokenColors::[]scope>beginning.punctuation.definition.list.markdown <br> tokenColors::[]scope>beginning.punctuation.definition.quote.markdown <br> tokenColors::[]scope>comment keyword.codetag.notation <br> tokenColors::[]scope>comment.block.documentation entity.name.type <br> tokenColors::[]scope>comment.block.documentation entity.name.type punctuation.definition.bracket <br> tokenColors::[]scope>comment.block.documentation keyword <br> tokenColors::[]scope>comment.block.documentation storage.type.class <br> tokenColors::[]scope>comment.block.documentation variable <br> tokenColors::[]scope>constant <br> tokenColors::[]scope>constant.character.escape <br> tokenColors::[]scope>constant.character.escape.backslash.regexp <br> tokenColors::[]scope>constant.character.string.escape <br> tokenColors::[]scope>constant.language.empty-list.haskell <br> tokenColors::[]scope>constant.other.character-class.set.regexp <br> tokenColors::[]scope>constant.other.date <br> tokenColors::[]scope>constant.other.key.perl <br> tokenColors::[]scope>constant.other.symbol.hashkey punctuation.definition.constant.ruby <br> tokenColors::[]scope>constant.other.symbol.hashkey.ruby <br> tokenColors::[]scope>constant.other.timestamp <br> tokenColors::[]scope>constant.regexp <br> tokenColors::[]scope>emphasis <br> tokenColors::[]scope>entity.name.class <br> tokenColors::[]scope>entity.name.directive.restructuredtext <br> tokenColors::[]scope>entity.name.filename <br> tokenColors::[]scope>entity.name.fragment.graphql <br> tokenColors::[]scope>entity.name.function.target.makefile <br> tokenColors::[]scope>entity.name.section.toml <br> tokenColors::[]scope>entity.name.tag.yaml <br> tokenColors::[]scope>entity.name.type <br> tokenColors::[]scope>entity.name.type.class <br> tokenColors::[]scope>entity.name.type.type-parameter <br> tokenColors::[]scope>entity.name.variable.parameter <br> tokenColors::[]scope>entity.other.attribute-name.parent-selector <br> tokenColors::[]scope>entity.other.attribute-name.placeholder punctuation <br> tokenColors::[]scope>entity.other.attribute-name.pseudo-class punctuation <br> tokenColors::[]scope>entity.other.attribute-name.pseudo-element punctuation <br> tokenColors::[]scope>entity.other.inherited-class <br> tokenColors::[]scope>fenced_code.block.language <br> tokenColors::[]scope>header <br> tokenColors::[]scope>invalid <br> tokenColors::[]scope>invalid.deprecated <br> tokenColors::[]scope>keyword.control.new <br> tokenColors::[]scope>keyword.expressions-and-types.swift <br> tokenColors::[]scope>keyword.operator.dereference.java <br> tokenColors::[]scope>keyword.operator.function.infix <br> tokenColors::[]scope>keyword.operator.navigation.groovy <br> tokenColors::[]scope>keyword.operator.negation.regexp <br> tokenColors::[]scope>keyword.operator.new <br> tokenColors::[]scope>keyword.operator.other.powershell <br> tokenColors::[]scope>keyword.other.statement-separator.powershell <br> tokenColors::[]scope>keyword.other.this <br> tokenColors::[]scope>keyword.primitive-datatypes.swift <br> tokenColors::[]scope>keyword.type.cs <br> tokenColors::[]scope>log.error <br> tokenColors::[]scope>log.warning <br> tokenColors::[]scope>markup.changed <br> tokenColors::[]scope>markup.deleted <br> tokenColors::[]scope>markup.error <br> tokenColors::[]scope>markup.fenced_code.block.markdown punctuation.definition.markdown <br> tokenColors::[]scope>markup.heading.markdown punctuation.definition.string.begin <br> tokenColors::[]scope>markup.heading.markdown punctuation.definition.string.end <br> tokenColors::[]scope>markup.inline.raw <br> tokenColors::[]scope>markup.inserted <br> tokenColors::[]scope>markup.italic <br> tokenColors::[]scope>markup.quote <br> tokenColors::[]scope>markup.quote.markdown meta.paragraph.markdown punctuation.definition.string.begin <br> tokenColors::[]scope>markup.quote.markdown meta.paragraph.markdown punctuation.definition.string.end <br> tokenColors::[]scope>markup.raw.inner.restructuredtext <br> tokenColors::[]scope>markup.raw.restructuredtext <br> tokenColors::[]scope>markup.underline <br> tokenColors::[]scope>markup.underline.link <br> tokenColors::[]scope>markup.underline.link.image <br> tokenColors::[]scope>meta.assertion.look-ahead.regexp <br> tokenColors::[]scope>meta.at-rule.function variable <br> tokenColors::[]scope>meta.at-rule.mixin variable <br> tokenColors::[]scope>meta.attribute-selector.scss <br> tokenColors::[]scope>meta.brace.round <br> tokenColors::[]scope>meta.decorator variable.other.object <br> tokenColors::[]scope>meta.decorator variable.other.property <br> tokenColors::[]scope>meta.decorator variable.other.readwrite <br> tokenColors::[]scope>meta.diff <br> tokenColors::[]scope>meta.diff.header <br> tokenColors::[]scope>meta.export variable.other.readwrite.alias <br> tokenColors::[]scope>meta.function-call punctuation <br> tokenColors::[]scope>meta.function-call.object <br> tokenColors::[]scope>meta.function-call.php <br> tokenColors::[]scope>meta.function-call.static <br> tokenColors::[]scope>meta.function.arguments variable.other.php <br> tokenColors::[]scope>meta.group.double.toml <br> tokenColors::[]scope>meta.group.toml <br> tokenColors::[]scope>meta.implementation storage.type.objc <br> tokenColors::[]scope>meta.import variable.other.readwrite <br> tokenColors::[]scope>meta.import variable.other.readwrite.alias <br> tokenColors::[]scope>meta.indexer.mappedtype.declaration entity.name.type <br> tokenColors::[]scope>meta.interface-or-protocol storage.type.objc <br> tokenColors::[]scope>meta.link.reference.def.restructuredtext <br> tokenColors::[]scope>meta.method-call.java meta.method <br> tokenColors::[]scope>meta.method.groovy <br> tokenColors::[]scope>meta.object-binding-pattern-variable punctuation.destructuring <br> tokenColors::[]scope>meta.paragraph.markdown punctuation.definition.string.begin <br> tokenColors::[]scope>meta.paragraph.markdown punctuation.definition.string.end <br> tokenColors::[]scope>meta.preprocessor.haskell <br> tokenColors::[]scope>meta.protocol-list.objc <br> tokenColors::[]scope>meta.return-type.objc <br> tokenColors::[]scope>meta.scope.for-loop.shell punctuation.definition.string.begin <br> tokenColors::[]scope>meta.scope.for-loop.shell punctuation.definition.string.end <br> tokenColors::[]scope>meta.scope.for-loop.shell string <br> tokenColors::[]scope>meta.scope.prerequisites.makefile <br> tokenColors::[]scope>meta.selectionset.graphql meta.arguments variable <br> tokenColors::[]scope>meta.selectionset.graphql meta.arguments.graphql variable.arguments.graphql <br> tokenColors::[]scope>meta.selectionset.graphql variable <br> tokenColors::[]scope>meta.selector <br> tokenColors::[]scope>meta.separator.markdown <br> tokenColors::[]scope>meta.string-contents.quoted.double punctuation.definition.variable <br> tokenColors::[]scope>meta.type.parameters entity.name.type <br> tokenColors::[]scope>meta.variable.assignment.destructured.object.coffee variable <br> tokenColors::[]scope>meta.variable.assignment.destructured.object.coffee variable variable <br> tokenColors::[]scope>punctuation.colon.graphql <br> tokenColors::[]scope>punctuation.definition.arguments.begin <br> tokenColors::[]scope>punctuation.definition.arguments.end <br> tokenColors::[]scope>punctuation.definition.attribute-selector.begin.bracket.square.scss <br> tokenColors::[]scope>punctuation.definition.attribute-selector.end.bracket.square.scss <br> tokenColors::[]scope>punctuation.definition.block.scalar.folded.yaml <br> tokenColors::[]scope>punctuation.definition.block.scalar.literal.yaml <br> tokenColors::[]scope>punctuation.definition.block.sequence.item.yaml <br> tokenColors::[]scope>punctuation.definition.character-class.regexp <br> tokenColors::[]scope>punctuation.definition.comment <br> tokenColors::[]scope>punctuation.definition.constant.restructuredtext <br> tokenColors::[]scope>punctuation.definition.directive.restructuredtext <br> tokenColors::[]scope>punctuation.definition.entity.begin <br> tokenColors::[]scope>punctuation.definition.entity.end <br> tokenColors::[]scope>punctuation.definition.entity.other.inherited-class <br> tokenColors::[]scope>punctuation.definition.group.assertion.regexp <br> tokenColors::[]scope>punctuation.definition.group.capture.regexp <br> tokenColors::[]scope>punctuation.definition.group.regexp <br> tokenColors::[]scope>punctuation.definition.interpolation.begin <br> tokenColors::[]scope>punctuation.definition.interpolation.end <br> tokenColors::[]scope>punctuation.definition.keyword <br> tokenColors::[]scope>punctuation.definition.link.restructuredtext <br> tokenColors::[]scope>punctuation.definition.string.begin <br> tokenColors::[]scope>punctuation.definition.string.end <br> tokenColors::[]scope>punctuation.definition.tag.cs <br> tokenColors::[]scope>punctuation.definition.template-expression.begin <br> tokenColors::[]scope>punctuation.definition.template-expression.end <br> tokenColors::[]scope>punctuation.definition.type.begin <br> tokenColors::[]scope>punctuation.definition.type.end <br> tokenColors::[]scope>punctuation.definition.variable.makefile <br> tokenColors::[]scope>punctuation.function.swift <br> tokenColors::[]scope>punctuation.section.embedded.begin <br> tokenColors::[]scope>punctuation.section.embedded.begin.jsx <br> tokenColors::[]scope>punctuation.section.embedded.begin.tsx <br> tokenColors::[]scope>punctuation.section.embedded.coffee <br> tokenColors::[]scope>punctuation.section.embedded.end <br> tokenColors::[]scope>punctuation.section.embedded.end source.php <br> tokenColors::[]scope>punctuation.section.embedded.end source.ruby <br> tokenColors::[]scope>punctuation.section.embedded.end.jsx <br> tokenColors::[]scope>punctuation.section.embedded.end.tsx <br> tokenColors::[]scope>punctuation.section.scope.begin <br> tokenColors::[]scope>punctuation.section.scope.end <br> tokenColors::[]scope>punctuation.separator.annotation <br> tokenColors::[]scope>punctuation.separator.dictionary.key-value <br> tokenColors::[]scope>punctuation.separator.hash <br> tokenColors::[]scope>punctuation.separator.inheritance <br> tokenColors::[]scope>punctuation.separator.key-value <br> tokenColors::[]scope>punctuation.separator.key-value.mapping.yaml <br> tokenColors::[]scope>punctuation.separator.list.comma.css <br> tokenColors::[]scope>punctuation.separator.namespace <br> tokenColors::[]scope>punctuation.separator.pointer-access <br> tokenColors::[]scope>punctuation.separator.slice <br> tokenColors::[]scope>punctuation.support.type.property-name.begin <br> tokenColors::[]scope>punctuation.support.type.property-name.end <br> tokenColors::[]scope>punctuation.terminator.expression.php <br> tokenColors::[]scope>source.go storage.type <br> tokenColors::[]scope>source.groovy storage.type <br> tokenColors::[]scope>source.groovy storage.type.def <br> tokenColors::[]scope>source.java storage.type <br> tokenColors::[]scope>source.powershell entity.other.attribute-name <br> tokenColors::[]scope>source.shell variable.other <br> tokenColors::[]scope>storage.class.std.rust <br> tokenColors::[]scope>storage.modifier <br> tokenColors::[]scope>storage.modifier.import <br> tokenColors::[]scope>storage.type.attribute.swift <br> tokenColors::[]scope>storage.type.c <br> tokenColors::[]scope>storage.type.core.rust <br> tokenColors::[]scope>storage.type.cs <br> tokenColors::[]scope>storage.type.generic.java <br> tokenColors::[]scope>storage.type.groovy <br> tokenColors::[]scope>storage.type.haskell <br> tokenColors::[]scope>storage.type.objc <br> tokenColors::[]scope>storage.type.ocaml <br> tokenColors::[]scope>storage.type.php <br> tokenColors::[]scope>string.other.link.description <br> tokenColors::[]scope>string.other.link.title <br> tokenColors::[]scope>string.quoted.docstring.multi <br> tokenColors::[]scope>string.quoted.docstring.multi.python constant.character.escape <br> tokenColors::[]scope>string.quoted.docstring.multi.python punctuation.definition.string.begin <br> tokenColors::[]scope>string.quoted.docstring.multi.python punctuation.definition.string.end <br> tokenColors::[]scope>string.regexp <br> tokenColors::[]scope>string.regexp punctuation.definition.string.begin <br> tokenColors::[]scope>string.regexp punctuation.definition.string.end <br> tokenColors::[]scope>string.template meta.brace <br> tokenColors::[]scope>string.template punctuation.accessor <br> tokenColors::[]scope>string.unquoted.heredoc punctuation.definition.string <br> tokenColors::[]scope>strong <br> tokenColors::[]scope>support <br> tokenColors::[]scope>support.function <br> tokenColors::[]scope>support.function.any-method.lua <br> tokenColors::[]scope>support.function.magic <br> tokenColors::[]scope>support.other.chomping-indicator.yaml <br> tokenColors::[]scope>support.type.property-name <br> tokenColors::[]scope>support.variable <br> tokenColors::[]scope>support.variable.property <br> tokenColors::[]scope>unused.comment <br> tokenColors::[]scope>variable <br> tokenColors::[]scope>variable.fragment.graphql <br> tokenColors::[]scope>variable.language <br> tokenColors::[]scope>variable.language punctuation.definition.variable.php <br> tokenColors::[]scope>variable.other.alias.yaml <br> tokenColors::[]scope>variable.other.constant <br> tokenColors::[]scope>variable.other.constant.js <br> tokenColors::[]scope>variable.other.constant.ts <br> tokenColors::[]scope>variable.other.constant.tsx <br> tokenColors::[]scope>variable.other.key.toml <br> tokenColors::[]scope>variable.other.predefined <br> tokenColors::[]scope>variable.other.readwrite.instance.ruby <br> tokenColors::[]scope>variable.parameter <br> tokenColors::[]scope>variable.parameter.function.language.special <br> tokenColors::[]scope>wildcard.comment |
| iceberg.color-theme.json | colors::activityBar.inactiveForeground <br> colors::activityBarBadge.foreground <br> colors::badge.foreground <br> colors::breadcrumb.activeSelectionForeground <br> colors::breadcrumb.background <br> colors::breadcrumb.focusForeground <br> colors::breadcrumb.foreground <br> colors::breadcrumbPicker.background <br> colors::button.foreground <br> colors::button.hoverBackground <br> colors::debugConsole.errorForeground <br> colors::debugConsole.infoForeground <br> colors::debugConsole.sourceForeground <br> colors::debugConsole.warningForeground <br> colors::debugConsoleInputIcon.foreground <br> colors::debugIcon.breakpointCurrentStackframeForeground <br> colors::debugIcon.breakpointDisabledForeground <br> colors::debugIcon.breakpointForeground <br> colors::debugIcon.breakpointStackframeForeground <br> colors::debugIcon.breakpointUnverifiedForeground <br> colors::debugIcon.continueForeground <br> colors::debugIcon.disconnectForeground <br> colors::debugIcon.pauseForeground <br> colors::debugIcon.restartForeground <br> colors::debugIcon.startForeground <br> colors::debugIcon.stepBackForeground <br> colors::debugIcon.stepIntoForeground <br> colors::debugIcon.stepOutForeground <br> colors::debugIcon.stepOverForeground <br> colors::debugIcon.stopForeground <br> colors::debugTokenExpression.boolean <br> colors::debugTokenExpression.error <br> colors::debugTokenExpression.name <br> colors::debugTokenExpression.number <br> colors::debugTokenExpression.string <br> colors::debugTokenExpression.value <br> colors::descriptionForeground <br> colors::diffEditor.insertedTextBackground <br> colors::diffEditor.removedTextBackground <br> colors::dropdown.foreground <br> colors::editor.findMatchBackground <br> colors::editor.findMatchHighlightBackground <br> colors::editor.foldBackground <br> colors::editor.lineHighlightBackground <br> colors::editor.rangeHighlightBackground <br> colors::editor.wordHighlightBackground <br> colors::editor.wordHighlightStrongBackground <br> colors::editorBracketHighlight.foreground1 <br> colors::editorBracketHighlight.foreground2 <br> colors::editorBracketHighlight.foreground3 <br> colors::editorBracketHighlight.foreground4 <br> colors::editorBracketHighlight.foreground5 <br> colors::editorBracketHighlight.foreground6 <br> colors::editorBracketHighlight.unexpectedBracket.foreground <br> colors::editorBracketMatch.background <br> colors::editorBracketMatch.border <br> colors::editorCursor.foreground <br> colors::editorError.foreground <br> colors::editorGroup.dropBackground <br> colors::editorGutter.addedBackground <br> colors::editorGutter.background <br> colors::editorGutter.deletedBackground <br> colors::editorGutter.modifiedBackground <br> colors::editorHoverWidget.border <br> colors::editorHoverWidget.foreground <br> colors::editorHoverWidget.statusBarBackground <br> colors::editorLightBulb.foreground <br> colors::editorLightBulbAutoFix.foreground <br> colors::editorLineNumber.activeForeground <br> colors::editorLineNumber.foreground <br> colors::editorLink.activeForeground <br> colors::editorMarkerNavigation.background <br> colors::editorOverviewRuler.addedForeground <br> colors::editorOverviewRuler.border <br> colors::editorOverviewRuler.deletedForeground <br> colors::editorOverviewRuler.errorForeground <br> colors::editorOverviewRuler.infoForeground <br> colors::editorOverviewRuler.modifiedForeground <br> colors::editorOverviewRuler.warningForeground <br> colors::editorOverviewRuler.wordHighlightForeground <br> colors::editorRuler.foreground <br> colors::editorSuggestWidget.selectedBackground <br> colors::editorWarning.foreground <br> colors::editorWidget.border <br> colors::extensionButton.prominentForeground <br> colors::foreground <br> colors::gitDecoration.addedResourceForeground <br> colors::gitDecoration.conflictingResourceForeground <br> colors::gitDecoration.deletedResourceForeground <br> colors::gitDecoration.ignoredResourceForeground <br> colors::gitDecoration.modifiedResourceForeground <br> colors::gitDecoration.renamedResourceForeground <br> colors::gitDecoration.stageDeletedResourceForeground <br> colors::gitDecoration.stageModifiedResourceForeground <br> colors::gitDecoration.submoduleResourceForeground <br> colors::gitDecoration.untrackedResourceForeground <br> colors::inputValidation.errorBackground <br> colors::inputValidation.errorBorder <br> colors::list.dropBackground <br> colors::list.errorForeground <br> colors::list.focusForeground <br> colors::list.warningForeground <br> colors::menu.background <br> colors::menu.foreground <br> colors::menu.selectionBackground <br> colors::menu.selectionForeground <br> colors::menu.separatorBackground <br> colors::menubar.selectionBackground <br> colors::menubar.selectionForeground <br> colors::merge.currentContentBackground <br> colors::merge.currentHeaderBackground <br> colors::merge.incomingContentBackground <br> colors::merge.incomingHeaderBackground <br> colors::notificationCenterHeader.background <br> colors::notifications.background <br> colors::notifications.border <br> colors::notifications.foreground <br> colors::notificationsErrorIcon.foreground <br> colors::notificationsInfoIcon.foreground <br> colors::notificationsWarningIcon.foreground <br> colors::panel.background <br> colors::panelTitle.activeForeground <br> colors::panelTitle.inactiveForeground <br> colors::peekViewEditorGutter.background <br> colors::peekViewResult.fileForeground <br> colors::peekViewResult.lineForeground <br> colors::peekViewResult.matchHighlightBackground <br> colors::peekViewResult.selectionBackground <br> colors::peekViewTitleDescription.foreground <br> colors::peekViewTitleLabel.foreground <br> colors::problemsErrorIcon.foreground <br> colors::problemsInfoIcon.foreground <br> colors::problemsWarningIcon.foreground <br> colors::quickInput.background <br> colors::quickInput.foreground <br> colors::quickInputList.focusBackground <br> colors::scrollbar.shadow <br> colors::scrollbarSlider.background <br> colors::scrollbarSlider.hoverBackground <br> colors::settings.headerForeground <br> colors::settings.modifiedItemIndicator <br> colors::sideBar.border <br> colors::sideBar.dropBackground <br> colors::sideBar.foreground <br> colors::sideBarSectionHeader.background <br> colors::sideBarSectionHeader.foreground <br> colors::statusBar.debuggingForeground <br> colors::statusBar.noFolderForeground <br> colors::statusBarItem.errorBackground <br> colors::statusBarItem.errorForeground <br> colors::statusBarItem.hoverBackground <br> colors::symbolIcon.classForeground <br> colors::symbolIcon.constructorForeground <br> colors::symbolIcon.enumeratorForeground <br> colors::symbolIcon.enumeratorMemberForeground <br> colors::symbolIcon.eventForeground <br> colors::symbolIcon.fieldForeground <br> colors::symbolIcon.functionForeground <br> colors::symbolIcon.interfaceForeground <br> colors::symbolIcon.methodForeground <br> colors::symbolIcon.variableForeground <br> colors::tab.activeForeground <br> colors::tab.activeModifiedBorder <br> colors::tab.hoverBackground <br> colors::tab.inactiveModifiedBorder <br> colors::tab.unfocusedActiveForeground <br> colors::tab.unfocusedInactiveForeground <br> colors::terminal.foreground <br> colors::terminal.selectionBackground <br> colors::terminalCommandDecoration.defaultBackground <br> colors::terminalCommandDecoration.errorBackground <br> colors::terminalCommandDecoration.successBackground <br> colors::textLink.activeForeground <br> colors::textLink.foreground <br> colors::titleBar.activeForeground <br> colors::titleBar.inactiveBackground <br> colors::titleBar.inactiveForeground <br> colors::tree.indentGuidesStroke <br> colors::widget.shadow <br> name <br> tokenColors::[]scope>constant <br> tokenColors::[]scope>entity.name.class <br> tokenColors::[]scope>entity.name.function.method <br> tokenColors::[]scope>entity.name.import.go <br> tokenColors::[]scope>entity.name.section <br> tokenColors::[]scope>entity.other.attribute-name.class.css, entity.other.attribute-name.parent-selector-suffix.css <br> tokenColors::[]scope>keyword.control.at-rule, keyword.control.content <br> tokenColors::[]scope>keyword.function <br> tokenColors::[]scope>keyword.operator <br> tokenColors::[]scope>keyword.operator.expression <br> tokenColors::[]scope>keyword.operator.new <br> tokenColors::[]scope>keyword.other.important.scss <br> tokenColors::[]scope>keyword.other.unit <br> tokenColors::[]scope>markup.deleted.diff <br> tokenColors::[]scope>markup.fenced_code.block <br> tokenColors::[]scope>markup.inline.raw.string <br> tokenColors::[]scope>markup.inserted.diff <br> tokenColors::[]scope>markup.underline.link <br> tokenColors::[]scope>meta.brace.square <br> tokenColors::[]scope>meta.definition.method <br> tokenColors::[]scope>meta.diff.header <br> tokenColors::[]scope>meta.diff.range <br> tokenColors::[]scope>meta.link <br> tokenColors::[]scope>meta.object-literal.key <br> tokenColors::[]scope>meta.tag.attributes <br> tokenColors::[]scope>meta.tag.sgml.doctype <br> tokenColors::[]scope>meta.type.annotation <br> tokenColors::[]scope>punctuation.definition.block <br> tokenColors::[]scope>punctuation.definition.block.tag.jsdoc <br> tokenColors::[]scope>punctuation.definition.tag <br> tokenColors::[]scope>punctuation.definition.template-expression <br> tokenColors::[]scope>storage.type.class.jsdoc <br> tokenColors::[]scope>storage.type.function <br> tokenColors::[]scope>support <br> tokenColors::[]scope>support.type.class.flowtype <br> tokenColors::[]scope>support.type.property-name <br> tokenColors::[]scope>text <br> tokenColors::[]scope>variable.interpolation.scss <br> tokenColors::[]scope>variable.language.this <br> tokenColors::[]scope>variable.other.jsdoc <br> tokenColors::[]scope>variable.scss |
| ayu-light.json | colors::activityBar.activeBorder <br> colors::activityBar.border <br> colors::activityBar.inactiveForeground <br> colors::activityBarBadge.foreground <br> colors::badge.foreground <br> colors::button.foreground <br> colors::button.hoverBackground <br> colors::button.secondaryBackground <br> colors::button.secondaryForeground <br> colors::button.secondaryHoverBackground <br> colors::debugConsoleInputIcon.foreground <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugIcon.breakpointDisabledForeground <br> colors::debugIcon.breakpointForeground <br> colors::descriptionForeground <br> colors::diffEditor.diagonalFill <br> colors::diffEditor.insertedTextBackground <br> colors::diffEditor.removedTextBackground <br> colors::dropdown.foreground <br> colors::editor.findMatchBackground <br> colors::editor.findMatchBorder <br> colors::editor.findMatchHighlightBackground <br> colors::editor.findMatchHighlightBorder <br> colors::editor.findRangeHighlightBackground <br> colors::editor.inactiveSelectionBackground <br> colors::editor.lineHighlightBackground <br> colors::editor.rangeHighlightBackground <br> colors::editor.selectionHighlightBackground <br> colors::editor.selectionHighlightBorder <br> colors::editor.snippetTabstopHighlightBackground <br> colors::editor.wordHighlightBackground <br> colors::editor.wordHighlightBorder <br> colors::editor.wordHighlightStrongBackground <br> colors::editor.wordHighlightStrongBorder <br> colors::editorBracketMatch.background <br> colors::editorBracketMatch.border <br> colors::editorCodeLens.foreground <br> colors::editorCursor.foreground <br> colors::editorError.foreground <br> colors::editorGroup.background <br> colors::editorGroupHeader.noTabsBackground <br> colors::editorGroupHeader.tabsBorder <br> colors::editorGutter.addedBackground <br> colors::editorGutter.deletedBackground <br> colors::editorGutter.modifiedBackground <br> colors::editorHoverWidget.border <br> colors::editorLineNumber.activeForeground <br> colors::editorLineNumber.foreground <br> colors::editorLink.activeForeground <br> colors::editorMarkerNavigation.background <br> colors::editorOverviewRuler.addedForeground <br> colors::editorOverviewRuler.border <br> colors::editorOverviewRuler.bracketMatchForeground <br> colors::editorOverviewRuler.deletedForeground <br> colors::editorOverviewRuler.errorForeground <br> colors::editorOverviewRuler.findMatchForeground <br> colors::editorOverviewRuler.modifiedForeground <br> colors::editorOverviewRuler.warningForeground <br> colors::editorOverviewRuler.wordHighlightForeground <br> colors::editorOverviewRuler.wordHighlightStrongForeground <br> colors::editorRuler.foreground <br> colors::editorSuggestWidget.background <br> colors::editorSuggestWidget.border <br> colors::editorSuggestWidget.highlightForeground <br> colors::editorSuggestWidget.selectedBackground <br> colors::editorWarning.foreground <br> colors::editorWidget.border <br> colors::errorForeground <br> colors::extensionButton.prominentForeground <br> colors::foreground <br> colors::gitDecoration.conflictingResourceForeground <br> colors::gitDecoration.deletedResourceForeground <br> colors::gitDecoration.ignoredResourceForeground <br> colors::gitDecoration.modifiedResourceForeground <br> colors::gitDecoration.submoduleResourceForeground <br> colors::gitDecoration.untrackedResourceForeground <br> colors::icon.foreground <br> colors::input.border <br> colors::inputOption.activeBackground <br> colors::inputOption.activeForeground <br> colors::inputValidation.errorBackground <br> colors::inputValidation.errorBorder <br> colors::inputValidation.infoBackground <br> colors::inputValidation.infoBorder <br> colors::inputValidation.warningBackground <br> colors::inputValidation.warningBorder <br> colors::keybindingLabel.background <br> colors::keybindingLabel.border <br> colors::keybindingLabel.bottomBorder <br> colors::keybindingLabel.foreground <br> colors::list.deemphasizedForeground <br> colors::list.errorForeground <br> colors::list.filterMatchBackground <br> colors::list.filterMatchBorder <br> colors::list.focusBackground <br> colors::list.focusForeground <br> colors::list.focusOutline <br> colors::list.inactiveSelectionForeground <br> colors::list.invalidItemForeground <br> colors::listFilterWidget.background <br> colors::listFilterWidget.noMatchesOutline <br> colors::listFilterWidget.outline <br> colors::minimap.background <br> colors::minimap.errorHighlight <br> colors::minimap.findMatchHighlight <br> colors::minimap.selectionHighlight <br> colors::minimapGutter.addedBackground <br> colors::minimapGutter.deletedBackground <br> colors::minimapGutter.modifiedBackground <br> colors::panel.background <br> colors::panelTitle.activeBorder <br> colors::panelTitle.activeForeground <br> colors::panelTitle.inactiveForeground <br> colors::peekViewEditor.matchHighlightBorder <br> colors::peekViewResult.fileForeground <br> colors::peekViewResult.lineForeground <br> colors::peekViewResult.matchHighlightBackground <br> colors::peekViewResult.selectionBackground <br> colors::peekViewTitleDescription.foreground <br> colors::peekViewTitleLabel.foreground <br> colors::scrollbar.shadow <br> colors::scrollbarSlider.activeBackground <br> colors::scrollbarSlider.background <br> colors::scrollbarSlider.hoverBackground <br> colors::settings.headerForeground <br> colors::settings.modifiedItemIndicator <br> colors::sideBar.border <br> colors::sideBarSectionHeader.background <br> colors::sideBarSectionHeader.border <br> colors::sideBarSectionHeader.foreground <br> colors::sideBarTitle.foreground <br> colors::statusBar.border <br> colors::statusBar.debuggingForeground <br> colors::statusBarItem.activeBackground <br> colors::statusBarItem.hoverBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::statusBarItem.remoteForeground <br> colors::tab.activeBorder <br> colors::tab.activeForeground <br> colors::tab.unfocusedActiveBorder <br> colors::tab.unfocusedActiveForeground <br> colors::tab.unfocusedInactiveForeground <br> colors::terminal.background <br> colors::terminal.foreground <br> colors::textBlockQuote.background <br> colors::textLink.activeForeground <br> colors::textLink.foreground <br> colors::textPreformat.foreground <br> colors::titleBar.activeForeground <br> colors::titleBar.border <br> colors::titleBar.inactiveBackground <br> colors::titleBar.inactiveForeground <br> colors::tree.indentGuidesStroke <br> colors::walkThrough.embeddedEditorBackground <br> colors::welcomePage.buttonBackground <br> colors::welcomePage.progress.background <br> colors::welcomePage.tileBackground <br> colors::welcomePage.tileShadow <br> colors::widget.shadow <br> semanticHighlighting <br> semanticTokenColors::parameter.label <br> tokenColors::[]name <br> tokenColors::[]scope>constant.character <br> tokenColors::[]scope>constant.language <br> tokenColors::[]scope>constant.numeric <br> tokenColors::[]scope>constant.numeric.line-number.find-in-files - match <br> tokenColors::[]scope>constant.numeric.line-number.match <br> tokenColors::[]scope>constant.other <br> tokenColors::[]scope>constant.other.symbol <br> tokenColors::[]scope>entity.name <br> tokenColors::[]scope>entity.name.filename.find-in-files <br> tokenColors::[]scope>entity.name.import <br> tokenColors::[]scope>entity.name.package <br> tokenColors::[]scope>entity.other.inherited-class <br> tokenColors::[]scope>invalid <br> tokenColors::[]scope>keyword.operator <br> tokenColors::[]scope>markup.bold markup.italic <br> tokenColors::[]scope>markup.changed <br> tokenColors::[]scope>markup.deleted <br> tokenColors::[]scope>markup.heading entity.name <br> tokenColors::[]scope>markup.inserted <br> tokenColors::[]scope>markup.italic <br> tokenColors::[]scope>markup.italic markup.bold <br> tokenColors::[]scope>markup.list punctuation.definition.list.begin <br> tokenColors::[]scope>markup.quote <br> tokenColors::[]scope>markup.raw <br> tokenColors::[]scope>markup.raw.inline <br> tokenColors::[]scope>markup.strike <br> tokenColors::[]scope>markup.table <br> tokenColors::[]scope>markup.underline.link <br> tokenColors::[]scope>message.error <br> tokenColors::[]scope>meta.decorator punctuation.decorator <br> tokenColors::[]scope>meta.decorator variable.other <br> tokenColors::[]scope>meta.diff <br> tokenColors::[]scope>meta.diff.header <br> tokenColors::[]scope>meta.embedded <br> tokenColors::[]scope>meta.function-call.generic <br> tokenColors::[]scope>meta.parameter <br> tokenColors::[]scope>meta.separator <br> tokenColors::[]scope>meta.tag.sgml <br> tokenColors::[]scope>punctuation.accessor <br> tokenColors::[]scope>punctuation.definition.markdown <br> tokenColors::[]scope>punctuation.definition.tag <br> tokenColors::[]scope>punctuation.definition.tag.begin <br> tokenColors::[]scope>punctuation.definition.tag.end <br> tokenColors::[]scope>punctuation.definition.template-expression <br> tokenColors::[]scope>punctuation.section <br> tokenColors::[]scope>punctuation.section.embedded <br> tokenColors::[]scope>punctuation.separator <br> tokenColors::[]scope>punctuation.terminator <br> tokenColors::[]scope>source.c storage.type <br> tokenColors::[]scope>source.css entity.name.tag <br> tokenColors::[]scope>source.css support.type <br> tokenColors::[]scope>source.go storage.type <br> tokenColors::[]scope>source.haskell storage.type <br> tokenColors::[]scope>source.java storage.type <br> tokenColors::[]scope>source.java storage.type.primitive <br> tokenColors::[]scope>source.less entity.name.tag <br> tokenColors::[]scope>source.less support.type <br> tokenColors::[]scope>source.ruby variable.other.readwrite <br> tokenColors::[]scope>source.sass entity.name.tag <br> tokenColors::[]scope>source.sass support.type <br> tokenColors::[]scope>source.scss entity.name.tag <br> tokenColors::[]scope>source.scss support.type <br> tokenColors::[]scope>source.stylus entity.name.tag <br> tokenColors::[]scope>source.stylus support.type <br> tokenColors::[]scope>storage.type.annotation <br> tokenColors::[]scope>storage.type.function <br> tokenColors::[]scope>string.other.link <br> tokenColors::[]scope>string.regexp <br> tokenColors::[]scope>support.class <br> tokenColors::[]scope>support.class.component <br> tokenColors::[]scope>support.function <br> tokenColors::[]scope>support.function.go <br> tokenColors::[]scope>support.macro <br> tokenColors::[]scope>support.type <br> tokenColors::[]scope>support.type.property-name <br> tokenColors::[]scope>text.html.markdown markup.inline.raw <br> tokenColors::[]scope>text.html.markdown meta.dummy.line-break <br> tokenColors::[]scope>variable <br> tokenColors::[]scope>variable.annotation <br> tokenColors::[]scope>variable.function <br> tokenColors::[]scope>variable.language <br> tokenColors::[]scope>variable.member <br> tokenColors::[]scope>variable.parameter <br> tokenColors::[]scope>variable.parameter.function-call <br> tokenColors::[]settings::background <br> type |
| nord-color-theme.json | colors::activityBar.activeBackground <br> colors::activityBar.activeBorder <br> colors::activityBar.dropBackground <br> colors::activityBarBadge.foreground <br> colors::badge.foreground <br> colors::button.foreground <br> colors::button.hoverBackground <br> colors::button.secondaryBackground <br> colors::button.secondaryForeground <br> colors::button.secondaryHoverBackground <br> colors::charts.blue <br> colors::charts.foreground <br> colors::charts.green <br> colors::charts.lines <br> colors::charts.orange <br> colors::charts.purple <br> colors::charts.red <br> colors::charts.yellow <br> colors::debugConsole.errorForeground <br> colors::debugConsole.infoForeground <br> colors::debugConsole.sourceForeground <br> colors::debugConsole.warningForeground <br> colors::debugConsoleInputIcon.foreground <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::descriptionForeground <br> colors::diffEditor.insertedTextBackground <br> colors::diffEditor.removedTextBackground <br> colors::dropdown.foreground <br> colors::editor.findMatchBackground <br> colors::editor.findMatchHighlightBackground <br> colors::editor.findRangeHighlightBackground <br> colors::editor.focusedStackFrameHighlightBackground <br> colors::editor.hoverHighlightBackground <br> colors::editor.inactiveSelectionBackground <br> colors::editor.inlineValuesBackground <br> colors::editor.inlineValuesForeground <br> colors::editor.lineHighlightBackground <br> colors::editor.lineHighlightBorder <br> colors::editor.rangeHighlightBackground <br> colors::editor.selectionHighlightBackground <br> colors::editor.stackFrameHighlightBackground <br> colors::editor.wordHighlightBackground <br> colors::editor.wordHighlightStrongBackground <br> colors::editorActiveLineNumber.foreground <br> colors::editorBracketHighlight.foreground1 <br> colors::editorBracketHighlight.foreground2 <br> colors::editorBracketHighlight.foreground3 <br> colors::editorBracketHighlight.foreground4 <br> colors::editorBracketHighlight.foreground5 <br> colors::editorBracketHighlight.foreground6 <br> colors::editorBracketHighlight.unexpectedBracket.foreground <br> colors::editorBracketMatch.background <br> colors::editorBracketMatch.border <br> colors::editorCodeLens.foreground <br> colors::editorCursor.foreground <br> colors::editorError.border <br> colors::editorError.foreground <br> colors::editorGroup.background <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.border <br> colors::editorGroupHeader.noTabsBackground <br> colors::editorGroupHeader.tabsBorder <br> colors::editorGutter.addedBackground <br> colors::editorGutter.background <br> colors::editorGutter.deletedBackground <br> colors::editorGutter.modifiedBackground <br> colors::editorHint.border <br> colors::editorHint.foreground <br> colors::editorHoverWidget.border <br> colors::editorInlayHint.background <br> colors::editorInlayHint.foreground <br> colors::editorLineNumber.activeForeground <br> colors::editorLineNumber.foreground <br> colors::editorLink.activeForeground <br> colors::editorMarkerNavigation.background <br> colors::editorMarkerNavigationError.background <br> colors::editorMarkerNavigationWarning.background <br> colors::editorOverviewRuler.addedForeground <br> colors::editorOverviewRuler.border <br> colors::editorOverviewRuler.currentContentForeground <br> colors::editorOverviewRuler.deletedForeground <br> colors::editorOverviewRuler.errorForeground <br> colors::editorOverviewRuler.findMatchForeground <br> colors::editorOverviewRuler.incomingContentForeground <br> colors::editorOverviewRuler.infoForeground <br> colors::editorOverviewRuler.modifiedForeground <br> colors::editorOverviewRuler.rangeHighlightForeground <br> colors::editorOverviewRuler.selectionHighlightForeground <br> colors::editorOverviewRuler.warningForeground <br> colors::editorOverviewRuler.wordHighlightForeground <br> colors::editorOverviewRuler.wordHighlightStrongForeground <br> colors::editorRuler.foreground <br> colors::editorSuggestWidget.background <br> colors::editorSuggestWidget.border <br> colors::editorSuggestWidget.focusHighlightForeground <br> colors::editorSuggestWidget.foreground <br> colors::editorSuggestWidget.highlightForeground <br> colors::editorSuggestWidget.selectedBackground <br> colors::editorSuggestWidget.selectedForeground <br> colors::editorWarning.border <br> colors::editorWarning.foreground <br> colors::editorWidget.border <br> colors::errorForeground <br> colors::extensionButton.prominentForeground <br> colors::foreground <br> colors::gitDecoration.conflictingResourceForeground <br> colors::gitDecoration.deletedResourceForeground <br> colors::gitDecoration.ignoredResourceForeground <br> colors::gitDecoration.modifiedResourceForeground <br> colors::gitDecoration.stageDeletedResourceForeground <br> colors::gitDecoration.stageModifiedResourceForeground <br> colors::gitDecoration.submoduleResourceForeground <br> colors::gitDecoration.untrackedResourceForeground <br> colors::input.border <br> colors::inputOption.activeBackground <br> colors::inputOption.activeForeground <br> colors::inputValidation.errorBackground <br> colors::inputValidation.errorBorder <br> colors::inputValidation.infoBackground <br> colors::inputValidation.infoBorder <br> colors::inputValidation.warningBackground <br> colors::inputValidation.warningBorder <br> colors::keybindingLabel.background <br> colors::keybindingLabel.border <br> colors::keybindingLabel.bottomBorder <br> colors::keybindingLabel.foreground <br> colors::list.dropBackground <br> colors::list.errorForeground <br> colors::list.focusBackground <br> colors::list.focusForeground <br> colors::list.focusHighlightForeground <br> colors::list.hoverForeground <br> colors::list.inactiveFocusBackground <br> colors::list.inactiveSelectionForeground <br> colors::list.warningForeground <br> colors::merge.border <br> colors::merge.currentContentBackground <br> colors::merge.currentHeaderBackground <br> colors::merge.incomingContentBackground <br> colors::merge.incomingHeaderBackground <br> colors::minimap.background <br> colors::minimap.errorHighlight <br> colors::minimap.findMatchHighlight <br> colors::minimap.selectionHighlight <br> colors::minimap.warningHighlight <br> colors::minimapGutter.addedBackground <br> colors::minimapGutter.deletedBackground <br> colors::minimapGutter.modifiedBackground <br> colors::minimapSlider.activeBackground <br> colors::minimapSlider.background <br> colors::minimapSlider.hoverBackground <br> colors::notification.background <br> colors::notification.buttonBackground <br> colors::notification.buttonForeground <br> colors::notification.buttonHoverBackground <br> colors::notification.errorBackground <br> colors::notification.errorForeground <br> colors::notification.foreground <br> colors::notification.infoBackground <br> colors::notification.infoForeground <br> colors::notification.warningBackground <br> colors::notification.warningForeground <br> colors::notificationCenter.border <br> colors::notificationCenterHeader.background <br> colors::notificationCenterHeader.foreground <br> colors::notificationLink.foreground <br> colors::notificationToast.border <br> colors::notifications.background <br> colors::notifications.border <br> colors::notifications.foreground <br> colors::panel.background <br> colors::panelTitle.activeBorder <br> colors::panelTitle.activeForeground <br> colors::panelTitle.inactiveForeground <br> colors::peekViewEditorGutter.background <br> colors::peekViewResult.fileForeground <br> colors::peekViewResult.lineForeground <br> colors::peekViewResult.matchHighlightBackground <br> colors::peekViewResult.selectionBackground <br> colors::peekViewResult.selectionForeground <br> colors::peekViewTitleDescription.foreground <br> colors::peekViewTitleLabel.foreground <br> colors::quickInputList.focusBackground <br> colors::quickInputList.focusForeground <br> colors::sash.hoverBorder <br> colors::scrollbar.shadow <br> colors::scrollbarSlider.activeBackground <br> colors::scrollbarSlider.background <br> colors::scrollbarSlider.hoverBackground <br> colors::sideBar.border <br> colors::sideBar.foreground <br> colors::sideBarSectionHeader.background <br> colors::sideBarSectionHeader.foreground <br> colors::sideBarTitle.foreground <br> colors::statusBar.border <br> colors::statusBar.debuggingForeground <br> colors::statusBar.noFolderForeground <br> colors::statusBarItem.activeBackground <br> colors::statusBarItem.errorBackground <br> colors::statusBarItem.errorForeground <br> colors::statusBarItem.hoverBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.warningBackground <br> colors::statusBarItem.warningForeground <br> colors::tab.activeBorder <br> colors::tab.activeBorderTop <br> colors::tab.activeForeground <br> colors::tab.hoverBackground <br> colors::tab.hoverBorder <br> colors::tab.lastPinnedBorder <br> colors::tab.unfocusedActiveBorder <br> colors::tab.unfocusedActiveBorderTop <br> colors::tab.unfocusedActiveForeground <br> colors::tab.unfocusedHoverBackground <br> colors::tab.unfocusedHoverBorder <br> colors::tab.unfocusedInactiveForeground <br> colors::terminal.background <br> colors::terminal.foreground <br> colors::terminal.tab.activeBorder <br> colors::textBlockQuote.background <br> colors::textBlockQuote.border <br> colors::textCodeBlock.background <br> colors::textLink.activeForeground <br> colors::textLink.foreground <br> colors::textPreformat.foreground <br> colors::textSeparator.foreground <br> colors::titleBar.activeForeground <br> colors::titleBar.border <br> colors::titleBar.inactiveBackground <br> colors::titleBar.inactiveForeground <br> colors::tree.indentGuidesStroke <br> colors::walkThrough.embeddedEditorBackground <br> colors::welcomePage.buttonBackground <br> colors::welcomePage.buttonHoverBackground <br> colors::widget.shadow <br> name <br> semanticHighlighting <br> tokenColors::[]name <br> tokenColors::[]scope>constant.character <br> tokenColors::[]scope>constant.character.escape <br> tokenColors::[]scope>constant.language <br> tokenColors::[]scope>constant.numeric <br> tokenColors::[]scope>constant.other.symbol.elixir <br> tokenColors::[]scope>constant.regexp <br> tokenColors::[]scope>emphasis <br> tokenColors::[]scope>entity.name.class <br> tokenColors::[]scope>entity.name.type.class <br> tokenColors::[]scope>entity.name.type.module.elixir <br> tokenColors::[]scope>entity.other.inherited-class <br> tokenColors::[]scope>invalid.deprecated <br> tokenColors::[]scope>invalid.illegal <br> tokenColors::[]scope>keyword.operator <br> tokenColors::[]scope>keyword.other.new <br> tokenColors::[]scope>markup.changed <br> tokenColors::[]scope>markup.deleted <br> tokenColors::[]scope>markup.inserted <br> tokenColors::[]scope>meta.preprocessor <br> tokenColors::[]scope>punctuation <br> tokenColors::[]scope>punctuation.definition.comment <br> tokenColors::[]scope>punctuation.definition.function-parameters <br> tokenColors::[]scope>punctuation.definition.method-parameters <br> tokenColors::[]scope>punctuation.definition.parameters <br> tokenColors::[]scope>punctuation.definition.tag <br> tokenColors::[]scope>punctuation.definition.variable <br> tokenColors::[]scope>punctuation.end.definition.comment <br> tokenColors::[]scope>punctuation.section <br> tokenColors::[]scope>punctuation.section.embedded.begin <br> tokenColors::[]scope>punctuation.section.embedded.end <br> tokenColors::[]scope>punctuation.separator.pointer-access.c <br> tokenColors::[]scope>punctuation.start.definition.comment <br> tokenColors::[]scope>punctuation.terminator <br> tokenColors::[]scope>source.c keyword.control.directive.conditional <br> tokenColors::[]scope>source.c meta.preprocessor.include <br> tokenColors::[]scope>source.c punctuation.definition.directive <br> tokenColors::[]scope>source.c string.quoted.other.lt-gt.include <br> tokenColors::[]scope>source.cpp keyword.control.directive.conditional <br> tokenColors::[]scope>source.cpp punctuation.definition.directive <br> tokenColors::[]scope>source.css constant.other.color.rgb-value <br> tokenColors::[]scope>source.css keyword.control.at-rule.media <br> tokenColors::[]scope>source.css keyword.control.at-rule.media punctuation.definition.keyword <br> tokenColors::[]scope>source.css meta.property-value <br> tokenColors::[]scope>source.css punctuation.definition.keyword <br> tokenColors::[]scope>source.css support.type.property-name <br> tokenColors::[]scope>source.css.scss punctuation.definition.interpolation.begin.bracket.curly <br> tokenColors::[]scope>source.css.scss punctuation.definition.interpolation.end.bracket.curly <br> tokenColors::[]scope>source.css.scss variable.interpolation <br> tokenColors::[]scope>source.diff meta.diff.header.from-file <br> tokenColors::[]scope>source.diff meta.diff.range.context <br> tokenColors::[]scope>source.diff punctuation.definition.from-file <br> tokenColors::[]scope>source.diff punctuation.definition.range <br> tokenColors::[]scope>source.diff punctuation.definition.separator <br> tokenColors::[]scope>source.go constant.other.placeholder.go <br> tokenColors::[]scope>source.java comment.block.documentation.javadoc punctuation.definition.entity.html <br> tokenColors::[]scope>source.java constant.other <br> tokenColors::[]scope>source.java keyword.other.documentation <br> tokenColors::[]scope>source.java keyword.other.documentation.author.javadoc <br> tokenColors::[]scope>source.java keyword.other.documentation.custom <br> tokenColors::[]scope>source.java keyword.other.documentation.directive <br> tokenColors::[]scope>source.java keyword.other.documentation.see.javadoc <br> tokenColors::[]scope>source.java meta.method-call meta.method <br> tokenColors::[]scope>source.java meta.tag.template.link.javadoc <br> tokenColors::[]scope>source.java meta.tag.template.value.javadoc <br> tokenColors::[]scope>source.java punctuation.definition.keyword.javadoc <br> tokenColors::[]scope>source.java punctuation.definition.tag.begin.javadoc <br> tokenColors::[]scope>source.java punctuation.definition.tag.end.javadoc <br> tokenColors::[]scope>source.java storage.modifier.import <br> tokenColors::[]scope>source.java storage.modifier.package <br> tokenColors::[]scope>source.java storage.type <br> tokenColors::[]scope>source.java storage.type.annotation <br> tokenColors::[]scope>source.java storage.type.generic <br> tokenColors::[]scope>source.java storage.type.primitive <br> tokenColors::[]scope>source.java string.other.link.title.javadoc <br> tokenColors::[]scope>source.js meta.decorator entity.name.function <br> tokenColors::[]scope>source.js meta.decorator variable.other.readwrite <br> tokenColors::[]scope>source.js meta.embedded.line meta.brace.round <br> tokenColors::[]scope>source.js meta.embedded.line meta.brace.square <br> tokenColors::[]scope>source.js meta.object-literal.key <br> tokenColors::[]scope>source.js punctuation.decorator <br> tokenColors::[]scope>source.js storage.type.class.jsdoc <br> tokenColors::[]scope>source.js string.quoted.template meta.brace.round <br> tokenColors::[]scope>source.js string.quoted.template meta.brace.square <br> tokenColors::[]scope>source.js string.quoted.template meta.method-call.with-arguments <br> tokenColors::[]scope>source.js string.quoted.template punctuation.quasi.element.begin <br> tokenColors::[]scope>source.js string.quoted.template punctuation.quasi.element.end <br> tokenColors::[]scope>source.js string.template meta.template.expression support.variable.property <br> tokenColors::[]scope>source.js string.template meta.template.expression variable.other.object <br> tokenColors::[]scope>source.js string.template punctuation.definition.template-expression <br> tokenColors::[]scope>source.js support.type.primitive <br> tokenColors::[]scope>source.js variable.other.object <br> tokenColors::[]scope>source.js variable.other.readwrite.alias <br> tokenColors::[]scope>source.perl punctuation.definition.variable <br> tokenColors::[]scope>source.php meta.function-call <br> tokenColors::[]scope>source.php meta.function-call.object <br> tokenColors::[]scope>source.properties entity.name.section.group-title.ini <br> tokenColors::[]scope>source.properties punctuation.separator.key-value.ini <br> tokenColors::[]scope>source.python entity.name.function.decorator <br> tokenColors::[]scope>source.python meta.function-call.generic <br> tokenColors::[]scope>source.python meta.function.decorator support.type <br> tokenColors::[]scope>source.python meta.function.parameters variable.parameter.function.language.special.self <br> tokenColors::[]scope>source.python support.type <br> tokenColors::[]scope>source.python variable.parameter.function.language <br> tokenColors::[]scope>source.rust entity.name.type <br> tokenColors::[]scope>source.rust entity.name.type.trait <br> tokenColors::[]scope>source.rust meta.attribute <br> tokenColors::[]scope>source.rust meta.attribute keyword.operator <br> tokenColors::[]scope>source.rust meta.attribute punctuation <br> tokenColors::[]scope>source.rust meta.macro entity.name.function <br> tokenColors::[]scope>source.rust punctuation.definition.interpolation <br> tokenColors::[]scope>source.ts entity.name.class <br> tokenColors::[]scope>source.ts entity.name.type <br> tokenColors::[]scope>source.ts meta.decorator entity.name.function <br> tokenColors::[]scope>source.ts meta.decorator variable.other.readwrite <br> tokenColors::[]scope>source.ts meta.embedded.line meta.brace.round <br> tokenColors::[]scope>source.ts meta.embedded.line meta.brace.square <br> tokenColors::[]scope>source.ts meta.object-literal.key <br> tokenColors::[]scope>source.ts meta.object-literal.key entity.name.function <br> tokenColors::[]scope>source.ts punctuation.decorator <br> tokenColors::[]scope>source.ts support.class <br> tokenColors::[]scope>source.ts support.constant.dom <br> tokenColors::[]scope>source.ts support.constant.json <br> tokenColors::[]scope>source.ts support.constant.math <br> tokenColors::[]scope>source.ts support.type <br> tokenColors::[]scope>source.ts support.variable <br> tokenColors::[]scope>source.tsx entity.name.class <br> tokenColors::[]scope>source.tsx entity.name.type <br> tokenColors::[]scope>source.tsx meta.decorator entity.name.function <br> tokenColors::[]scope>source.tsx meta.decorator variable.other.readwrite <br> tokenColors::[]scope>source.tsx meta.embedded.line meta.brace.round <br> tokenColors::[]scope>source.tsx meta.embedded.line meta.brace.square <br> tokenColors::[]scope>source.tsx meta.object-literal.key <br> tokenColors::[]scope>source.tsx meta.object-literal.key entity.name.function <br> tokenColors::[]scope>source.tsx punctuation.decorator <br> tokenColors::[]scope>source.tsx support.class <br> tokenColors::[]scope>source.tsx support.constant.dom <br> tokenColors::[]scope>source.tsx support.constant.json <br> tokenColors::[]scope>source.tsx support.constant.math <br> tokenColors::[]scope>source.tsx support.type <br> tokenColors::[]scope>source.tsx support.variable <br> tokenColors::[]scope>source.yaml entity.name.tag <br> tokenColors::[]scope>string.regexp <br> tokenColors::[]scope>strong <br> tokenColors::[]scope>support.class <br> tokenColors::[]scope>support.function <br> tokenColors::[]scope>support.function.construct <br> tokenColors::[]scope>support.type <br> tokenColors::[]scope>support.type.exception <br> tokenColors::[]scope>text.html.basic constant.character.entity.html <br> tokenColors::[]scope>text.html.basic constant.other.inline-data <br> tokenColors::[]scope>text.html.basic meta.tag.sgml.doctype <br> tokenColors::[]scope>text.html.basic punctuation.definition.entity <br> tokenColors::[]scope>text.html.markdown beginning.punctuation.definition.list <br> tokenColors::[]scope>text.html.markdown beginning.punctuation.definition.quote <br> tokenColors::[]scope>text.html.markdown constant.character.math.tex <br> tokenColors::[]scope>text.html.markdown constant.other.reference.link <br> tokenColors::[]scope>text.html.markdown markup.fenced_code.block <br> tokenColors::[]scope>text.html.markdown markup.fenced_code.block punctuation.definition <br> tokenColors::[]scope>text.html.markdown markup.inline.raw <br> tokenColors::[]scope>text.html.markdown markup.inline.raw punctuation.definition.raw <br> tokenColors::[]scope>text.html.markdown markup.italic <br> tokenColors::[]scope>text.html.markdown markup.quote <br> tokenColors::[]scope>text.html.markdown markup.underline.link <br> tokenColors::[]scope>text.html.markdown punctuation.definition.constant <br> tokenColors::[]scope>text.html.markdown punctuation.definition.function.math.tex <br> tokenColors::[]scope>text.html.markdown punctuation.definition.heading <br> tokenColors::[]scope>text.html.markdown punctuation.definition.math.begin <br> tokenColors::[]scope>text.html.markdown punctuation.definition.math.end <br> tokenColors::[]scope>text.html.markdown punctuation.definition.string <br> tokenColors::[]scope>text.html.markdown punctuation.math.operator.latex <br> tokenColors::[]scope>text.html.markdown string.other.link.description <br> tokenColors::[]scope>text.html.markdown string.other.link.title <br> tokenColors::[]scope>text.xml entity.name.tag.namespace <br> tokenColors::[]scope>text.xml keyword.other.doctype <br> tokenColors::[]scope>text.xml meta.tag.preprocessor entity.name.tag <br> tokenColors::[]scope>text.xml string.unquoted.cdata <br> tokenColors::[]scope>text.xml string.unquoted.cdata punctuation.definition.string <br> tokenColors::[]scope>token.debug-token <br> tokenColors::[]scope>token.error-token <br> tokenColors::[]scope>token.info-token <br> tokenColors::[]scope>token.warn-token <br> tokenColors::[]scope>variable.language <br> tokenColors::[]scope>variable.other <br> tokenColors::[]scope>variable.other.constant.elixir <br> tokenColors::[]scope>variable.other.readwrite.module.elixir <br> tokenColors::[]scope>variable.parameter <br> tokenColors::[]settings::background <br> type |




# 📝 2024/09/08

## URL scheme どうすればいいか問題

たぶん Base64 ではない気がするのよね。。。

- [Custom URL Scheme の処理をシンプルに書く #Objective-C - Qiita](https://qiita.com/naonya3/items/c55e6151b4ff6ab5725f)

  - `UIApplicationDelegate` で処理が書かれている？

- [Defining a custom URL scheme for your app | Apple Developer Documentation](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app)

### ちなみに

[GitHub - omz/PythonistaAppTemplate: Xcode template for building standalone apps from Pythonista (iOS) scripts](https://github.com/omz/PythonistaAppTemplate)

Pythonista3 でアプリを配布できるリポジトリ内には、書かれていなかった

## ChatGPT 4o mini(free)君に、Pythonista3 Theme 設定のスキームについて聞いてみる

- [pystaColorThemeDev/scripts/dists/dumps/minimumTemplateDefaultThemeSample.json at main · pome-ta/pystaColorThemeDev · GitHub](https://github.com/pome-ta/pystaColorThemeDev/blob/main/scripts/dists/dumps/minimumTemplateDefaultThemeSample.json)

```
pythonista3://?action=add-theme&theme-data=eNqtVU1v2zAMvedXBN61BtrutvPQ2y5r7wYt0Y5mSQxkCmtW9L9Plu1lij8SF80tpN_jI8WPt91-nzGURQmiqR15K7P9t3329HQfftnd6GbFGicerSwW1psS3cTXCjpi25nfwt9gkCRadsrWZ1uwCtI0AUdPRZbzlk9DXMWglcii973_KBMHFE1Jr7kkiynt4OmM7Dz-Yx2_7Iwpl4a2XZD2paqittngq3FTBMlU5bno-TTY3VmHs-hyB1L5qPAxYW3w9JucXK9qgjhgoLJ1_pBgLupdkpbZtEISq4-935Svs-TDs14Rks-9fkXOAPNyR80-25j8123JR8smxPXM5pIKI9UkGMZXziWGJgBWZCMwNAy6bvhS7NHRLxS8TSZDfTWepctQ56G_secqb8XIdyOEoW1mJnt5UOakdyunQfI83wWP24o1ZvGZU-CVDj38gfp066TUJJrAD4437S4yBi1_3iY2JL3GDeJvOQUJIJQcvOZbELsBFfarWztsMa8KjNKn6PuBVlP-E2uvwf33Sav-xNQe7vt7qPrKJVwrYQblRdeeE2ftmTGoDBt87ojiEUIzkyvitE_vb-nAnVaP9yFMqgWll0KMApYpLJg-tFFWGW9e0Bw1MH7v83o5oMFnCDYcQoY8ixY1xoYuLsu1e_8LEW0lgg~~
```

- [pystaColorThemeDev/scripts/dists/dumps/nord-color-theme.json at main · pome-ta/pystaColorThemeDev · GitHub](https://github.com/pome-ta/pystaColorThemeDev/blob/main/scripts/dists/dumps/nord-color-theme.json)

```
pythonista3://?action=add-theme&theme-data=eNqdVk1zmzAQvedXeMjVzBjb8dDcDCa39tA_wAhYY4rQeoQ0jZvJf6-QoEYY45Kjd3lv3672wx9Pi4UjSBInJC1zjpJlzuJ14ayjzXa7cpaNOyO8jEu4JEi49gouYdkBRSEoaMzBP0TRN4OhRcIJvygvE9q5Cbbrl3XnZBAzWSXAtW8bvux2e-NLCB9q6UOPyIR7JFVBL9r3HRhF9yfkkhLe-6Qu_mhR3krb6hTPUDeGD_WzyQnTWvCC5VebsqZI0Ujy34IwCDSh9hhScWlTLQShRepo76f5yElPkJYJvrsZMrBpW0-_dq0K82VjtLkoqes70p5bbaPBJ-PaCMxsldequ71gO28X-f61EClyBtzlJCukVri2WFWb_EbTJWNV9fZe6NnKT6CoWO56FmZQ7wRp5txWKIPj197vlq-xuO2zPhDijr3-EXlFhLjfUV0lR5PfzEteW2YhHmc2lpQa1NLCCHgXbgaqCYgokGmgahjgzUjb2DPHX5CKeTIFyR_GYzgMdV0lI3UPtn60PwweS7K04xtrHj9cHVZDZXU5Mtk3U7mckt6snBJQivEuWM8rVpfFxBSYRGZMgSyo6uEv1KdZJwnFtFT8hItZuwurCtg9yHAB_UfbVphJCtObwQJMnoL9Joj80AaokhNJ70luD6FBPLUo598p7L2KM3V2TYy4aaSb-5pLIUBdSrVruyOqbuSqhdZwJqrtkMd6Lm_vrznOE8HFSc0UIwXth-hzdALuUzBSmdA_moNgWFUqcQ0UdHdd_xyoPwBRqEr8-RfVtCsH
```

- [pystaColorThemeDev/scripts/dists/dumps/iceberg.color-theme.json at main · pome-ta/pystaColorThemeDev · GitHub](https://github.com/pome-ta/pystaColorThemeDev/blob/main/scripts/dists/dumps/iceberg.color-theme.json)

```
pythonista3://?action=add-theme&theme-data=eNqtVk1zmzAQvedXeMg1zACmGOcWEx966KV_gBFijRWE1iPENG4m_71CyLXBYIdOj97lvX272g9_PCwWjiJZmhFaFhIbkTuL54XjbX3P_-Y8te6cyDIt4ZghkcarZANPJ6BiioPBJFESv_odhrNMEnnUXqGuCDkTkIqmykAaXxiGm5UFZkQOtfiRHwfWvUOh3B2pGD8a3w8QHN2fUDScyItPavbbiPI9Y6spHqBuDR_6Z5sT0lpJJoqzTVspcuwkbcLNNg4MofF0pOpoU2WKcEYd4_3sPnLoHmiZ4bubo4A-rfVc1s6q6L5sjX0uTup6QtojjWic--PBb8btIzDvqzxX3b0IRrz1kq7OhaAoBUhXkpw1RmHQY9Vt8gu7LhmRHocvXhL1le9BU4nC9XuYQb0z5LlzXaEcdhORLnrxa3ytxbXPekeIO_b6O5QVUWq6ox6jbOXF6_Hkl_OSN5ZZiPuZjSWlB7XsYRS8KzcH3QREMRQGqBsGZDvSfexB4htQNU-mIsXdeAKHoc6rZKTuL7qBk9XgsRpBT3zTzTNQVpcjkz09KGPS25VTAjZqvAuCecU6ZfE_p6BhXPfwP9SnXScZR1pqfiLVnCGgWFUgpiDRxiDmbOIK84ZPPVS83sRJ0AfcPAVjAF1y0nD1lfo8WJTz9xTaLWjP3eSpszHStpGu7mvRKAX6Uupda4_o5YGt4UB026FMzVwOmU_H-UZwtdczJQjjUyFOAgYU28BfdmfTEaTqQn-noMezsMQ6m7QGDqbBzv8PglWQhLrKn38ANGArig~~
```

### 回答

ごにょごにょと、サンプルで出したテキストで事例をだしつつ、それっぽいコードブロックで案内をしているが

Base64 エンコードと言っている。しかし、以前に変換してみたときは、それっぽい文字列にならなかった記憶なんよな。。。

「JSON」 データの変換だと違うのかしら？

> 変換後の文字列は、iOS アプリ「Pythonista3」の URL スキームの形式で、`action=add-theme` というアクションと、Base64 エンコードされた `theme-data` を含んでいます。この `theme-data` には、JSON 形式のテーマ設定が Base64 エンコードされたデータが含まれています。

> この変換プロセスでは、JSON データを Base64 でエンコードし、そのエンコードされたデータを URL スキームのパラメータとして設定しています。これにより、JSON データを安全に URL 形式で送信し、アプリケーションがそのデータを処理できるようにしています。

# 📝 2024/09/07

## VSCode の theme たち

有名どころをそれなりに収集して、一般的な要素を把握できるようにしていく

`tokenColors` の要素たちが、いい感じに振り分けができると嬉しい

### アウトプットイメージ

全体的に設定されている要素と、個別で設定されている要素に分けて`.md` 形式で吐けるように

- 全体であたっているもの
- 個別で設定しているもの

意外に、一部の共通する部分をどう表示させて見せることができると。。。

### 探す

### サイト

- [2024 VSCode のおすすめテーマはこれだ！ | Designup](https://designup.jp/vscode-best-themes.html)
- [19 Best VSCode Themes to Boost Your Coding Experience (2024)](https://snappify.com/blog/best-vscode-themes)
- [23 Best VS Code Themes in 2024 - DEV Community](https://dev.to/ikoichi/23-best-vs-code-themes-in-2024-45g1)
  - 直リンなし
- [Search results - tag:color-theme | Visual Studio Code , Visual Studio Marketplace](https://marketplace.visualstudio.com/search?term=tag%3Acolor-theme&target=VSCode&category=Themes&sortBy=Relevance)
  - マケプレ
    - tag: tag:color-theme
    - Showing: Themes
    - Sort By: Relevance

### GitHub リンク

- [GitHub - Binaryify/OneDark-Pro: Atom's iconic One Dark theme for Visual Studio Code](https://github.com/Binaryify/OneDark-Pro)
- [GitHub - DevShayan/notepadpp-color-theme](https://github.com/DevShayan/notepadpp-color-theme)
- [GitHub - thehelpfultipper/pink_panda_vsctheme](https://github.com/thehelpfultipper/pink_panda_vsctheme)
  - ファイル名にスペースが存在する。。。
- [GitHub - primer/github-vscode-theme: GitHub's VS Code themes](https://github.com/primer/github-vscode-theme?tab=readme-ov-file)
  - `.json` はなく build が必要そう
  - 要素の項目など確認できそう
- [GitHub - tokyo-night/tokyo-night-vscode-theme: A clean, dark Visual Studio Code theme that celebrates the lights of Downtown Tokyo at night.](https://github.com/tokyo-night/tokyo-night-vscode-theme)
- [GitHub - robb0wen/synthwave-vscode: Synthwave inspired colour theme for VS Code 🌅🕶](https://github.com/robb0wen/synthwave-vscode)

### メモ

`.json` 意外にも`.xml` 形式もありそう？

## `yield` を使っている

### なんとなくの理解、、、

`for` やらで回して返す処理に関し、「返す」値の変数を宣言せずに、返せる。

```.py
v = []
```

のような、受け皿を作らなくも良い。

ジェネレータが返ってくるので、実際に使う先では、`list` 等でキャストしてあげる。

### 型ヒントはどう書くのか

現在は、型ヒントを書かずにしている。

`import` で`typing` 関係をわざわざ持ってくるのもなー。という状態。

`typing` を呼び出してからの詳細は調べていない。

## コードの遠回りな書き方

無駄に関数を宣言したり、処理の手順や変数の宣言に悩み中。。。

一人でやりつづけていると、自分の考えが凝り固まって、柔軟な考え方を受容できる能力が落ちていまうのが怖い。

レビューを受けつつコードを書いていきたいが、レビューを受けてもらうほど、みんなが使ってもらえるようなコードを書いていない。

こうやってエコーチャンバーが加速するのだろうなぁ。。。

### 関数の細分化と、何を持たせて、何を返すのか

基本的な書き方が、クソデカな要素を分割していき、必要に応じて関数を作っている。

その、事前に決まったクソデカ処理前提として書いているから、一般化ができていない気がする

パーツとして、機能振り分けができ、汎用的な要素を自前で用意できるような考え方にしていきたい

# 📝 2024/09/06

## color の相関性

Pythonista3 と VSCode であまり相関性が見られない、、、

ベースとしてるカラーから、独自に組んだ方が早いか？

hsv 変換して、近い色ピックアップするとか？

# 📝 2024/09/04

## Pythonista3 と VSCode 一気出し

ここに書き出すと、表示関係で面倒になるため、別`.md` へ吐き出し（予定）

## Dracula

Pythonista3 の方は、カラーに`#` が無かったため、`.json` にて追記

# 📝 2024/09/04

## vscode の theme color を`.md` として落とす

以下テスト

ここに書き出すと、表示関係で面倒になるため、別`.md` へ吐き出し（予定）

# 📝 2024/09/03

Theme の分析をしていきたい

[draftPythonistaScripts/markdown/colorTest.md at main · pome-ta/draftPythonistaScripts](https://github.com/pome-ta/draftPythonistaScripts/blob/main/markdown/colorTest.md)

## theme あつめ

VSCode の theme を dump していく

dracula theme は、CodeSandbox で`build` してから、格納

[GitHub - dracula/visual-studio-code: 🧛🏻‍♂️ Dark theme for Visual Studio Code](https://github.com/dracula/visual-studio-code)

## 分析

`.json` から、`value` を抜き出し、まとめる

`.md` の形式として吐き出す

### `.md` 吐き出し

table でまとめられたらいいけど、表示が変になるかな？

# 📝 2024/09/02

とりあえず書き出しはできたけど

- 書き換えの手間が多い
  - 項目増やすのに、数箇所書く
- クレジット入れたいな

# 📝 2024/09/01

## やはりミニマムから始めよう、、、

最大要素でやろうとしたけど、ミニマムから増やすか、、、

## 少々ハードコード気味に

### 分類分け

`name(top?)`, `colors`, `tokenColors` と分けて取ってみる

分類をどこで分けようか、自関数内？投げる手前の関数？

### 予備候補の書き方

配列で格納かしらね

[deep-dark-space/themes/Deep Dark Space-color-theme.json at main · smpl-ndrw/deep-dark-space · GitHub](https://github.com/smpl-ndrw/deep-dark-space/blob/main/themes/Deep%20Dark%20Space-color-theme.json)

`name`, の top の所、他にもありそうやな

`{"type": "dark",}` とかあったわ

とりま、Iceberg のみで考えるか

# 📝 2024/08/31

## 一旦整理

Pythonista3 の Theme フォーマットと、VSCode の Theme フォーマットを紐づける

`.json` で得たものを、`dict` としてわけわけするけども、どうも使い回しが気持ち悪い？

根本的に、自分の辞書構造の理解が定着していない。

### 想定できること、したいこと

- Pythonista3 側では、最大の項目要件を準備する
- VSCode の Theme は、複数の項目でマッチできるようにする
  - 設定されていない項目もあるので、サブとしてフォローさせておきたい
- VSCode でカバーできない部分は事前に設定しておきたい
- Theme ごとの紐付けを容易な設計にしたい

#### Pythonista3 側

- 実際のところ、どの項目がどこに反映されているのは不明点がある
- 最小要件が把握できていない
- `dark_keyboard`, `font-family`, `font-size` は、事前に固定になりそう
  - 可変的に指定できる窓口を用意していない
  - `font-family`, `font-size` は、命名的に個別設定かも
- 未設定の数値を`NONE` にするか、仮のカラーにするか決めてない

#### VSCode 側

- 項目ごとの反映場所がどこか不明なところがある
- 指定先の用語が把握できていないから、雑な部分がある
- 現在想定外の指定の方法について把握できていない
- `tokenColors` 内の、`scope` が配列の可能性がある

### 構造を考える

[vscode-iceberg-theme/src/themes/dark.ts](https://github.com/cocopon/vscode-iceberg-theme/blob/main/src/themes/dark.ts)

結構ゴリゴリと書いてるぽいから、やはり書いた方がいいか？

そうなると、`dict` の呼び出しをシュッとできるようになると、いいのだけど。。。

Python 側でドットアクセスができるようになって、何か嬉しいことってあるかしら？

`templateDefaultThemeSample` という地獄な名前

対応表みたいなのを作ったらええのか？

結局のところ、どこまでハードコードをするか？って問題か

`key` に`-` がついてる問題、`.css` と`.js` の style で考えたら、キャメルケースにするのが無難か

# 📝 2024/08/30

## 整理

vscode のテーマと Pythonista3 のテーマを揃える

編集に関しては、vscode でやるのが無難か？

双方の dump したものがあるから、繋ぎ合わせていく？

### img

Pythonista3 のテーマ設定スクショを格納

### 最小？最大？

```
min
#161821 background editor.background
#161821 bar_background tab.activeBackground
#c6c8d1 default_text tokenColors {scope: text}
#1e2132 gutter_background editorGutter.background
#0e1015 gutter_border tab.border
#161821 library_background sideBar.background
#444b71 line_number editorLineNumber.foreground
name name
#161821 separator_line menu.separatorBackground
#0e1015 tab_background tab.inactiveBackground
#c6c8d1 tab_title tab.activeForeground
#272c42 text_selection_tint editor.selectionBackground
#0e1015 thumbnail_border sideBar.border
#84a0c6 tint activityBarBadge.background

#c6c8d1 builtinfunction "scope": "entity.name.function",foreground
#c6c8d1 class "scope": "entity.name.class",foreground
#c6c8d1 classdef "scope": "entity.name.class",foreground
#a093c7 code "scope": "markup.inline.raw.string",foreground
#6b7089 codeblock-start "scope": "markup.fenced_code.block",foreground
#6b7089 comment "scope": "comment",foreground

#c6c8d1 default "scope": "text",foreground
#b4be82 docstring "scope": "punctuation.definition.block.tag.jsdoc",foreground
#6b7089 formatting  "scope": "markup.fenced_code.block",foreground
#c6c8d1 function  "scope": "entity.name.function",foreground
#c6c8d1 functiondef  "scope": "entity.name.function",foreground
#84a0c6 keyword keyword
#a093c7 number constant
#89b8c2 string "scope": "string",
#a093c7 task-done "entity.other.attribute-name",

scopes
```

Pythonista3 上でどこが何に対応してるか確認？

```
- max_main_keys
  - __tint
  - background
  - bar_background
  - dark_keyboard
  - default_text
  - editor_actions_icon_background
  - editor_actions_icon_tint
  - editor_actions_popover_background
  - error_text
  - font-family
  - font-size
  - gutter_background
  - gutter_border
  - interstitial
  - library_background
  - library_tint
  - line_number
  - name
  - scopes
  - separator_line
  - tab_background
  - tab_title
  - text_selection_tint
  - thumbnail_border
  - tint

- max_scopes_keys
  - bold
  - bold-italic
  - builtinfunction
  - checkbox
  - checkbox-done
  - class
  - classdef
  - code
  - codeblock-start
  - comment
  - decorator
  - default
  - docstring
  - escape
  - formatting
  - function
  - functiondef
  - heading-1
  - heading-2
  - heading-3
  - italic
  - keyword
  - link
  - marker
  - module
  - number
  - project
  - string
  - tag
  - task-done

- min_main_keys
  - background
  - bar_background
  - default_text
  - gutter_background
  - gutter_border
  - library_background
  - line_number
  - name
  - scopes
  - separator_line
  - tab_background
  - tab_title
  - text_selection_tint
  - thumbnail_border
  - tint

- min_scopes_keys
  - bold
  - bold-italic
  - builtinfunction
  - checkbox
  - checkbox-done
  - class
  - classdef
  - code
  - codeblock-start
  - comment
  - default
  - docstring
  - formatting
  - function
  - functiondef
  - heading-1
  - heading-2
  - heading-3
  - italic
  - keyword
  - link
  - module
  - number
  - project
  - string
  - tag
  - task-done

```

# 📝 2024/08/29

## Pythonista3 が起動時に落ちる

```.json
{
  "name": "hoge"
}
```

だけだと、落ちる

最低条件がどこまでか知りたいけど、時間かかるから面倒

# 📝 2024/08/28

## color

[Theme Color | Visual Studio Code Extension API](https://code.visualstudio.com/api/references/theme-color)

### 対応確認

```
#161821 background: editor.background
#161821 bar_background: activityBar.background
#c6c8d1 default_text: tokenColors {scope: text}
#e27878 error_text: editorError.foreground
#1e2132 gutter_background: editorGutter.background
#0e1015 gutter_border: panel.border
#1e2132 library_background: menu.background
#161821 library_tint: menu.separatorBackground
#444b71 line_number: editorLineNumber.foreground
#e2a478 builtinfunction: entity.name.function.method
class:
```

### Pythonista3 default

```
- Default: 21
  - __tint:
  - background:
  - bar_background:
  - default_text:
  - editor_actions_icon_background:
  - editor_actions_icon_tint:
  - editor_actions_popover_background:
  - error_text:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - line_number:
  - name:
  - scopes: 29
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - decorator: 1
      - color:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - marker: 3
      - box-background-color:
      - box-border-color:
      - box-border-type:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- PythonistaDark: 21
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 28
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - decorator: 1
      - color:
    - default: 1
      - color:
    - docstring: 1
      - color:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

```

## 各 theme の要素数など

```
- Theme09_Editorial: 20
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - line_number:
  - name:
  - scopes: 27
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - default: 1
      - color:
    - docstring: 1
      - color:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Theme04_SolarizedDark 2: 21
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 27
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Theme10_WWDC16: 21
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 28
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 1
      - color:
    - decorator: 1
      - color:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Default: 21
  - __tint:
  - background:
  - bar_background:
  - default_text:
  - editor_actions_icon_background:
  - editor_actions_icon_tint:
  - editor_actions_popover_background:
  - error_text:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - line_number:
  - name:
  - scopes: 29
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - decorator: 1
      - color:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - marker: 3
      - box-background-color:
      - box-border-color:
      - box-border-type:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Theme11_Ayu: 21
  - background:
  - bar_background:
  - default_text:
  - editor_actions_icon_background:
  - editor_actions_icon_tint:
  - editor_actions_popover_background:
  - error_text:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 29
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 1
      - color:
    - decorator: 1
      - color:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - marker: 3
      - box-background-color:
      - box-border-color:
      - box-border-type:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Theme03_SolarizedLight: 21
  - background:
  - bar_background:
  - default_text:
  - editor_actions_icon_background:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 28
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - escape: 1
      - background-color:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Theme01_Dawn: 17
  - background:
  - bar_background:
  - default_text:
  - error_text:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - line_number:
  - name:
  - scopes: 28
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - decorator: 1
      - color:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- PythonistaDark: 21
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 28
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - decorator: 1
      - color:
    - default: 1
      - color:
    - docstring: 1
      - color:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Theme08_Oceanic: 21
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 27
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Theme02_Tomorrow: 20
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - line_number:
  - name:
  - scopes: 27
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - default: 1
      - color:
    - docstring: 1
      - color:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Theme05_CoolGlow: 21
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 27
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Theme06_Gold: 20
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - line_number:
  - name:
  - scopes: 27
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - default: 1
      - color:
    - docstring: 1
      - color:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- Theme07_TomorrowNight: 20
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - line_number:
  - name:
  - scopes: 27
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - default: 1
      - color:
    - docstring: 1
      - color:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- MyTheme: 18
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - library_background:
  - line_number:
  - name:
  - scopes: 29
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - decorator: 1
      - color:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - escape: 1
      - background-color:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- 59962EDD-7900-44D0-9947-35D7739964A6: 21
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 27
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- BCD46A04-50DD-4212-A800-39FDAEC8856F: 21
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 27
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:

- tmpMergeDumps: 25
  - __tint:
  - background:
  - bar_background:
  - dark_keyboard:
  - default_text:
  - editor_actions_icon_background:
  - editor_actions_icon_tint:
  - editor_actions_popover_background:
  - error_text:
  - font-family:
  - font-size:
  - gutter_background:
  - gutter_border:
  - interstitial:
  - library_background:
  - library_tint:
  - line_number:
  - name:
  - scopes: 30
    - bold: 1
      - font-style:
    - bold-italic: 1
      - font-style:
    - builtinfunction: 1
      - color:
    - checkbox: 1
      - checkbox:
    - checkbox-done: 2
      - checkbox:
      - done:
    - class: 1
      - color:
    - classdef: 2
      - color:
      - font-style:
    - code: 2
      - background-color:
      - corner-radius:
    - codeblock-start: 1
      - color:
    - comment: 2
      - color:
      - font-style:
    - decorator: 1
      - color:
    - default: 1
      - color:
    - docstring: 2
      - color:
      - font-style:
    - escape: 1
      - background-color:
    - formatting: 1
      - color:
    - function: 1
      - color:
    - functiondef: 2
      - color:
      - font-style:
    - heading-1: 1
      - font-style:
    - heading-2: 1
      - font-style:
    - heading-3: 1
      - font-style:
    - italic: 1
      - font-style:
    - keyword: 1
      - color:
    - link: 1
      - text-decoration:
    - marker: 3
      - box-background-color:
      - box-border-color:
      - box-border-type:
    - module: 1
      - color:
    - number: 1
      - color:
    - project: 1
      - font-style:
    - string: 1
      - color:
    - tag: 1
      - text-decoration:
    - task-done: 2
      - color:
      - text-decoration:
  - separator_line:
  - tab_background:
  - tab_title:
  - text_selection_tint:
  - thumbnail_border:
  - tint:
```

# 📝 2024/08/27

## 思いつき

- vscode の theme コンバートできたらおもろい？

## 辞書

[Python でネストした dict をマージしたい #DeepMerge - Qiita](https://qiita.com/rana_kualu/items/7c957851a058c1ae7808)

[Python で 2 つの辞書型(dict 型)をマージ | レコチョクのエンジニアブログ](https://techblog.recochoku.jp/5748)

# 📝 2024/08/25

パスの空白は`%20` へ変換？`webbrowser` であれは、URL として読むからそうか

直での path で開けない、ディレクトリを戻る作業をして表示ができる状態になっている

「9 階層上がる」とハードコード指定してるけど、しゃあないか

## アプリのディレクトリ構造についての理解

`home = os.getenv('CFFIXED_USER_HOME')` という部分、全く知らなかったので調査

[#おまけ | simctl コマンドを使ってみる #iOS - Qiita](https://qiita.com/tamaki/items/02eb43253193b950b08f#%E3%81%8A%E3%81%BE%E3%81%91)

# 📝 2024/08/24

チャレンジ再開

ここはテスト開発用として、完成したら別リポジトリを用意予定

## 方針

- theme の設定を理解
- 本家からぬるっとコンバート
- モードを切り替える

## 今後

- サクッと切り替えができるスクリプト
- 完成版の URL を生成するやつ
- 対象項目をピックアップして、関連性の確認
- Pythonista3 本体内の Theme 設定のコード
  - 表示サムネイル
  - 共有時の URL 発行

```
pythonista3://?action=add-theme&theme-data=eNqtWM2PGzUUv-9fYaWHXjYlyX5zQdttS5FahNhKXJAiz4yTuJnYwfZ0m1aV2o2EQLQSFw7lgFSpIODQStxA_DcjoH8Gz_Z82TOTbBZmtNqM37P9vn7vPfvxFkKdcaIUEcMAh9Ox4AmLhsNhyGczwlQHvY869yYElUQU8pgLxEdIwXhMGUEsmQVEaEIyY4gzSyEjhSSNSM5KIqq4uNbZ1nsqmi2-d3C0e71nBwNclcKQb5knJ7eSchW4iOBfXXxHZssFPzEISOZYYEWkodhl0EjwWV3kCIvpcEoWAcfCN9FnEwL8sCZHiSQII80MlpChIIShfFa2kgz5nEhviVtczLACu4zRCGR9gAXliURTyiJpJCcPFaKsKheqzOFzRWE_hAUBq89ojI00J6enSKpFTKSzt97xMXzCAMh2BgYpR2DMmMtIdbw72Du81TGEJ9tbGTUiQczDaVcqLJSnx4dU3U6CrtkUyQVT-CGa0PEkhj8jKWVSiSTMxB0pEzkQJmZJZJa0smZbOZKVMdAthbxy2NPvoJdNMxMFI6IrcEQTo-3AVSHG0nfAiR5DDM8gGLBEEBdK2x0jw2zExkxRrAUvBZyQcBrwh37MYTmd47lWLWMoZowSZnSPyKjF5oP-wf7BzVKXEWfK2tOQAx5HrkMs_jwRPjaDspRUa9Gy4xWzJXFXjQgYESvL0jDp6Gj_cPfEnUMVjmnoTPCkzzicWUFCYwiN3DKeItc1tQuRn9ObfFTQQhzHhc6QnaaOMBpE3Uwx4DbrQywRofOYK9Rc8PskVK2OzejFXuBPnMQ-_w07atC7bYA9j7FGsUbziAIuEYyZrzOqJohxJOckpDhGM4IZ4MXBQgV2ba60WDjsudrk9lkdci5GssjtRpy5IMwpehCgTIpIzTn1oLPWjEdJTDzbfLJQE_CYpdWdSmdzDr9AWUX0HFmDkJ9BN44PDaWujUg_6ICCMFQ7SzUeKqZB_gLHeDNOzSAUREhoOC6FnRDIQWzc7a9CRR3TeqRJJkeQfO3BZmsXInkb3CEPSIz6KKPXdRg0ThjUJ4yKwrRZmOYb7TRutNMu2c5mFqgk4csEEUyjjDqFwOyxkQyVXRsMlFlne4M0qrAfkx_ptoZKVGYtSDa37929o_-f6f6H8bMPigzGw8bIznEKeYyafk-2hLopMf9jXSsqUJuPQAtbnMuU3pQvrLwtUp3c3OvvHq1IfX6boGkkQitKvFfPNsi54MK19Ypxv1QRGYIgfj6a8ATyBZSpAAfxAgXElB_LC138BPreEByoOxvfo9soSBSKOJHsqu6RyUz3khGHjAixUC1KusL6WIUhpKgqes6iQ2kzxP7h4MZep96g1dG5pkdrwKUCNzVUsDIR7ZunCrUmo2sDTQlPlBehOWRaVt_dPTjqH22E4jJ1errfhSNFxM8YKjkqXqx1pCsrdq3UdNd3blW22nnATzzMJArT10vyRUJYWIkGW_FbTLZ_c7d_fOjDInOinwjA23LigFGz-j1Zy0498zQ1sL42DT2AxdEFziYkGPUjT5_szOUDB7NxgscEZeSKTy2XDwb7u2TLWtILlqGtTB5zFneXzo6GhBUHaM1TnqLhg4gRDonOEwrOcYUI9_HFp5QC4GBoEkbVLYZipaePSMOZPnNudhg2zVoI6_JYJzqm7x4ekfy2YQL5h2EaN94Q1LVtuC6QkEDVmT7M2649O4mfhoLOFbpDA4HFoskMl1-rsI_G0rBMoZ3jPf1m53l7gQE10hxhTJ-4o9_s0iI7lejYXad1btAGnzmhX1Fu7ZRCB-PJEZ7ReHEJX9qJ1-o6mRV2zJO5WisqSUzsCaHxnknXj7UBP4Em4iqUFCrhxLYwNSd31D1Nk3BAY4lvlPTp83T5Zbr8M13-kD59kS5fpctv0uWPeuTZT-n5y_TZm5Lh2Zt3r37-5_Uff337In16XhqrdiNns92xfj1gaEq_V8Co7RKvrmDTjR5lUEzoA9AeB42YvsCkQgltMecMnOUrEnUaxLUa9vTb8YN-3YVe5RKyAJM14bV8LQOp_2id9XhPz39Pz9-my1_T5Xfp-ffp8iuULn9Jz1-b75f6N9DA68vnf798--7r3xyvr7yAzRHSJphzVelch1ofmKfjQ9E2FoTFvPspGScxFq0o2qxCaJHMrUaxiAV1ImQu5apqsWZ6vXJslNFhlm1QW_PaSvZidzf3rovSgtvGa14CFOdxgMXn72n4GC3di3KvdFlv9vXbcC2tqSNo4ElL2NfyiHvlfllUZDoY6fV3mRAumkTWraJtvvXkX9BzlRg~
```
