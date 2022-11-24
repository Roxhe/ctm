

class Player:
    """Initialisation des joueurs"""
    def __init__(self, last_name, first_name, birthdate, gender, global_rank=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.global_rank = global_rank
        self.score = 0.0
        self.id = 0

    def __str__(self):
        player_presentation = f'Nom : {self.last_name}, Prénom : {self.first_name}, Rang : {self.global_rank}'
        return player_presentation

