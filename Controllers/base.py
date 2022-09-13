from Models.model_tournament import Tournament
from Models.model_player import Player


class Controller:

    def __init__(self, tournament: Tournament, view):
        self.players: Player = []
        self.tournament = tournament
        self.view = view

    def create_players(self):
        while True:
            for ln, fn, bd, gd, gr in self.view.inp_create_player():
                player = Player(ln, fn, bd, gd, gr)
                self.players.append(player)
