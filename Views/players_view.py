from Models.model_player import Player


class DisplayPlayer:

    def __init__(self):
        self.lst_player_new_tournament = []

    def prompt_player(self, players_rapport):
        last_name = input("Entrez le nom du joueur :\n")
        first_name = input("Entrez le prénom du joueur :\n")
        birthdate = input("Entrez la date de naissance du joueur (DD/MM/AAAA) :\n")
        gender = input("Entrez le genre du joueur :\n")
        globalrank = int(input("Entrez le classement global du joueur :\n"))

        lst_input_player = [last_name, first_name, birthdate, gender, globalrank]
        stocked_player = players_rapport.stock_player(lst_input_player)
        print(f"Le joueur suivant a été ajouté :"
              f"{stocked_player.__str__()}\n")
        player = Player(lst_input_player[0], lst_input_player[1],
                        lst_input_player[2], lst_input_player[3],
                        lst_input_player[4])
        return player

    def prompt_suppr_player(self, players_rapport):
        players_rapport.return_player_list()
        player_to_suppr = int(input("Entrez le numéro du joueur à supprimer :  "))
        players_rapport.suppr_player(player_to_suppr)

    def prompt_suppr_players(self, players_rapport):
        while True:
            self.prompt_suppr_player(players_rapport)
            end_or_not = input("Souhaitez vous supprimer un autre joueur ? yes : y / no : n\n")
            if end_or_not == 'y':
                continue
            elif end_or_not == 'n':
                players_rapport.return_player_list()
                break

    def prompt_modif_player_rank(self, players_rapport):
        players_rapport.return_player_list()
        players_to_modif = int(input("Entrez le numéro du joueur auquel modifier le classement :\n"))
        print(players_rapport.list_stock_players[players_to_modif - 1].__str__())
        new_rank = int(input("Entrez le nouveau classement du joueur :\n"))
        players_rapport.modif_player_rank(players_to_modif, new_rank)

    def prompt_modif_players_ranks(self, players_rapport):
        while True:
            self.prompt_modif_player_rank(players_rapport)
            end_or_not = input("Souhaitez vous supprimer un autre joueur ? yes : y / no : n\n")
            if end_or_not == 'y':
                continue
            elif end_or_not == 'n':
                break

    def prompt_players(self, players_rapport):
        while True:
            self.prompt_player(players_rapport)
            end_or_not = input("Souhaitez vous recréer un joueur ? yes : y / no : n\n")
            if end_or_not == 'y':
                continue
            elif end_or_not == 'n':
                players_rapport.return_player_list()
                break

    def prompt_players_new_tournament(self, players_rapport):
        for i in range(8):
            self.lst_player_new_tournament.append(self.prompt_player(players_rapport))
        return self.lst_player_new_tournament
