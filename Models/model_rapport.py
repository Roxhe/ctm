from Models.model_player import Player
from Models.model_tournament import Tournament


class Rapport:

    def __init__(self):
        self.list_stock_players = [Player("André", "Albert", "01/01/1991", "n", 10),
                                   Player("Breau", "Brigitte", "02/02/1992", "n", 12),
                                   Player("Charles", "Charlie", "03/03/1993", "n", 3),
                                   Player("Drap", "Dorian", "04/04/1994", "n", 40),
                                   Player("Emph", "Ethan", "05/05/1995", "n", 5),
                                   Player("Friand", "Felix", "06/06/1996", "n", 36),
                                   Player("Grand", "Guy", "07/07/1997", "n", 7),
                                   Player("Henri", "Hugo", "08/08/1998", "n", 56)]
        self.list_stock_tournament = []
        self.player = 0
        self.tournament = 0

    def stock_player(self, lst):
        self.player = Player(lst[0], lst[1], lst[2], lst[3], lst[4])
        self.list_stock_players.append(self.player)
        return self.player

    def return_player_list(self):
        i = 0
        for self.player in self.list_stock_players:
            i += 1
            print(f"{i}. ", self.player.__str__())

    def stock_tournament(self, lst_t, players):
        self.tournament = Tournament(lst_t[0], lst_t[1], lst_t[2], players)
        self.list_stock_tournament.append(self.tournament)
        return self.tournament

    def return_tournament_list(self):
        for self.tournament in self.list_stock_tournament:
            print(self.tournament.__str__())

