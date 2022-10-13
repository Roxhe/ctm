from Views.menu_view import Menu
from Views.players_view import DisplayPlayer

class Player():

    def nav_submenu_player(self):
        menu = Menu()
        display_player = DisplayPlayer()

        if menu.choice == 1:
           display_player.prompt_players()
           menu.sub_player()
        elif menu.choice == 2:
           display_player.return_all_players()
           menu.sub_player()

        elif menu.choice == 3:
            menu.sub_player()
