from dataclasses import dataclass

# todo: 型`str` は色情報もあるので、今後分けていきたい

@dataclass
class Theme:
    background: str = '#ff0000'
    bar_background: str = '#ff0000'
    default_text: str = '#ff0000'
    gutter_background: str = '#ff0000'
    library_background: str = '#ff0000'
    line_number: str = '#ff0000'
    name: str = '#ff0000'
    separator_line: str = '#ff0000'
    tab_background: str = '#ff0000'
    tab_title: str = '#ff0000'
    text_selection_tint: str = '#ff0000'
    thumbnail_border: str = '#ff0000'
    tint: str = '#ff0000'

theme = Theme(**{'background': '#0000ff'})

x = 1