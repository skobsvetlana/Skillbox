import json
from typing import List, Any

def find_key(data: dict, key_to_find: str) -> Any:
    res = None

    for key, value in data.items():
        if key == key_to_find:
            return value

        if isinstance(value, dict):
            res = find_key(value, key_to_find)
            if res:
                break
    return res


diff_list = ['services', 'staff', 'datetime']
result: dict = dict()

with open('json_old.json', 'r', encoding='utf-8') as file:
    json_old = json.load(file)

with open('json_new.json', 'r', encoding='utf-8') as file:
    json_new = json.load(file)


for el in diff_list:
    old_value = find_key(data=json_old, key_to_find=el)
    new_value = find_key(data=json_new, key_to_find=el)
    if old_value != new_value:
        result[el] = new_value

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4)

print(result)



