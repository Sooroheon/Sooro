import json
with open('dictlist.json', 'r') as file:
    json_reader = file.read()
    dict_list = json.load(json_reader)

for dic in dict_list:
    print('이름: {}'.format(dic['name']))
    print('나이: {}'.format(dic['age']))
    print('키: {}'.format(dic['spec']))
    print('몸무게: {}'.format(dic['spec']))
    print()