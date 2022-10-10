from Models.model_rapport import Rapport
from Models.model_tournament import Tournament


class DisplayTournament:

    def __init__(self):
        self.tournament_rapport = Rapport()
        self.lst_input_tournament = []

    def prompt_tournament(self):
        t_name = input("Entrez le nom du Tournoi :\n")
        t_place = input("Entrez l'endroit où se déroule le Tournoi :\n")
        t_date = input("Entrez la date du tournoi (DD/MM/AAAA) : \n")

        self.lst_input_tournament = [t_name, t_place, t_date]

        self.tournament_rapport.stock_tournament(self.lst_input_tournament)

    def return_all_tournament(self):
        self.tournament_rapport.return_tournament_list()

#c
    def tournament_in_play(self):
        tournament_in_play = self.tournament_rapport.stock_tournament(self.lst_input_tournament)
        tournament_in_play.sort_player()
        tournament_in_play.exec_round()

