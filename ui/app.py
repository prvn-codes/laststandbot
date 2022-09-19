import json
from flask import Flask, render_template
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import sys
sys.path.insert(0,"./")
import api.challonge as ch

app = Flask("__name__", template_folder="./ui/template", static_folder="./ui/static")

os.environ["TOURNAMENT_ID"] = str(ch.getTournamentIDs()[0])

participants_json = ch.getParticipants(os.environ["TOURNAMENT_ID"])
participants = {}
for participant in participants_json:
    participants[participant["participant"]["id"]] = participant["participant"]["name"] 

@app.route("/")
def home():
    matches = ch.getMatches(os.environ["TOURNAMENT_ID"])
    data = []
    for match in matches:
        if match["match"]["player1_id"]:
            temp = {}
            temp["id"] = match["match"]["id"]
            temp["team_a"] = participants[match["match"]["player1_id"]]
            temp["team_b"] = participants[match["match"]["player2_id"]]
            temp["state"] = match["match"]["state"]
            data.append(temp)

    return render_template("displayMatches.html", matches = data)
@app.route("/match/<match_id>")
def updateMatch(match_id):
    return json.loads(f"./data/match/{match_id}.json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088, debug=True)
