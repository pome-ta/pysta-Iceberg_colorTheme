from pathlib import Path
import json

theme_path = Path('./vscodeThemes/iceberg.color-theme.json')
theme_json = json.loads(theme_path.read_text())


print(theme_json['name'])
