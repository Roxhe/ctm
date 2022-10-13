from Views.menu_view import Menu

class MenuController:

    def nav_menu_cont(self):
        menu = Menu()

        if menu.choice == 1:
            menu.sub_tournament()
        elif menu.choice == 2:
            menu.sub_player()
        elif menu.choice == 3:
            exit()
