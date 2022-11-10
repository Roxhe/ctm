from Models.model_rapport import Rapport
from Models.model_player import Player
from Models.model_tournament import Tournament

class RapportController:

    def __init__(self):
        self.model_rapport = Rapport()
        self.player = 0
        self.tournament = 0

    def stock_player(self, lst):
        self.player = Player(lst[0], lst[1], lst[2], lst[3], lst[4])
        self.model_rapport.list_stock_players.append(self.player)
        return self.player

    def return_player_list(self):
        for self.player in self.model_rapport.list_stock_players:
            print(self.player.__str__())

    def stock_tournament(self, lst_t, players):
        self.tournament = Tournament(lst_t[0], lst_t[1], lst_t[2], players)
        self.model_rapport.list_stock_tournament.append(self.tournament)
        return self.tournament

    def return_tournament_list(self):
        for self.tournament in self.model_rapport.list_stock_tournament:
            print(self.tournament.__str__())

