#from Models.model_tournament import Tournament
from Models.model_player import Player
from Views.base import View


class Controller:

    def __init__(self, view):
        self.players: Player = []
        #self.tournament = tournament
        self.view = view

    def create_players(self):
        while True:
            ac = self.view.inp_create_player()
            ln = ac[0]
            fn = ac[1]
            bd = ac[2]
            gd = ac[3]
            gr = ac[4]

            player = Player(ln, fn, bd, gd, gr)
            self.players.append(player)
            print(f"Le joueur suivant a été ajouté :"
                  f"{player.__str__()}\n")
            end_or_not = input("Souhaitez-vous créer un autre joueur ? (y/n)")
            if end_or_not == 'y':
                continue
            elif end_or_not == 'n':
                for player in self.players:
                    print(player.__str__())
                break

testv = View()
test1 = Controller(testv)
test1.create_players()
