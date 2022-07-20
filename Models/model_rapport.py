
class Rapport():
    def __init__(self, list_players):
        self.list_players = list_players

    def display_players(self, list_players):
        #ajouter une manière de trier plus tard
        for player in list_players:
            print(player)