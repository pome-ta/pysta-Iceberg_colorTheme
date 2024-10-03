from pathlib import Path
import json

#from .server import VSCodeThemeServer
#from .themeconverter import VSCodeThemeServer

# todo: Pythonista3 以外での`Path` 挙動クッション用
ROOT_PATH: Path = Path(__file__).parent
PY_LOCAL = Path(ROOT_PATH, '../../theme')


def get_user_theme_dir() -> Path | None:
  try:
    # xxx: 一応
    from objc_util import ObjCClass
  except ModuleNotFoundError as e:
    print(f'{e}:')
    return None
  _path_objc = ObjCClass('PA2UITheme').sharedTheme().userThemesPath()
  _path = Path(str(_path_objc))
  return _path

def to_dump(json_data: dict, info_data: dict | None = None) -> str:
  dump_data = json_data if info_data is None else json_data | info_data
  kwargs = {
    'indent': 1,
    'sort_keys': True,
    'ensure_ascii': False,
  }
  return json.dumps(dump_data, **kwargs)


def export(dump_theme: str, theme_file_name: str,
           target_dir: Path | None) -> None:
  if target_dir is None or not isinstance(target_dir, Path):
    raise ValueError(f'`target_dir` の値が不正です')

  if not target_dir.is_dir():
    target_dir.mkdir(parents=True)
  json_file = Path(target_dir, theme_file_name)
  json_file.write_text(dump_theme, encoding='utf-8')

'''
def build(convert_fnc,
          ts: VSCodeThemeServer,
          save_vscode: bool = True,
          vscode_dir: Path = None,
          save_pythonista: bool = True,
          pythonista_dir: Path = PY_LOCAL) -> str:
  converted = convert_fnc(ts)
  theme_dump = to_dump(converted)

  if save_vscode:
    export(ts.dump, ts.file_name,
           ts.tmp_dir if vscode_dir is None else vscode_dir)
  if save_pythonista:
    export(theme_dump, ts.file_name, pythonista_dir)

  if (user_theme_dir := get_user_theme_dir()) is not None:
    export(theme_dump, ts.file_name, user_theme_dir)

  return theme_dump
'''
