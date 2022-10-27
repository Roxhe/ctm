from Views.menu_view import Menu
from Views.players_view import DisplayPlayer



class PlayerController:

    def __init__(self):
        self.view_player = DisplayPlayer()
        self.menu = Menu()

    def nav_submenu_player(self):
        choice = self.menu.sub_player()
        match choice:
            case 1:
                self.view_player.prompt_players()
            case 2:
                self.view_player.return_all_players()
            case 3:
                self.menu.display_menu()
            case _:
                #print("Veuillez rentrer soit 1, soit 2, soit 3. \n")
                self.nav_submenu_player()
