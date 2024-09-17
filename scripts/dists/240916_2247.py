"""
note: GitHub のパラメータ周り調査
raw は取れてるから、他の情報
  - リポジトリ名
  - 作者
"""


import requests

params = {
  'licenses': 'true',
}



if __name__ == '__main__':
  from pprint import pprint
  #url = 'https://github.com/pome-ta/pystaColorThemeDev/blob/main/scripts/dists/dumps/myOceanic.json'
  url = 'https://github.com/pome-ta/pystaColorThemeDev/'
  
  
  
  response = requests.get(url, params)
  pprint(response.headers)

