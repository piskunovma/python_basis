# import json
#
# data = {1: 2, 'key': '??????', 'key2': (1, 2, 3, 4)}
#
# data_list = [
#              {1: 2, 'key': '??????', 'key2': (1, 2, 3, 4)},
#              {1: 2, 'key': '??????', 'key2': (1, 2, 3, 4)},
#              {1: 2, 'key': '??????', 'key2': (1, 2, 3, 4)}
#             ]
#
# j_data = json.dumps(data)
#
# test_j_str = '{"1": 2, "key": "\u0441\u0442\u0440\u043e\u043a\u0430", "key2": [1, 2, 3, 4]}'
# print(json.loads((test_j_str)))
#
#
# print(j_data)

# import json
# import requests
#
# data_list = [
#              {1: 2, 'key': '??????', 'key2': (1, 2, 3, 4)},
#              {1: 2, 'key': '??????', 'key2': (1, 2, 3, 4)},
#              {1: 2, 'key': '??????', 'key2': (1, 2, 3, 4)}
#             ]
#
# # with open('data.json', 'w') as file:
# #     file.write(json.dumps(data_list))
#
# url = 'https://api.github.com/users/piskunovma'
#
# response = requests.get(url)
# user_data = response.json().get('login')
#
# with open(f'{user_data}.json', 'w') as file:
#     file.write(response.text)

import os
import shutil

path_file = os.getcwd()

files = [itm for itm in os.listdir(path_file) if os.path.isfile(os.path.join(path_file, itm))]

# os.rename(os.path.join(path_file, 'data.json'), 'new_data.json')

# os.system(('ls -la'))

shutil.copy(os.path.join(path_file, 'new_data.json'), os.path.join(path_file, 'new_data2'))
shutil.make_archive(os.path.join(path_file, 'new_arch'), 'zip', os.path.join(path_file, 'temp'))

print(files)
print(os.system(('dir')))