from pathlib import Path
import json


# 最大の要素と最小の要素を取得したい
# 最大: tmpMergeDumps.json


def get_json2dict(path: Path) -> dict:
    return json.loads(path.read_text())


_main_keys = []
_scopes_keys = []


root_path = Path(__file__)
dumps_path = Path(root_path.parent, 'dumps')


for p in dumps_path.iterdir():
  print(p.name)
  json_dict = get_json2dict(p)
  _main_keys.extend(list(json_dict.keys()))
  _scopes_keys.extend(list(json_dict['scopes'].keys()))


dumps_len = len(list(dumps_path.iterdir()))
max_main_keys = sorted(set(_main_keys))
max_scopes_keys = sorted(set(_scopes_keys))

count_main_dict = {k: 0 for k in max_main_keys}
count_scopes_dict = {k: 0 for k in max_scopes_keys}


for k in _main_keys:
  count_main_dict[k] += 1

for k in _scopes_keys:
   count_scopes_dict[k] += 1

min_main_keys = [k for k, v in count_main_dict.items() if v == dumps_len]
min_scopes_keys = [k for k, v in count_scopes_dict.items() if v == dumps_len]


print('- max_main_keys')
for k in max_main_keys:
  print(f'  - {k}')

print('')
print('- max_scopes_keys')
for k in max_scopes_keys:
  print(f'  - {k}')

print('')
print('- min_main_keys')
for k in min_main_keys:
  print(f'  - {k}')

print('')
print('- min_scopes_keys')
for k in min_scopes_keys:
  print(f'  - {k}')

x = 1
