from model_player import Player
from model_round import Round

class Tournament:
    """Initialisation d'un Tournoi"""
    def __init__(self, name, place, date,  players = [], nb_of_rounds=4):
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
            self.dict_fsort[player.last_name] = player.global_rank

        self.dict_fsort = dict(sorted(self.dict_fsort.items(), key=lambda x: x[1], reverse=True))
        print(self.dict_fsort)

        for player in self.players:
            player.id = self.players.index(player) + 1
            self.rem_id.append(f"{player.last_name} {player.first_name} portera le numéro {player.id}.")
            print(f"{player.last_name} {player.first_name} portera le numéro {player.id}.")
            self.players_fmatch.append(player.id)

        return self.players_fmatch

    def reminds_id(self):

        for rid in self.rem_id:
            print(rid)

    def exec_round(self):
        print("Début Tour 1")
        round_m = Round(self.players_fmatch)
        round_m.create_pair_round1()
        round_m.run_match()
        print("Fin Tour 1")
        for i in range(self.nb_of_rounds - 1):
            print(f"Debut Tour {i+2}")
            round_m.create_pair_otherr()
            round_m.run_match()
            print(f"Fin Tour {i + 2}")

        for k, l in zip(round_m.score_dict.keys(), round_m.score_dict.values()):
            a = (k, l)
            self.final_result.append(a)

        for n, m in zip(list(range(1, 8+1)), self.final_result):
            print(f"{n}.ID et score: {m}")
