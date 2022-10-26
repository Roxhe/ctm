from Views.menu_view import Menu
from Controllers.controller_tournament import TournamentController
from Controllers.controller_player import PlayerController

class MenuController:

    def __init__(self):
        self.menu = Menu()
        self.tournament_cont = TournamentController()
        self.player_cont = PlayerController()


    def nav_menu_cont(self):
        # match case
        while True:
            choice = self.menu.display_menu()
            print(choice)
            if choice == 1:
                self.tournament_cont.nav_submenu_tournament()
            elif choice == 2:
                self.player_cont.nav_submenu_player()
            elif choice == 3:
                exit()