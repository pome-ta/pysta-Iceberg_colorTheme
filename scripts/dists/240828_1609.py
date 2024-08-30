from pathlib import Path
import json
from objc_util import ObjCClass

themes_path = Path(str(ObjCClass('PA2UITheme').sharedTheme().userThemesPath()))

target_path = Path('./dumps/myOceanic.json')

move_path = Path(themes_path, target_path.name)

json_str = target_path.read_text()
move_path.write_text(json_str, encoding='utf-8')

