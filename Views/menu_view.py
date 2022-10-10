from rich.console import Console
from rich.markdown import Markdown

from Views.players_view import DisplayPlayer
from Views.tournaments_view import DisplayTournament


console = Console()


class Menu:

    def __init__(self):
        self.choice = 0
        self.display_player = DisplayPlayer()
        self.display_tournament = DisplayTournament()

    def display_menu(self):

        main_menu = """
    # Bienvenue dans Chess Tournament Manager
        
        Veuillez sélectionner le menu désiré.
        
        1. Tournois
        2. Joueurs
        3. Quitter
        """

        main_menu0 = Markdown(main_menu)
        console.print(main_menu0)
        self.nav_menu()

    def sub_tournament(self):
        main_sub_tournament = """
    # Tournois
    
    Veuillez sélectionner le menu désiré.
    
    1. Créer un Tournoi
    2. Liste des anciens Tournois   
    3. Retour au menu principal
    """
        main_sub_tournament0 = Markdown(main_sub_tournament)
        console.print(main_sub_tournament0)

        self.nav_tournament()

    def sub_player(self):
        main_sub_player = """
    # Joueurs
        
            
    Veuillez sélectionner le menu désiré.
    
    1. Créer les Joueurs
    2. Liste des Joueurs existants
    3. Retour au menu principal
        """

        main_sub_player0 = Markdown(main_sub_player)
        console.print(main_sub_player0)
        self.nav_player()

    def nav_menu(self):
        self.choice = int(input())
        if self.choice == 1:
            self.sub_tournament()
        elif self.choice == 3:
            exit()
        elif self.choice == 2:
            self.sub_player()
        elif self.choice == 0:
            self.choice = int(input("Veuillez rentrez soir, 1, soit 2, soit 3. \n"))

    def nav_tournament(self):
        self.choice = int(input())
        if self.choice == 1:
            self.display_tournament.prompt_tournament()
            self.display_tournament.tournament_in_play()
            self.sub_tournament()
        elif self.choice == 3:
            self.display_menu()
        elif self.choice == 2:
            self.display_tournament.return_all_tournament()
            self.sub_tournament()
        elif self.choice == 0:
            self.choice = int(input("Veuillez rentrez soir, 1, soit 2, soit 3. \n"))

    def nav_player(self):

        self.choice = int(input())
        if self.choice == 1:
            self.display_player.prompt_players()
            self.sub_player()
        elif self.choice == 3:
            self.display_menu()
        elif self.choice == 2:
            self.display_player.return_all_players()
            self.sub_player()
        elif self.choice == 0:
            self.choice = int(input("Veuillez rentrez soir, 1, soit 2, soit 3. \n"))


menu_t = Menu()
menu_t.display_menu()