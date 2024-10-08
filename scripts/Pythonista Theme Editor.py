#[Pythonista/theme/Pythonista Theme Editor.py at master · tdamdouni/Pythonista · GitHub](https://github.com/tdamdouni/Pythonista/blob/master/theme/Pythonista%20Theme%20Editor.py)

# coding: utf-8

# https://forum.omz-software.com/topic/2106/1-6-editor-themes-i-hate-myself-for-mentioning-it-but-i-will/11

# https://gist.github.com/omz/6c168b0c36ca3b23cacc
'''
Basic theme editor for Pythonista 1.6 (beta)

WARNING: Use at your own risk! User themes aren't "officially" supported, and
this may break in future versions. If you enter invalid JSON or anything else
that the app can't deal with, it *will* crash -- your input is not validated
in any way.
> 警告:使用は自己責任でお願いします! ユーザーテーマは「公式」にはサポートされておらず、将来のバージョンでは壊れる可能性があります。 無効なJSONやその他のものを入力した場合
を入力すると、アプリはクラッシュします。
'''

from objc_util import *
import os
import glob
import dialogs
import ui


def get_theme_names():
  '''Return names of all built-in themes'''
  res_path = str(ObjCClass('NSBundle').mainBundle().resourcePath())
  theme_paths = glob.glob(os.path.join(res_path, 'Themes2/*.json'))
  theme_names = [os.path.split(p)[1].split('.')[0] for p in theme_paths]
  return theme_names


def get_theme_path(name):
  '''Return absolute path of the JSON file of a built-in theme'''
  if name.startswith('User:'):
    return os.path.join(get_user_themes_path(), name[5:] + '.json')
  else:
    res_path = str(ObjCClass('NSBundle').mainBundle().resourcePath())
    theme_path = os.path.join(res_path, 'Themes2/%s.json' % name)
    if not os.path.exists(theme_path):
      raise IOError('Theme does not exist')
    return theme_path


def get_user_themes_path():
  '''Return folder path where user themes are stored'''
  home = os.getenv('CFFIXED_USER_HOME')
  user_themes_path = os.path.join(home, 'Library/Application Support/Themes')
  if not os.path.exists(user_themes_path):
    os.mkdir(user_themes_path)
  return user_themes_path


def get_current_theme_name():
  defaults = ObjCClass('NSUserDefaults').standardUserDefaults()
  return str(defaults.objectForKey_('ThemeName'))


def edit_theme(theme_name: str, theme_json: str = '') -> str:
  return dialogs.text_dialog('Edit Theme (%s)' % theme_name,
                             theme_json,
                             font=('Menlo', 12),
                             autocorrection=False,
                             spellchecking=False,
                             autocapitalization=ui.AUTOCAPITALIZE_NONE,
                             done_button_title='Apply')


@on_main_thread
def set_theme(name):
  defaults = ObjCClass('NSUserDefaults').standardUserDefaults()
  defaults.setObject_forKey_(name, 'ThemeName')
  ui_theme = ObjCClass('PA2UITheme').sharedTheme()
  ui_theme.loadThemeNamed_(name)
  # Reset the thumbnail cache for the script library:
  renderer = ObjCClass('PAScriptThumbnailRenderer').sharedThumbnailRenderer()
  renderer.reset()
  # Hide the keyboard (switching between light/dark doesn't look right otherwise):
  UIApp = ObjCClass('UIApplication')
  UIApp.sharedApplication().keyWindow().endEditing_(True)


def main():
  base_theme_name = get_current_theme_name()
  default_theme_path = get_theme_path(base_theme_name)
  try:
    with open(default_theme_path, encoding='utf-8') as f:
      theme_json = f.read()
  except Exception as e:
    theme_json = ''
    print(f'{e}:')

  edited_theme = edit_theme(base_theme_name, theme_json)

  if not edited_theme:
    return
  user_theme_path = os.path.join(get_user_themes_path(), 'testTheme.json')
  with open(user_theme_path, 'w', encoding='utf-8') as f:
    f.write(edited_theme)
  set_theme('User:MyTheme')
  dialogs.hud_alert('Theme saved')


if __name__ == '__main__':
  main()

