from pathlib import Path
import json

from dataclasses import dataclass

from tmpDict import tmp_theme_dict


@dataclass
class DataPalette:
  background: str = '#ff0000'
  bar_background: str = '#ff0000'
  dark_keyboard: bool
  default_text: str = '#ff0000'
  editor_actions_icon_background: str = '#ff0000'
  editor_actions_icon_tint: str = '#00ff00'
  editor_actions_popover_background: str = '#0000ff'
  error_text: str = '#ff0000'

  gutter_background: str = '#ff0000'
  gutter_border: str = '#ff0000'
  interstitial: str = '#ff0000'
  library_background: str = '#ff0000'
  library_tint: str = '#ff0000'
  line_number: str = '#ff0000'
  name: str = 'templateDefaultThemeSample'

  scopes: dict

  separator_line: str = '#ff0000'
  tab_background: str = '#ff0000'
  tab_title: str = '#ff0000'
  text_selection_tint: str = '#ff0000'
  thumbnail_border: str = '#ff0000'
  tint: str = '#ff0000'


vscode_theme_path = Path(
  Path(__file__).parent, './vscodeThemes/iceberg.color-theme.json')
vscode_theme_dict = json.loads(vscode_theme_path.read_text())


def convert_palette(vs_dict: dict) -> dict:

  pass

