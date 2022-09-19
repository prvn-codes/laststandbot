import challonge as ch
import json
from datetime import datetime

if __name__ == '__main__':
    """driver code to test all get api calls
    """

    # getTournaments
    f = open("./data/tournaments.json","w")
    tournaments = ch.getTournaments()
    f.write(json.dumps(tournaments, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getTournaments\t-> successful")

    # getTournamentIDs
    f = open("./data/tournament_ids.txt","w")
    tournament_ids = ch.getTournamentIDs()    
    f.write(json.dumps(tournament_ids, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getTournamentIDs\t-> successful")
    
    # getTournamentInfo
    f = open("./data/tournament_info_sample.json","w")
    tournament_info = ch.getTournamentInfo(tournament_ids[0])
    f.write(json.dumps(tournament_info, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getTournamentInfo\t-> successful")
    
    # getMatches
    f = open("./data/matches.json","w")
    matches = ch.getMatches(tournament_ids[0])
    f.write(json.dumps(matches, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getMatches\t-> successful")

    # getMatchIDs
    f = open("./data/match_ids.txt","w")
    match_ids = ch.getMatchIDs(tournament_ids[0])
    f.write(json.dumps(match_ids, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getMatchIDs\t-> successful")

    # getMatchInfo
    f = open("./data/match_info_sample.json","w")
    match_info = ch.getMatchInfo(tournament_ids[0],match_ids[0])
    f.write(json.dumps(match_info, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getMatchInfo\t-> successful")

    # getParticipants
    f = open("./data/participants.json","w")
    participants = ch.getParticipants(tournament_ids[0])
    f.write(json.dumps(participants, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getParticipants\t-> successful")

    # getParticipantIDs
    f = open("./data/participant_ids.txt","w")
    participant_ids = ch.getParticipantIDs(tournament_ids[0])
    f.write(json.dumps(participant_ids, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getParticipantIDs\t-> successful")

    # getParticipantInfo
    f = open("./data/participant_info_sample.json","w")
    participant_info = ch.getParticipantInfo(tournament_ids[0],participant_ids[0])
    f.write(json.dumps(participant_info, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getParticipantInfo\t-> successful")

    # getAttachments
    f = open("./data/attachments_match1.json","w")
    attachments = ch.getAttachments(tournament_ids[0], match_ids[0])
    f.write(json.dumps(attachments, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getAttachments\t-> successful")

    # getAttachmentIDs
    f = open("./data/attachment_match1_ids.txt","w")
    attachment_ids = ch.getAttachmentIDs(tournament_ids[0],match_ids[0])
    f.write(json.dumps(attachment_ids, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getAttachmentIDs\t-> successful")

    # getAttachmentInfo
    f = open("./data/attachment_match1_info_sample.json","w")
    if attachments:
        attachment = ch.getAttachmentInfo(tournament_ids[0], match_ids[0],attachments[0])
        f.write(json.dumps(attachment, indent=4))
    f.close()
    print(f"[{datetime.now()}] : getAttachmentInfo\t-> successful")

    # --------------------------------setters-----------------------
    f = open("./data/update_match.json", "r")
    response_code = ch.updateMatchInfo(tournament_ids[0], match_ids[0], json.load(f))
    print(f"[{datetime.now()}] {response_code} : updateMatchInfo\t-> successful")
    f.close()