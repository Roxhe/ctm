from Controllers.controller_tournament import TournamentController
from Views.menu_view import Menu
from Views.tournaments_view import DisplayTournament
from Views.players_view import DisplayPlayer
from Models.model_rapport import Rapport


class NavController:

    def __init__(self):
        self.tournament_controller = TournamentController()
        self.menu = Menu()
        self.view_tournament = DisplayTournament()
        self.view_player = DisplayPlayer()
        self.rapport = Rapport()
        self.rapport.deserialize_player()
        self.rapport.deserialize_tournament()

    def nav_main(self):

        choice = self.menu.display_menu()
        match choice:
            case 1:
                self.nav_submenu_tournament()
            case 2:
                self.nav_submenu_player()
            case 3:
                self.rapport.serialize_player()
                self.rapport.serialize_tournament()
                exit()
            case _:
                self.menu.menu_error()
                self.nav_main()

    def nav_submenu_tournament(self):

        choice = self.menu.sub_tournament()
        match choice:
            case 1:
                self.tournament_controller.create_tournament(self.rapport)
                self.tournament_controller.tournament_in_play()
                self.nav_submenu_tournament()
            case 2:
                self.tournament_controller.create_tournament_new_players(self.rapport)
                self.tournament_controller.tournament_in_play()
                self.nav_submenu_tournament()
            case 3:
                self.rapport.return_tournament_list()
                self.rapport.return_tournament_played_match()
                self.nav_submenu_tournament()
            case 4:
                self.nav_main()
            case _:
                self.menu.menu_error()
                self.nav_submenu_tournament()

    def nav_submenu_player(self):
        choice = self.menu.sub_player()
        match choice:
            case 1:
                self.view_player.prompt_players(self.rapport)
                self.nav_submenu_player()
            case 2:
                self.rapport.return_player_list()
                self.nav_submenu_player()
            case 3:
                self.view_player.prompt_modif_players_ranks(self.rapport)
                self.nav_submenu_player()
            case 4:
                self.view_player.prompt_suppr_players(self.rapport)
                self.nav_submenu_player()
            case 5:
                self.nav_main()
            case _:
                self.menu.menu_error()
                self.nav_submenu_player()
