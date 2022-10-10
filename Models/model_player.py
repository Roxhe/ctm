

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

    def serialize(self, player):
        serialized_player = {
            "last_name": player.last_name,
            "first_name:": player.first_name,
            "birthdate": player.birthdate,
            "gender": player.gender,
            "global_rank": player.global_rank
        }
        return serialized_player

    def deserialize(self, serialized_player):
        last_name = serialized_player['last_name']
        first_name = serialized_player['first_name']
        birthdate = serialized_player['birthdate']
        gender = serialized_player['gender']
        global_rank = serialized_player['global_rank']
        player = Player(last_name=last_name,
                        first_name=first_name,
                        birthdate=birthdate,
                        gender=gender,
                        global_rank=global_rank)
        return player

