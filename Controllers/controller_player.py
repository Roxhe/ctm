from Views.menu_view import Menu
from Views.players_view import DisplayPlayer



class PlayerController:

    def __init__(self):
        self.view_player = DisplayPlayer()
        self.menu = Menu()

    def nav_submenu_player(self):
        # match case
        while True:
            choice = self.menu.display_menu()
            if choice == 1:
                self.view_player.prompt_players()
            elif choice == 2:
                self.view_player.return_all_players()
            elif choice == 3:
                exit()
