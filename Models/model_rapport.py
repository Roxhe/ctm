from Models.model_player import Player
from Models.model_tournament import Tournament
from tinydb import TinyDB, Query

class Rapport:

    def __init__(self):
        self.list_stock_players = []
        self.list_stock_tournament = []
        self.player = 0
        self.tournament = 0
        self.db = TinyDB('db.json')
        self.players_table = self.db.table("players")
        self.tournaments_table = self.db.table("tournaments")

    def stock_player(self, lst):
        self.player = Player(lst[0], lst[1], lst[2], lst[3], lst[4])
        self.list_stock_players.append(self.player)
        return self.player

    def return_player_list(self):
        choice = int(input("Taper 1 pour afficher en ordre alphabétique.\nTaper 2 pour afficher par classement.\n"))
        match choice:
            case 1:
                self.list_stock_players.sort(key=lambda player: player.last_name)
            case 2:
                self.list_stock_players.sort(key=lambda player: player.global_rank, reverse=True)
        i = 0
        for self.player in self.list_stock_players:
            i += 1
            print(f"{i}. ", self.player.__str__())

    def return_tournament_list(self):
        i = 0
        for self.tournament in self.list_stock_tournament:
            i += 1
            print(f"{i}.", self.tournament.__str__())

    def return_tournament_played_match(self):
        selec_tournament = int(input("Rentrez le numéro associé au tournoi pour plus de détails : \n"))
        self.list_stock_tournament[selec_tournament - 1].players.sort(key=lambda player: player.last_name)
        print("Liste de joueur par ordre alphabétique :")
        i = 0
        for player in self.list_stock_tournament[selec_tournament - 1].players:
            i += 1
            print(f"{i}. ", player.__str__())
        print("Numéro des joueurs pendant le tournoi :")
        i = 0
        j = 1
        for id in self.list_stock_tournament[selec_tournament - 1].rem_id:
            print(id)
        for match in self.list_stock_tournament[selec_tournament - 1].played_match_result:

            if i % 4 == 0:
                print(f"Round {j}")
                j += 1

            if match[2] > 0:
                print(f"Match opposant {match[0]} et {match[1]} avec pour vainqueur {match[2]}")
                i += 1
            else:
                print(f"Match opposant {match[0]} et {match[1]} ayant comme résultat une égalité")
                i += 1

        print("Liste des joueurs par classement dans le tournoi :")
        for n, m in zip(list(range(1, 8 + 1)), self.list_stock_tournament[selec_tournament - 1].final_result):
            for player in self.list_stock_tournament[selec_tournament - 1].players:
                if m[0] == player.id:
                    p = f"{player.last_name} {player.first_name}"
            print(f"{n}. Nom : {p}\n ID : {m[0]}\n Score: {m[1]}")

    def suppr_player(self, players_to_suppr):
        del self.list_stock_players[players_to_suppr - 1]

    def modif_player_rank(self, players_to_modif, new_rank):
        self.list_stock_players[players_to_modif - 1].global_rank = new_rank

    def serialize_player(self):
        self.players_table.truncate()

        for player in self.list_stock_players:
            serialized_player = {
                "last_name": player.last_name,
                "first_name": player.first_name,
                "birthdate": player.birthdate,
                "gender": player.gender,
                "global_rank": player.global_rank
            }
            self.players_table.insert(serialized_player)

    def deserialize_player(self):
        for player in self.players_table:
            last_name = player['last_name']
            first_name = player['first_name']
            birthdate = player['birthdate']
            gender = player['gender']
            global_rank = player['global_rank']
            player = Player(last_name=last_name,
                            first_name=first_name,
                            birthdate=birthdate,
                            gender=gender,
                            global_rank=global_rank)
            self.list_stock_players.append(player)

    def serialize_tournament(self):
        self.tournaments_table.truncate()

        for tournament in self.list_stock_tournament:
            self.tournaments_table.insert(tournament.serialize())

    def deserialize_tournament(self):
        for tournament in self.tournaments_table:
            name = tournament['name']
            place = tournament['place']
            date = tournament['date']
            players = tournament['players']
            nb_of_rounds = tournament['nb_of_rounds']
            dict_fsort = tournament['dict_fsort']
            rem_id = tournament['rem_id']
            final_result = tournament['final_result']
            played_match = tournament['played_match']
            tournament = Tournament(name=name,
                                    place=place,
                                    date=date,
                                    players=players,
                                    nb_of_rounds=nb_of_rounds,
                                    dict_fsort=dict_fsort,
                                    rem_id=rem_id,
                                    final_result=final_result,
                                    played_match=played_match)
            self.list_stock_tournament.append(tournament)
