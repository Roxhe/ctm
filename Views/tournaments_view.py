from Models.model_rapport import Rapport
from Controllers.controller_rapport import RapportController

class DisplayTournament:

    def __init__(self):
        self.tournament_rapport = Rapport()
        self.rapport_controller = RapportController()
        self.lst_input_tournament = []

    def prompt_tournament(self):
        t_name = input("Entrez le nom du Tournoi :\n")
        t_place = input("Entrez l'endroit où se déroule le Tournoi :\n")
        t_date = input("Entrez la date du tournoi (DD/MM/AAAA) : \n")

        self.lst_input_tournament = [t_name, t_place, t_date]

        return self.lst_input_tournament, self.tournament_rapport

    def return_all_tournament(self):
        self.rapport_controller.return_tournament_list()

    def reminds_id(self, tournament):
        o = input("Pour un rappel des numéros de joueur tapé : y\n"
                      "Pour continuer, appuyer sur Entrée\n")
        if o == 'y':
            for player in tournament.players:
                print(f"{player.last_name} {player.first_name} porte le numéro {player.id}.")

    def display_final_result(self, tournament):
        for n, m in zip(list(range(1, 8+1)), tournament.final_result):
            for player in tournament.players:
                if m[0] == player.id:
                    p = f"{player.last_name} {player.first_name}"
            print(f"{n}. Nom : {p}\n ID : {m[0]}\n Score: {m[1]}")

    def display_round_bounds(self, i):
        print(f"\nDebut Tour {i + 2}")

    def display_round1_bounds(self):
        print("\nDebut Tour 1")
