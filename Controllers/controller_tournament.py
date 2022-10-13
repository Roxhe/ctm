from Views.menu_view import Menu
from Views.tournaments_view import DisplayTournament


class TournamentController():

    def nav_submenu_tournament(self):
        menu = Menu()
        display_tournament = DisplayTournament()
        print(menu.choice)
        if menu.choice == 1:
            display_tournament.prompt_tournament()
            display_tournament.tournament_in_play()
            menu.sub_tournament()
        elif menu.choice == 2:
            display_tournament.return_all_tournament()
            menu.sub_tournament()
        elif menu.choice == 3:
            menu.display_menu()
