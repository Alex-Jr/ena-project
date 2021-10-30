import requests
import json
import csv
import time
import random

## read players ids from './players-ids.txt
players_ids = []
with open('players-ids.txt', 'r') as file:
    players_ids = file.readlines()

names = []
medals = []
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

    medal_count = -1
    name = 'error'
    if(response.status_code == 200):   
        parsed_response = json.loads(response.content)
        medal_count = parsed_response['achievements'][6]['count']
        name = parsed_response['citizen']["name"]

    names.append(name)
    medals.append(medal_count)
    time.sleep(10 + random.random() * 5)

# offline tests
# content = []
# with open('mockup.txt', 'r') as file:
#     content = file.readlines()
# parsed_response = json.loads(content[0])
# medals.append(parsed_response['achievements'][6]['count'])
# names.append(parsed_response['citizen']["name"])

with open('generate-sky-hero-output.csv', 'w') as file:
    headers= ['name', 'sky_hero_medals']
    writer = csv.DictWriter(file, fieldnames=headers)

    i = 0
    for name in names:
        writer.writerow({'name': name, 'sky_hero_medals': medals[i]})
        i = i + 1

