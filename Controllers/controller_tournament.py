from Views.menu_view import Menu
from Views.tournaments_view import DisplayTournament



class TournamentController:

    def __init__(self):
        self.view_tournament = DisplayTournament()
        self.menu = Menu()

    def nav_submenu_tournament(self):
        while True:
            choice = self.menu.sub_tournament()
            if choice == 1:
                self.view_tournament.prompt_tournament()
                self.view_tournament.tournament_in_play()

            elif choice == 2:
                self.view_tournament.return_all_tournament()
                self.menu.sub_tournament()
            elif choice == 3:
                exit()