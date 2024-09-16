from pathlib import Path
import json

ROOT_PATH = Path(__file__).parent


def insert_theme(json_path: Path) -> None:

  def get_user_themes_dir() -> Path | None:
    try:
      # todo: 一応
      from objc_util import ObjCClass
    except ModuleNotFoundError:
      return None
    _path_objc = ObjCClass('PA2UITheme').sharedTheme().userThemesPath()
    _path = Path(str(_path_objc))
    return _path if _path.exists() else None

  user_themes_dir = get_user_themes_dir()
  if user_themes_dir is None:
    return
  json_name = json_path.name
  json_str = json_path.read_text()

  new_theme = Path(user_themes_dir, json_name)
  new_theme.write_text(json_str, encoding='utf-8')


if __name__ == '__main__':
  dumps_dir = '../dists/dumps'
  target_json = 'myOceanic.json'

  theme_path = Path(ROOT_PATH, dumps_dir, target_json)
  insert_theme(theme_path)

