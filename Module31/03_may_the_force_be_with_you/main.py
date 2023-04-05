import requests
import json

def get_info(path):
    response = requests.get(path)
    data = json.loads(response.text)

    return data

starship_details = ["name", "starship_class", "max_atmosphering_speed"]
pilots_details = ['height', 'homeworld', 'mass', 'name']
path = "https://swapi.dev/api/starships/10/"
result = {}
pilots = []


data = get_info(path)

for el in starship_details:
    result[el] = data[el]

pilots_info = data['pilots']

for i in range(len(pilots_info)):
    pilot = {}
    pilot_info = get_info(pilots_info[i])

    for el in pilots_details:
        pilot[el] = pilot_info[el]

    homeworld_info = get_info(pilot['homeworld'])
    pilot['homeworld_url'] = pilot['homeworld']
    pilot['homeworld'] = homeworld_info['name']
    pilots.append(pilot)


result['pilots'] = pilots

with open('Millennium Falcon.json', 'w', encoding='utf8') as file:
    json.dump(result, file, indent=4)

print(result)