
class Tournament:
    """Initialisation d'un Tournoi"""
    def __init__(self, name, place, date,  players=[], nb_of_rounds=4):
        self.name = name
        self.place = place
        self.date = date
        self.players = players
        self.nb_of_rounds = nb_of_rounds
        self.dict_fsort = {}
        self.rem_id = []
        self.players_fmatch = []
        self.final_result = []
        self.played_match_result = []

    def serialize(self):
        serialized_tournament = dict()
        serialized_tournament['Name'] = self.name
        serialized_tournament['Place'] = self.place
        serialized_tournament['Date'] = self.date
        serialized_tournament['Players'] = self.players
        serialized_tournament['Nb_of_rounds'] = self.nb_of_rounds
        serialized_tournament['Dict_fsort'] = self.dict_fsort
        serialized_tournament['Rem_id'] = self.rem_id
        serialized_tournament['Final_result'] = self.final_result
        serialized_tournament['Played_match_result'] = self.played_match_result
        return serialized_tournament

    def deserialize(self):
        deserialized_tournament = (self.name, self.place, self.date, self.players, self.nb_of_rounds, self.dict_fsort,
                                    self.rem_id, self.final_result, self.played_match_result)
        return deserialized_tournament

    def __str__(self):
        tournament_presentation = f'Tournoi "{self.name}", se déroule à "{self.place}", le "{self.date}".'
        return tournament_presentation
