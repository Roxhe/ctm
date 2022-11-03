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
                self.nav_submenu_player()
            case 2:
                self.view_player.return_all_players()
                self.nav_submenu_player()
            case 3:
                self.menu.display_menu()
            case _:
                self.menu.menu_error()
                self.nav_submenu_player()
