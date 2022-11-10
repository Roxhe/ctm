from Models.model_player import Player


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
