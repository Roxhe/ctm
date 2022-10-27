from Views.menu_view import Menu
from Views.tournaments_view import DisplayTournament
from Models.model_tournament import Tournament
from Models.model_rapport import Rapport


class TournamentController:

    def __init__(self):
        self.view_tournament = DisplayTournament()
        self.menu = Menu()
        self.tournament = 0
        self.tournament_rapport = Rapport()

    def nav_submenu_tournament(self):

        choice = self.menu.sub_tournament()
        match choice:
            case 1:
                self.view_tournament.prompt_tournament()
                print(self.view_tournament.tournament_rapport.__init__())
                #self.tournament_in_play()
            case 2:
                self.view_tournament.return_all_tournament()
                self.menu.sub_tournament()
            case 3:
                self.menu.display_menu()
            case _:
                #print("Veuillez rentrer soit 1, soit 2, soit 3. \n")
                self.nav_submenu_tournament()

        return self.tournament

    def sort_player(self):

        for player in self.tournament.players:
            self.tournament.dict_fsort[player] = player.global_rank

        self.tournament.dict_fsort = dict(sorted(self.tournament.dict_fsort.items(), key=lambda x: x[1], reverse=True))
        self.tournament.players = list(self.tournament.dict_fsort)

        for player in self.tournament.players:
            player.id = self.tournament.players.index(player) + 1
            self.tournament.rem_id.append(f"{player.last_name} {player.first_name} portera le numéro {player.id}.")
            self.tournament.players_fmatch.append(player.id)

        return self.tournament

    def tournament_in_play(self):
        self.tournament = self.tournament_rapport.stock_tournament(self.view_tournament.lst_input_tournament)
        TournamentController.sort_player(self.tournament)
        self.tournament.exec_round()
