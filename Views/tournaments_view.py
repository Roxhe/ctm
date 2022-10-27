from Models.model_rapport import Rapport


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
        return self.lst_input_tournament, self.tournament_rapport

    def return_all_tournament(self):
        self.tournament_rapport.return_tournament_list()




