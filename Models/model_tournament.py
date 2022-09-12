from model_player import Player
from model_round import Round

class Tournament:
    """Initialisation d'un Tournoi"""
    def __init__(self, name, place, date,  players=[], nb_of_rounds=4):
        self.name = name
        self.place = place
        self.date = date
        self.players = players
        self.nb_of_rounds = nb_of_rounds
        self.dict_fsort = {}
        self.rem_id = []
        self.players_fmatch = []
        self.final_result = []

    def __str__(self):
        tournament_presentation = f'Ce tournoi "{self.name}", se déroule à "{self.place}", le "{self.date}".'
        return tournament_presentation

    def sort_player(self):

        for player in self.players:
            self.dict_fsort[player] = player.global_rank

        self.dict_fsort = dict(sorted(self.dict_fsort.items(), key=lambda x: x[1], reverse=True))
        self.players = list(self.dict_fsort)

        for player in self.players:
            player.id = self.players.index(player) + 1
            self.rem_id.append(f"{player.last_name} {player.first_name} portera le numéro {player.id}.")
            print(f"{player.last_name} {player.first_name} portera le numéro {player.id}.")
            self.players_fmatch.append(player.id)

        return self.players_fmatch

    def reminds_id(self):
        for player in self.players:
            print(f"{player.last_name} {player.first_name} porte le numéro {player.id}.")


    def exec_round(self):

        print("Début Tour 1")
        round_m = Round(self.players_fmatch)
        round_m.create_pair_round1()
        round_m.run_match()
        print("Fin Tour 1")
        o = input("Pour un rappel des numéros de joueur tapé : y\n"
                  "si non, appuyer sur Entrée\n")
        if o == 'y':
            print(self.reminds_id())

        for i in range(self.nb_of_rounds - 1):
            print(f"Debut Tour {i+2}")
            round_m.create_pair_otherr()
            round_m.run_match()
            print(f"Fin Tour {i + 2}")
            o = input("Pour un rappel des numéros de joueur tapé : y\n"
                      "Pour continuer, appuyer sur Entrée\n")
            if o == 'y':
                print(self.reminds_id())

        for k, l in zip(round_m.score_dict.keys(), round_m.score_dict.values()):
            a = (k, l)
            self.final_result.append(a)

        for n, m in zip(list(range(1, 8+1)), self.final_result):
            for player in self.players:
                if m[0] == player.id:
                    p = f"{player.last_name} {player.first_name}"
            print(f"{n}. Nom : {p}\n ID : {m[0]}\n Score: {m[1]}")

