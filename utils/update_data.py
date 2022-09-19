import sys
import json
from datetime import datetime
sys.path.insert(0,"./")
import api.challonge as ch

if __name__ == "__main__":
    f = open("./data/tournament/tournaments.json","w")
    tournaments = ch.getTournaments()
    f.write(json.dumps(tournaments, indent=4))
    f.close()
    print(f"[{datetime.now()}] : fetchTournaments\t-> successful")

    matches = ch.getMatches(tournaments[0]["tournament"]["id"])
    for match in matches:
        f = open(f'./data/match/{match["match"]["id"]}.json',"w")
        f.write(json.dumps(match, indent=4))
        f.close()
    print(f"[{datetime.now()}] : fetchMatches\t-> successful")

    participants = ch.getParticipants(tournaments[0]["tournament"]["id"])
    for participant in participants:
        f = open(f'./data/participant/{participant["participant"]["id"]}.json',"w")
        f.write(json.dumps(participant, indent=4))
        f.close()
    print(f"[{datetime.now()}] : fetchparticipants\t-> successful")