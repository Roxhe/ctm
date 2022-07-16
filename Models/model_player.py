

class Player:
    """Initialisation des joueurs """
    def __init__(self, last_name, first_name, birthdate, gender, global_rank=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.global_rank = global_rank
        self.score = 0.0

    def __str__(self):
        player_presentation = f'Prénom : {self.first_name}, Nom : {self.last_name}, ' \
                              f'Rang : {self.global_rank}, Score : {self.score}'
        return player_presentation

        cd de