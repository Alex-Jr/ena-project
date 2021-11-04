import requests
import json
import csv
import time
import random

## read players ids from './players-ids.txt
players_ids = []
with open('players-ids.txt', 'r') as file:
    players_ids = file.readlines()

player_data = []
base_url = 'https://www.erepublik.com/en/main/citizen-profile-json/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Connection': 'close',
    'Cache-Control': 'max-age=0',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
}

for player_id in players_ids:
    url = base_url + player_id.replace('\n', '')
    response = requests.get(url=url, headers=headers)
   
    if(response.status_code == 200):   
        parsed_response = json.loads(response.content)
        player_data.append({
            'id': player_id,
            'name': parsed_response['citizen']["name"],
            'sky_hero_medals': parsed_response['achievements'][6]['count'],
            'air_rank_number': parsed_response['military']['militaryData']['aircraft']['rankNumber'],
            'air_rank_title':  parsed_response['military']['militaryData']['aircraft']['name'],
            'air_rank_points': parsed_response['military']['militaryData']['aircraft']['points'],
        })
    else:
        player_data.append({
            'id': player_id,
            'name': 'error',
            'sky_hero_medals': '0',
            'air_rank_number': '0',
            'air_rank_title': 'error',
            'air_rank_points': '0'
        })
    
    timeout = 20 + random.random() * 10
    print('Fetched id: {} - Sleeping for {:1f} seconds'.format(player_id, timeout))
    time.sleep(timeout)

with open('generate-sky-hero-output.csv', 'w') as file:
    headers= [
        'id',
        'name',
        'sky_hero_medals',
        'air_rank_number',
        'air_rank_title',
        'air_rank_points'
    ]
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()

    for data in player_data:
        writer.writerow(data)
