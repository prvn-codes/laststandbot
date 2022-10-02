import requests


class Driver:

    def __init__(self, username, api_key) -> None:
        self.username = username
        self.api_key = api_key
        self.api_url_base = "https://"+self.username + \
            ":"+self.api_key+"@api.challonge.com/v1/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'}
        self.valid_responses = {
            200: "OK",
            401: "Unauthorized (Invalid API key or insufficient permissions)",
            404: "Page does not exist or Object not found within your challonge account scope",
            406: "Requested format is not supported :request JSON or XML only",
            422: "Validation error(s) for create or update method",
            500: "Something went wrong on Challonge end."
        }

        self.cache_data = {
            "tournament": {},
            "matches": [],
            "participants" : [],
        }

    def checkResponseCode(self: "Driver", response_code: int):
        """checks for valid response code and raises execptionss
        Args:
            response_code (int): response code
        """
        if response_code != 200:
            raise Exception(
                f"[{response_code}]-> {self.valid_responses[response_code]}")

    # ----------------------------- Tournament -----------------------------------------

    def getTournaments(self: "Driver") -> dict:
        """a function to get information of all tournaments
        * Returns:
            dict: a dictionary of information about all tournaments
        """
        response = requests.get(
            self.api_url_base+"tournaments.json", headers=self.headers)
        self.checkResponseCode(response.status_code)
        return response.json()

    def getTournamentIDs(self: "Driver") -> list:
        """a function which returns all tournament ids
        * Returns:
            list: a list of all tournament ids
        """
        tourns = self.getTournaments()
        tourns_id = []
        for tourn in tourns:
            tourns_id.append(tourn['tournament']['id'])
        return tourns_id

    def getTournamentInfo(self: "Driver", tournament_id: int) -> dict:
        """a function which returns information about a tournament
        Args:
            tournament_id (int): tournament id
        Returns:
            dict: a dictionary containing information about tournament
        """
        response = requests.get(
            self.api_url_base+f"tournaments/{tournament_id}.json", headers=self.headers)
        self.checkResponseCode(response.status_code)
        return response.json()

    # ----------------------------- Match -----------------------------------------

    def getMatches(self: "Driver", tournament_id: int) -> dict:
        """a function which returns information of all matches
        * Args:
            tournament_id (int): tournament
        * Returns:
            dict: a dictionary containing information about all matches
        """
        response = requests.get(
            self.api_url_base+f"tournaments/{tournament_id}/matches.json", headers=self.headers)
        self.checkResponseCode(response.status_code)
        return response.json()

    def getMatchIDs(self: "Driver", tournament_id: int) -> list:
        """a function which returns match id of all matches
        * Args:
            tournament_id (int): tournament id
        * Returns:
            list: a list of all match ids
        """
        matches = self.getMatches(tournament_id)
        matchIDs = []
        for match in matches:
            matchIDs.append(match['match']['id'])
        return matchIDs

    def getMatchInfo(self: "Driver", tournament_id: int, match_id: int) -> dict:
        """a function which returns information about a match
        * Args:
            tournament_id (int): tournament id
            match_id (int): match id
        * Returns:
            dict: a dictionary containing information about match
        """
        response = requests.get(
            self.api_url_base+f"tournaments/{tournament_id}/matches/{match_id}.json", headers=self.headers)
        self.checkResponseCode(response.status_code)
        return response.json()

    #  ----------------------------- Participant -----------------------------------------

    def getParticipants(self: "Driver", tournament_id: int) -> dict:
        """a function which returns information of all participants from a tournamentq
        * Args:
            tournament_id (int): tournament id
        * Returns:
            dict: a dictionary containing information of all participants
        """
        response = requests.get(
            self.api_url_base+f"tournaments/{tournament_id}/participants.json", headers=self.headers)
        self.checkResponseCode(response.status_code)
        return response.json()

    def getParticipantIDs(self: "Driver", tournament_id: int) -> list:
        """a function which returns all participants id from a tournament

        * Args:
            tournament_id (int): tournament id

        * Returns:
            list: a list of all participants from a tournament
        """
        participants = self.getParticipants(tournament_id)
        participants_ids = []
        for participant in participants:
            participants_ids.append(participant['participant']['id'])
        return participants_ids

    def getParticipantInfo(self: "Driver", tournament_id: int, participant_id: int) -> dict:
        """ a function which returns information about participant 
        * Args:
            tournament_id (int): tournament id
            participant_id (int): participant's id
        * Returns:
            dict: a dictionary containing information about participant 
        """
        response = requests.get(
            self.api_url_base+f"tournaments/{tournament_id}/participants/{participant_id}.json", headers=self.headers)
        self.checkResponseCode(response.status_code)
        return response.json()

    #  ----------------------------- attachments -----------------------------------------
    def getAttachments(self: "Driver", tournament_id: int, match_id: int) -> dict:
        """a function which returns information of all attachments of a match
        Args:
            tournament_id (int): tournament id
            match_id (int): match id
        Returns:
            dict: a dictionary containing information of all attachments of a match
        """

        response = requests.get(
            self.api_url_base+f"tournaments/{tournament_id}/matches/{match_id}/attachments.json", headers=self.headers)
        self.checkResponseCode(response.status_code)
        return response.json()

    def getAttachmentIDs(self: "Driver", tournament_id: int, match_id: int) -> dict:
        """a function which returns list of all attachments of a match
        Args:
            tournament_id (int): tournament id
            match_id (int): match id
        Returns:
            dict: a list of all attachment ids of a match
        """
        attachments = self.getAttachments(tournament_id, match_id)
        attachment_IDs = []
        for attachment in attachments:
            attachment_IDs.append(attachment['attachment']['id'])
        return attachment_IDs

    def getAttachmentInfo(self: "Driver", tournament_id: int, match_id: int, attachment_id: int) -> dict:
        """a function which returns information of a attachment
        Args:
            tournament_id (int): tournament id
            match_id (int): match id
            attachment_id (int): attachment id
        Returns:
            dict: a dictionary containing information about attachment
        """
        response = requests.get(
            self.api_url_base+f"tournaments/{tournament_id}/matches/{match_id}/attachments/{attachment_id}.json", headers=self.headers)
        self.checkResponseCode(response.status_code)
        return response.json()
