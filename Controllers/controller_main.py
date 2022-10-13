from Controllers.controller_menu import MenuController
from Views.menu_view import Menu

menu = Menu()
menu_controller = MenuController()

class ControllerMainMenu():

    def __init__(self):
        self.menu = Menu()
        self.menu_controller = MenuController()

    def mainmenu(self):
        self.menu.display_menu()



test = ControllerMainMenu()
test.mainmenu()