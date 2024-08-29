from pathlib import Path
import json
from objc_util import ObjCClass

theme_path = Path('./vscodeThemes/iceberg.color-theme.json')
theme_json = json.loads(theme_path.read_text())


print(theme_json['name'])

