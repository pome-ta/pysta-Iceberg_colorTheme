from pathlib import Path
import json


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

