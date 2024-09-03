from pathlib import Path

theme_path = Path(Path(__file__).parent, './vscodeThemes')


for p in theme_path.iterdir():
  print(p.name)
