import requests
import pandas as pd

base_url = 'https://rickandmortyapi.com/api/'
endpoint = 'character'


def main_request(base_url, endpoint, page=1):
    response = requests.get(base_url + endpoint + f"?page={page}")
    return response.json()

def get_pages(response):
    return response.get('info').get('pages')

def parse_json(response):
    char_list = []

    for item in response.get('results'):
        character = {
        'id': item.get('id'),
        'name': item.get('name'),
        'episodes': len(item.get('episode')),
        }
        char_list.append(character)
    return char_list

main_list = []
data = main_request(base_url, endpoint)
for page in range(1, get_pages(data)+ 1):
    print(page)
    main_list.extend(parse_json(main_request(base_url, endpoint, page)))

data_frame = pd.DataFrame(main_list)
data_frame.to_csv('character.csv', index=False)
