import requests
import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

api_url_base = "https://"+os.environ.get("CHALLONGE_USERNAME")+":"+os.environ.get("CHALLONGE_API_KEY")+"@api.challonge.com/v1/"
headers={'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'}

valid_responses = {
    200:"OK",
    401:"Unauthorized (Invalid API key or insufficient permissions)",
    404:"Page does not exist or Object not found within your challonge account scope",
    406:"Requested format is not supported :request JSON or XML only",
    422:"Validation error(s) for create or update method",
    500:"Something went wrong on Challonge end."
    }

def checkResponseCode(response_code : int):
    """checks for valid response code and raises execptions

    Args:
        response_code (int): response code

    """
    if response_code != 200:
        raise Exception(f"[{response_code}]-> {valid_responses[response_code]}")
    


# ----------------------------- Tournament -----------------------------------------

def getTournaments() -> dict:
    """a function to get information of all tournaments

    * Returns:
        dict: a dictionary of information about all tournaments
    """

    response = requests.get(api_url_base+"tournaments.json", headers=headers)
    checkResponseCode(response.status_code)
    return response.json()

def getTournamentIDs() -> list:
    """a function which returns all tournament ids

    * Returns:
        list: a list of all tournament ids
    """
    tourns = getTournaments()
    tourns_id =[]
    for tourn in tourns:
        tourns_id.append(tourn['tournament']['id'])
    return tourns_id

def getTournamentInfo(tournament_id : int) -> dict:
    """a function which returns information about a tournament

    Args:
        tournament_id (int): tournament id

    Returns:
        dict: a dictionary containing information about tournament
    """
    response = requests.get(api_url_base+f"tournaments/{tournament_id}.json", headers=headers)
    checkResponseCode(response.status_code)
    return response.json()

# ----------------------------- Match -----------------------------------------

def getMatches(tournament_id : int) -> dict:
    """a function which returns information of all matches

    * Args:
        tournament_id (int): tournament

    * Returns:
        dict: a dictionary containing information about all matches
    """
    response = requests.get(api_url_base+f"tournaments/{tournament_id}/matches.json", headers=headers)
    checkResponseCode(response.status_code)
    return response.json()

def getMatchIDs(tournament_id : int) -> list:
    """a function which returns match id of all matches

    * Args:
        tournament_id (int): tournament id

    * Returns:
        list: a list of all match ids
    """
    matches = getMatches(tournament_id)
    matchIDs = []
    for match in matches:
        matchIDs.append(match['match']['id'])  
    return matchIDs

def getMatchInfo(tournament_id : int, match_id : int) -> dict:
    """a function which returns information about a match

    * Args:
        tournament_id (int): tournament id
        match_id (int): match id

    * Returns:
        dict: a dictionary containing information about match
    """
    response = requests.get(api_url_base+f"tournaments/{tournament_id}/matches/{match_id}.json", headers=headers)
    checkResponseCode(response.status_code)
    return response.json()

#  ----------------------------- Participant -----------------------------------------
def getParticipants(tournament_id : int) -> dict:
    """a function which returns information of all participants from a tournamentq

    * Args:
        tournament_id (int): tournament id

    * Returns:
        dict: a dictionary containing information of all participants
    """
    response = requests.get(api_url_base+f"tournaments/{tournament_id}/participants.json", headers=headers)
    checkResponseCode(response.status_code)
    return response.json()   

def getParticipantIDs(tournament_id : int) -> list:
    """a function which returns all participants id from a tournament

    * Args:
        tournament_id (int): tournament id

    * Returns:
        list: a list of all participants from a tournament
    """
    participants = getParticipants(tournament_id)
    participants_ids = []
    for participant in participants:
        participants_ids.append(participant['participant']['id'])  
    return participants_ids

def getParticipantInfo(tournament_id : int,participant_id : int) -> dict:
    """ a function which returns information about participant 

    * Args:
        tournament_id (int): tournament id
        participant_id (int): participant's id

    * Returns:
        dict: a dictionary containing information about participant 
    """
    response = requests.get(api_url_base+f"tournaments/{tournament_id}/participants/{participant_id}.json", headers=headers)
    checkResponseCode(response.status_code)
    return response.json()

#  ----------------------------- attachments -----------------------------------------

def getAttachments(tournament_id : int, match_id : int) -> dict:
    """a function which returns information of all attachments of a match

    Args:
        tournament_id (int): tournament id
        match_id (int): match id

    Returns:
        dict: a dictionary containing information of all attachments of a match
    """

    response = requests.get(api_url_base+f"tournaments/{tournament_id}/matches/{match_id}/attachments.json", headers=headers)
    checkResponseCode(response.status_code)
    return response.json()

def getAttachmentIDs(tournament_id : int, match_id : int) -> dict:
    """a function which returns list of all attachments of a match

    Args:
        tournament_id (int): tournament id
        match_id (int): match id

    Returns:
        dict: a list of all attachment ids of a match
    """
    attachments = getAttachments(tournament_id, match_id)
    attachment_IDs = []
    for attachment in attachments:
        attachment_IDs.append(attachment['attachment']['id'])
    return attachment_IDs

def getAttachmentInfo(tournament_id : int,match_id : int,attachment_id : int) -> dict:
    """a function which returns information of a attachment

    Args:
        tournament_id (int): tournament id
        match_id (int): match id
        attachment_id (int): attachment id

    Returns:
        dict: a dictionary containing information about attachment
    """
    response = requests.get(api_url_base+f"tournaments/{tournament_id}/matches/{match_id}/attachments/{attachment_id}.json", headers=headers)
    checkResponseCode(response.status_code)
    return response.json()      


if __name__ == '__main__':
    """driver code to test all get api calls
    """

    # getTournaments
    f = open("./data/tournaments.json","w")
    tournaments = getTournaments()
    f.write(json.dumps(tournaments, indent=4))
    f.close()
    print("[getTournaments]\t-> successful")

    # getTournamentIDs
    f = open("./data/tournament_ids.txt","w")
    tournament_ids = getTournamentIDs()    
    f.write(json.dumps(tournament_ids, indent=4))
    f.close()
    print("[getTournamentIDs]\t-> successful")
    
    # getTournamentInfo
    f = open("./data/tournament_info_sample.json","w")
    tournament_info = getTournamentInfo(tournament_ids[0])
    f.write(json.dumps(tournament_info, indent=4))
    f.close()
    print("[getTournamentInfo]\t-> successful")
    
    # getMatches
    f = open("./data/matches.json","w")
    matches = getMatches(tournament_ids[0])
    f.write(json.dumps(matches, indent=4))
    f.close()
    print("[getMatches]\t-> successful")

    # getMatchIDs
    f = open("./data/match_ids.txt","w")
    match_ids = getMatchIDs(tournament_ids[0])
    f.write(json.dumps(match_ids, indent=4))
    f.close()
    print("[getMatchIDs]\t-> successful")

    # getMatchInfo
    f = open("./data/match_info_sample.json","w")
    match_info = getMatchInfo(tournament_ids[0],match_ids[0])
    f.write(json.dumps(match_info, indent=4))
    f.close()
    print("[getMatchInfo]\t-> successful")

    # getParticipants
    f = open("./data/participants.json","w")
    participants = getParticipants(tournament_ids[0])
    f.write(json.dumps(participants, indent=4))
    f.close()
    print("[getParticipants]\t-> successful")

    # getParticipantIDs
    f = open("./data/participant_ids.txt","w")
    participant_ids = getParticipantIDs(tournament_ids[0])
    f.write(json.dumps(participant_ids, indent=4))
    f.close()
    print("[getParticipantIDs]\t-> successful")

    # getParticipantInfo
    f = open("./data/participant_info_sample.json","w")
    participant_info = getParticipantInfo(tournament_ids[0],participant_ids[0])
    f.write(json.dumps(participant_info, indent=4))
    f.close()
    print("[getParticipantInfo]\t-> successful")

    # getAttachments
    f = open("./data/attachments_match1.json","w")
    attachments = getAttachments(tournament_ids[0], match_ids[0])
    f.write(json.dumps(attachments, indent=4))
    f.close()
    print("[getAttachments]\t-> successful")

    # getAttachmentIDs
    f = open("./data/attachment_match1_ids.txt","w")
    attachment_ids = getAttachmentIDs(tournament_ids[0],match_ids[0])
    f.write(json.dumps(attachment_ids, indent=4))
    f.close()
    print("[getAttachmentIDs]\t-> successful")

    # getAttachmentInfo
    f = open("./data/attachment_match1_info_sample.json","w")
    if len(attachments) != 0:
        attachment = getAttachmentInfo(tournament_ids[0], match_ids[0],attachments[0])
        f.write(json.dumps(attachment, indent=4))
    f.close()
    print("[getAttachmentInfo]\t-> successful")