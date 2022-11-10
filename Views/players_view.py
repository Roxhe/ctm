from Models.model_player import Player
from Models.model_rapport import Rapport

class DisplayPlayer:

    def __init__(self):
        self.players_rapport = Rapport()
        self.lst_player_new_tournament = []

    def prompt_player(self):
        last_name = input("Entrez le nom du joueur :\n")
        first_name = input("Entrez le prénom du joueur :\n")
        birthdate = input("Entrez la date de naissance du joueur (DD/MM/AAAA) :\n")
        gender = input("Entrez le genre du joueur :\n")
        globalrank = int(input("Entrez le classement global du joueur :\n"))

        lst_input_player = [last_name, first_name, birthdate, gender, globalrank]
        stocked_player = self.players_rapport.stock_player(lst_input_player)
        print(f"Le joueur suivant a été ajouté :"
              f"{stocked_player.__str__()}\n")
        player = Player(lst_input_player[0], lst_input_player[1],
                        lst_input_player[2], lst_input_player[3],
                        lst_input_player[4])
        return player

    def prompt_players(self):
        while True:
            self.prompt_player()
            end_or_not = input("Souhaitez vous recréer un joueur ? yes : y / no : n\n")
            if end_or_not == 'y':
                continue
            elif end_or_not == 'n':
                self.players_rapport.return_player_list()
                break

    def prompt_players_new_tournament(self):
        for i in range(8):
            self.lst_player_new_tournament.append(self.prompt_player())
        return self.lst_player_new_tournament

    def return_all_players(self):
        self.players_rapport.return_player_list()
