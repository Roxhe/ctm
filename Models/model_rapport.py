from Models.model_player import Player
from Models.model_tournament import Tournament
from Views.rapport_view import DisplayRapport
from Controllers.controller_round import RoundController
from tinydb import TinyDB, Query

class Rapport:

    def __init__(self):
        self.list_stock_players = []
        self.list_stock_tournaments = []
        self.player = 0
        self.tournament = 0
        self.rapport_view = DisplayRapport()
        self.db = TinyDB('db.json')
        self.players_table = self.db.table("players")
        self.db_tournament = TinyDB('db_tournament.json')
        self.tournaments_table = self.db_tournament.table("tournaments")

    def stock_player(self, lst):
        self.player = Player(lst[0], lst[1], lst[2], lst[3], lst[4])
        self.list_stock_players.append(self.player)
        return self.player

    def return_players_list(self):
        self.rapport_view.return_players_list(self.list_stock_players)

    def return_tournaments_list(self):
        self.rapport_view.return_tournaments_list(self.list_stock_tournaments)

    def return_tournament_played_match(self):
        self.rapport_view.return_tournament_played_match(self.list_stock_tournaments)

    def suppr_player(self, players_to_suppr):
        del self.list_stock_players[players_to_suppr - 1]

    def modif_player_rank(self, players_to_modif, new_rank):
        self.list_stock_players[players_to_modif - 1].global_rank = new_rank

    def serialize_player(self):
        self.players_table.truncate()

        for player in self.list_stock_players:
            self.players_table.insert(player.serialize())

    def deserialize_player(self):
        for player in self.players_table:
            last_name = player['LastName']
            first_name = player['FirstName']
            birthdate = player['Birthdate']
            gender = player['Gender']
            global_rank = player['GlobalRank']
            player = Player(last_name=last_name,
                            first_name=first_name,
                            birthdate=birthdate,
                            gender=gender,
                            global_rank=global_rank)
            self.list_stock_players.append(player)

    def serialize_tournament(self):
        self.tournaments_table.truncate()
        for tournament in self.list_stock_tournaments:
            self.tournaments_table.insert(tournament.serialize())

    def deserialize_tournament(self):
        for tournament in self.tournaments_table:
            name = tournament['Name']
            place = tournament['Place']
            date = tournament['Date']

            deserialized_players = []
            players = tournament['Players']
            for player in players:
                last_name = player['LastName']
                first_name = player['FirstName']
                birthdate = player['Birthdate']
                gender = player['Gender']
                global_rank = player['GlobalRank']
                player = Player(last_name=last_name,
                                first_name=first_name,
                                birthdate=birthdate,
                                gender=gender,
                                global_rank=global_rank)
                deserialized_players.append(player)

            nb_of_rounds = tournament['Nb_of_rounds']
            rem_id = tournament['Rem_id']
            final_result = tournament['Final_result'],
            played_match_result = tournament['Played_match_result']
            round_time = tournament['Round_time']

            tournament = Tournament(name=name,
                                    place=place,
                                    date=date,
                                    players=deserialized_players,
                                    nb_of_rounds=nb_of_rounds,
                                    rem_id=rem_id,
                                    final_result=final_result,
                                    played_match_result=played_match_result,
                                    round_time=round_time)

            self.list_stock_tournaments.append(tournament)
