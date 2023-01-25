
class Tournament:
    """Initialisation d'un Tournoi"""
    def __init__(self, name, place, date, players=[], nb_of_rounds=4, rem_id=[],
                 players_fmatch=[], played_match_result=[], final_result=[], round_time=[]):
        self.name = name
        self.place = place
        self.date = date
        self.players = players
        self.nb_of_rounds = nb_of_rounds
        self.dict_fsort = {}
        self.rem_id = rem_id
        self.players_fmatch = players_fmatch
        self.final_result = final_result
        self.played_match_result = played_match_result
        self.round_time = round_time

    def serialize(self):
        serialized_tournament = dict()
        serialized_tournament['Name'] = self.name
        serialized_tournament['Place'] = self.place
        serialized_tournament['Date'] = self.date

        serialized_players = []
        for player in self.players:
            serialized_player = dict()
            serialized_player['LastName'] = player.last_name
            serialized_player['FirstName'] = player.first_name
            serialized_player['Birthdate'] = player.birthdate
            serialized_player['Gender'] = player.gender
            serialized_player['GlobalRank'] = player.global_rank

            serialized_players.append(serialized_player)

        serialized_tournament['Players'] = serialized_players
        serialized_tournament['Nb_of_rounds'] = self.nb_of_rounds
        serialized_tournament['Rem_id'] = self.rem_id
        serialized_tournament['Final_result'] = self.final_result
        serialized_tournament['Played_match_result'] = self.played_match_result
        serialized_tournament['Round_time'] = self.round_time
        return serialized_tournament

    def __str__(self):
        tournament_presentation = f'Tournoi "{self.name}", se déroule à "{self.place}", le "{self.date}".'
        return tournament_presentation
