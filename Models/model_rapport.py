from Models.model_player import Player
from Models.model_tournament import Tournament

class Rapport:

    def __init__(self):
        self.list_stock_players = []
        self.list_stock_tournament = []
        self.player = 0
        self.tournament = 0

    def stock_player(self, lst):
        self.player = Player(lst[0], lst[1], lst[2], lst[3], lst[4])
        self.list_stock_players.append(self.player)
        return self.player

    def return_player_list(self):
        for self.player in self.list_stock_players:
            print(self.player.__str__())

    def stock_tournament(self, lst_t):
        player1 = Player("André", "Albert", "01/01/1991", "n", 10)
        player2 = Player("Breau", "Brigitte", "02/02/1992", "n", 12)
        player3 = Player("Charles", "Charlie", "03/03/1993", "n", 3)
        player4 = Player("Drap", "Dorian", "04/04/1994", "n", 40)
        player5 = Player("Emph", "Ethan", "05/05/1995", "n", 5)
        player6 = Player("Friand", "Felix", "06/06/1996", "n", 36)
        player7 = Player("Grand", "Guy", "07/07/1997", "n", 7)
        player8 = Player("Henri", "Hugo", "08/08/1998", "n", 56)
        players = [player1, player8, player7, player6, player5, player4, player3, player2]

        self.tournament = Tournament(lst_t[0], lst_t[1], lst_t[2], players)

        self.list_stock_tournament.append(self.tournament)
        return self.tournament

    def return_tournament_list(self):
        for self.tournament in self.list_stock_tournament:
            print(self.tournament.__str__())