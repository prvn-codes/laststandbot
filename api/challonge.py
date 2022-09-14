import requests
import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

api_url_base = "https://"+os.environ.get("CHALLONGE_USERNAME")+":"+os.environ.get("CHALLONGE_API_KEY")+"@api.challonge.com/v1/"
headers={'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'}

def getTournaments():
    response = requests.get(api_url_base+"tournaments.json", headers=headers)
    data = json.loads(response.text)
    return data 

def getMatches(tournament_id):
    response = requests.get(api_url_base+"tournaments.json", headers=headers)
    data = json.loads(response.text)
    return data 

if __name__ == '__main__':
    print(getTournaments()) 

# with open('./data/updated.json', 'r',encoding='utf-8') as f:
#     data= json.load(f)
#     response = requests.put(url=api_url_base+"tournaments/11453176/matches/289068746.json",headers=headers,json=data)
#     print(response.text)

# response = requests.get(api_url_base+"tournaments/"+os.environ.get("TOURNAMENT_ID")+"/participants.json",headers=headers)
# print(response.text)

# with open('./data/tournaments.json', 'w') as f:
#     json.dump(response.json(), f, ensure_ascii=False, indent=4)

# response = requests.get(api_url_base+"tournaments/11453176/matches.json",headers=headers)

# with open('./data/matches.json', 'w') as f:
#     json.dump(response.json(), f, ensure_ascii=False, indent=4)

# print(api_url_base+"tournaments/11453176/matches/289068745")