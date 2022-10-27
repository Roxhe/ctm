from Views.menu_view import Menu
from Controllers.controller_tournament import TournamentController
from Controllers.controller_player import PlayerController

class MenuController:

    def __init__(self):
        self.menu = Menu()
        self.tournament_cont = TournamentController()
        self.player_cont = PlayerController()

    def nav_menu_cont(self):
        choice = self.menu.display_menu()
        match choice:
            case 1:
                self.tournament_cont.nav_submenu_tournament()
            case 2:
                self.player_cont.nav_submenu_player()
            case 3:
                exit()
            case _:
                #print("Veuillez rentrer soit 1, soit 2, soit 3. \n")
                self.nav_menu_cont()
