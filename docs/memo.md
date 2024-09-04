# 📝 2024/09/04


## vscode のtheme color を`.md` として落とす


以下テスト


### solarized-light-color-theme.json

| color | name |
| --- | --- |
| #00000014 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #002B36 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #073642 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #081E2580 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #268BD2 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #2AA198 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #2AA19899 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #567983 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #584C27 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #584C27AA | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #586E75 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #586E7580 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #586E75AA | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #657B83 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #6C6C6C | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #6C71C4 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #7744AA40 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #839496 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #859900 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #878B9180 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #93A1A1 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #AB395B | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #AC9D57 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #B49471 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #B58900 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #B58900AA | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #CB4B16 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #CCC4B0 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #D1CBB8 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #D33682 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #D3AF86 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #D3CBB7 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #D9D2C2 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #DC322F | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #DDD6C1 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #DDD6C199 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #DDD6C1AA | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #DFCA88 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #DFCA8844 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #DFCA8866 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #EEE8D5 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #F7F0E0 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #FDF6E3 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |
| #FFFBF2 | colors::activityBar.background <br> colors::activityBar.foreground <br> colors::activityBarBadge.background <br> colors::badge.background <br> colors::button.background <br> colors::debugExceptionWidget.background <br> colors::debugExceptionWidget.border <br> colors::debugToolBar.background <br> colors::dropdown.background <br> colors::dropdown.border <br> colors::editor.background <br> colors::editor.foreground <br> colors::editor.lineHighlightBackground <br> colors::editor.selectionBackground <br> colors::editorCursor.foreground <br> colors::editorGroup.border <br> colors::editorGroup.dropBackground <br> colors::editorGroupHeader.tabsBackground <br> colors::editorHoverWidget.background <br> colors::editorIndentGuide.activeBackground <br> colors::editorIndentGuide.background <br> colors::editorLineNumber.activeForeground <br> colors::editorWhitespace.foreground <br> colors::editorWidget.background <br> colors::extensionButton.prominentBackground <br> colors::extensionButton.prominentHoverBackground <br> colors::focusBorder <br> colors::input.background <br> colors::input.foreground <br> colors::input.placeholderForeground <br> colors::inputOption.activeBorder <br> colors::list.activeSelectionBackground <br> colors::list.activeSelectionForeground <br> colors::list.highlightForeground <br> colors::list.hoverBackground <br> colors::list.inactiveSelectionBackground <br> colors::minimap.selectionHighlight <br> colors::notebook.cellEditorBackground <br> colors::panel.border <br> colors::peekView.border <br> colors::peekViewEditor.background <br> colors::peekViewEditor.matchHighlightBackground <br> colors::peekViewResult.background <br> colors::peekViewTitle.background <br> colors::pickerGroup.border <br> colors::pickerGroup.foreground <br> colors::ports.iconRunningProcessForeground <br> colors::progressBar.background <br> colors::quickInputList.focusBackground <br> colors::selection.background <br> colors::sideBar.background <br> colors::sideBarTitle.foreground <br> colors::statusBar.background <br> colors::statusBar.debuggingBackground <br> colors::statusBar.foreground <br> colors::statusBar.noFolderBackground <br> colors::statusBarItem.prominentBackground <br> colors::statusBarItem.prominentHoverBackground <br> colors::statusBarItem.remoteBackground <br> colors::tab.activeBackground <br> colors::tab.activeModifiedBorder <br> colors::tab.border <br> colors::tab.inactiveBackground <br> colors::tab.inactiveForeground <br> colors::tab.lastPinnedBorder <br> colors::terminal.ansiBlack <br> colors::terminal.ansiBlue <br> colors::terminal.ansiBrightBlack <br> colors::terminal.ansiBrightBlue <br> colors::terminal.ansiBrightCyan <br> colors::terminal.ansiBrightGreen <br> colors::terminal.ansiBrightMagenta <br> colors::terminal.ansiBrightRed <br> colors::terminal.ansiBrightWhite <br> colors::terminal.ansiBrightYellow <br> colors::terminal.ansiCyan <br> colors::terminal.ansiGreen <br> colors::terminal.ansiMagenta <br> colors::terminal.ansiRed <br> colors::terminal.ansiWhite <br> colors::terminal.ansiYellow <br> colors::terminal.background <br> colors::titleBar.activeBackground <br> colors::walkThrough.embeddedEditorBackground <br> tokenColors::[None]::settings::foreground <br> tokenColors::[['meta.embedded','source.groovy.embedded','stringmeta.image.inline.markdown','variable.legacy.builtin.python']]::settings::foreground <br> tokenColors::[comment]::settings::foreground <br> tokenColors::[string]::settings::foreground <br> tokenColors::[string.regexp]::settings::foreground <br> tokenColors::[constant.numeric]::settings::foreground <br> tokenColors::[['variable.language','variable.other']]::settings::foreground <br> tokenColors::[keyword]::settings::foreground <br> tokenColors::[storage]::settings::foreground <br> tokenColors::[['entity.name.class','entity.name.type','entity.name.namespace','entity.name.scope-resolution']]::settings::foreground <br> tokenColors::[entity.name.function]::settings::foreground <br> tokenColors::[punctuation.definition.variable]::settings::foreground <br> tokenColors::[['punctuation.section.embedded.begin','punctuation.section.embedded.end']]::settings::foreground <br> tokenColors::[['constant.language','meta.preprocessor']]::settings::foreground <br> tokenColors::[['support.function.construct','keyword.other.new']]::settings::foreground <br> tokenColors::[['constant.character','constant.other']]::settings::foreground <br> tokenColors::[entity.other.inherited-class]::settings::foreground <br> tokenColors::[entity.name.tag]::settings::foreground <br> tokenColors::[punctuation.definition.tag]::settings::foreground <br> tokenColors::[entity.other.attribute-name]::settings::foreground <br> tokenColors::[support.function]::settings::foreground <br> tokenColors::[punctuation.separator.continuation]::settings::foreground <br> tokenColors::[['support.type','support.class']]::settings::foreground <br> tokenColors::[support.type.exception]::settings::foreground <br> tokenColors::[invalid]::settings::foreground <br> tokenColors::[['meta.diff','meta.diff.header']]::settings::foreground <br> tokenColors::[markup.deleted]::settings::foreground <br> tokenColors::[markup.changed]::settings::foreground <br> tokenColors::[markup.inserted]::settings::foreground <br> tokenColors::[markup.quote]::settings::foreground <br> tokenColors::[markup.list]::settings::foreground <br> tokenColors::[['markup.bold','markup.italic']]::settings::foreground <br> tokenColors::[markup.inline.raw]::settings::foreground <br> tokenColors::[markup.heading]::settings::foreground <br> tokenColors::[markup.heading.setext]::settings::foreground |







# 📝 2024/09/03


Theme の分析をしていきたい

[draftPythonistaScripts/markdown/colorTest.md at main · pome-ta/draftPythonistaScripts](https://github.com/pome-ta/draftPythonistaScripts/blob/main/markdown/colorTest.md)


## theme あつめ

VSCode のtheme をdump していく


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


`name`, のtop の所、他にもありそうやな

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



`key` に`-` がついてる問題、`.css` と`.js` のstyle で考えたら、キャメルケースにするのが無難か



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
