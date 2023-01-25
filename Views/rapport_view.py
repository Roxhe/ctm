
class DisplayRapport:

    def __init__(self):
        pass

    def return_players_list(self, list_stock_players):
        choice = int(input("Taper 1 pour afficher en ordre alphabétique.\nTaper 2 pour afficher par classement.\n"))
        match choice:
            case 1:
                list_stock_players.sort(key=lambda player: player.last_name)
            case 2:
                list_stock_players.sort(key=lambda player: player.global_rank, reverse=True)
        i = 0
        for self.player in list_stock_players:
            i += 1
            print(f"{i}. ", self.player.__str__())

    def return_tournaments_list(self, list_stock_tournament):
        i = 0
        for self.tournament in list_stock_tournament:
            i += 1
            print(f"{i}.", self.tournament.__str__())

    def return_tournament_played_match(self, list_stock_tournaments):
        selec_tournament = int(input("Rentrez le numéro associé au tournoi pour plus de détails : \n"))
        list_stock_tournaments[selec_tournament - 1].players.sort(key=lambda player: player.last_name)
        print("Liste de joueur par ordre alphabétique :")
        i = 0
        for player in list_stock_tournaments[selec_tournament - 1].players:
            i += 1
            print(f"{i}. ", player.__str__())
        print("Numéro des joueurs pendant le tournoi :")
        i = 0
        j = 1
        for id in list_stock_tournaments[selec_tournament - 1].rem_id:
            print(id)
        for match in list_stock_tournaments[selec_tournament - 1].played_match_result:

            if i % 4 == 0:
                print(f"Round {j}")
                if j == 1:
                    print(f"Début : {list_stock_tournaments[selec_tournament - 1].round_time[0]}\n"
                          f"Fin : {list_stock_tournaments[selec_tournament - 1].round_time[1]}")
                elif j == 2:
                    print(f"Début : {list_stock_tournaments[selec_tournament - 1].round_time[2]}\n"
                          f"Fin : {list_stock_tournaments[selec_tournament - 1].round_time[3]}")
                elif j == 3:
                    print(f"Début : {list_stock_tournaments[selec_tournament - 1].round_time[4]}\n"
                          f"Fin : {list_stock_tournaments[selec_tournament - 1].round_time[5]}")
                elif j == 4:
                    print(f"Début : {list_stock_tournaments[selec_tournament - 1].round_time[6]}\n"
                          f"Fin : {list_stock_tournaments[selec_tournament - 1].round_time[7]}")
                j += 1

            if match[2] > 0:
                print(f"Match opposant {match[0]} et {match[1]} avec pour vainqueur {match[2]}")
                i += 1
            else:
                print(f"Match opposant {match[0]} et {match[1]} ayant comme résultat une égalité")
                i += 1

        print("Liste des joueurs par classement dans le tournoi :")
        for n, m in zip(list(range(1, 8 + 1)), list_stock_tournaments[selec_tournament - 1].final_result):
            for player in list_stock_tournaments[selec_tournament - 1].players:
                if m[0] == player.id:
                    p = f"{player.last_name} {player.first_name}"
                    print(f"{n}. Nom : {p}\n ID : {m[0]}\n Score: {m[1]}")
