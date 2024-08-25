import webbrowser
import urllib.parse
from objc_util import ObjCClass

theme_path = str(ObjCClass('PA2UITheme').sharedTheme().userThemesPath())
#url_path = '/private' + urllib.parse.quote(theme_path)
url_path = '/..' * 9 + urllib.parse.quote(theme_path)

webbrowser.open(f'pythonista3://{url_path}')

