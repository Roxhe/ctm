import datetime

from Controllers.controller_round import RoundController
from Views.tournaments_view import DisplayTournament
from Views.players_view import DisplayPlayer
from Models.model_tournament import Tournament

class TournamentController:

    def __init__(self):
        self.view_player = DisplayPlayer()
        self.view_tournament = DisplayTournament()
        self.tournament = 0
        self.players = []


    def create_tournament(self, tournament_rapport):
        self.players.clear()
        self.view_tournament.prompt_tournament()
        lst_t = self.view_tournament.lst_input_tournament
        tournament_rapport.return_players_list()
        for i in range(8):
            ind_player = self.view_tournament.selec_player()
            self.players.append(tournament_rapport.list_stock_players[ind_player - 1])
        self.tournament = Tournament(lst_t[0], lst_t[1], str(datetime.date.today()), self.players)
        tournament_rapport.list_stock_tournament.append(self.tournament)
        return self.tournament, self.players

    def create_tournament_new_players(self, tournament_rapport):
        self.players.clear()
        self.view_tournament.prompt_tournament()
        lst_t = self.view_tournament.lst_input_tournament
        self.players = self.view_player.prompt_players_new_tournament(tournament_rapport)
        self.tournament = Tournament(lst_t[0], lst_t[1], lst_t[2], self.players)
        tournament_rapport.list_stock_tournament.append(self.tournament)
        return self.tournament, self.players

    def sort_player(self):
        self.tournament.players = self.players
        for player in self.tournament.players:
            self.tournament.dict_fsort[player] = player.global_rank

        self.tournament.dict_fsort = dict(sorted(self.tournament.dict_fsort.items(), key=lambda x: x[1], reverse=True))
        self.tournament.players = list(self.tournament.dict_fsort)

        for player in self.tournament.players:
            player.id = self.tournament.players.index(player) + 1
            self.tournament.rem_id.append(f"{player.last_name} {player.first_name} porte le numéro {player.id}.")
            self.tournament.players_fmatch.append(player.id)

        return self.tournament

    def exec_rounds(self):

        self.view_tournament.rem_id(self.tournament)
        self.view_tournament.display_round1_bounds()
        round_m = RoundController(self.tournament.players_fmatch)
        round_m.create_pair_round1()
        self.round_tracker()
        round_m.run_match()
        self.round_tracker()
        self.view_tournament.reminds_id(self.tournament)


        for i in range(self.tournament.nb_of_rounds - 1):

            self.view_tournament.display_round_bounds(i)
            round_m.create_pair_otherr()
            self.round_tracker()
            round_m.run_match()
            self.round_tracker()
            self.view_tournament.reminds_id(self.tournament)


        for k, l in zip(round_m.score_dict.keys(), round_m.score_dict.values()):
            a = (k, l)
            self.tournament.final_result.append(a)

        self.view_tournament.display_final_result(self.tournament)
        for played_match_result in round_m.match_and_result:
            self.tournament.played_match_result.append(played_match_result)

    def round_tracker(self):
        dt = str(datetime.datetime.now())
        dt = dt[:-7]
        self.tournament.round_time.append(dt)

    def tournament_in_play(self):
        self.sort_player()
        self.exec_rounds()
