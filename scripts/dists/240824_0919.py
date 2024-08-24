from pathlib import Path
import webbrowser

from objc_util import ObjCClass

main_root_str = str(ObjCClass('NSBundle').mainBundle().resourcePath())

main_root_path = Path(main_root_str)

#webbrowser.open(f'pythonista3://{main_root_path}')
