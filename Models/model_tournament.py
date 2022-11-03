
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

    def __str__(self):
        tournament_presentation = f'Ce tournoi "{self.name}", se déroule à "{self.place}", le "{self.date}".'
        return tournament_presentation
