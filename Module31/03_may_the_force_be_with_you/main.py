import requests
import json
from typing import Dict, List


def get_info(path: str) -> Dict:
    response: requests = requests.get(path)
    data: json = json.loads(response.text)

    return data


starship_details: List[str] = ["name", "starship_class", "max_atmosphering_speed"]
pilots_details: List[str] = ['height', 'homeworld', 'mass', 'name']
path: str = "https://swapi.dev/api/starships/10/"
result: Dict = {}
pilots:  List = []

data: json = get_info(path)

for el in starship_details:
    result[el] = data[el]

pilots_info: Dict = data['pilots']

for i in range(len(pilots_info)):
    pilot: Dict = {}
    pilot_info: json = get_info(pilots_info[i])

    for el in pilots_details:
        pilot[el] = pilot_info[el]

    homeworld_info: json = get_info(pilot['homeworld'])
    pilot['homeworld_url'] = pilot['homeworld']
    pilot['homeworld'] = homeworld_info['name']
    pilots.append(pilot)

result['pilots'] = pilots

with open('Millennium Falcon.json', 'w', encoding='utf8') as file:
    json.dump(result, file, indent=4)

print(result)
