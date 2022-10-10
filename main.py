from Models.model_player import Player

player1 = Player("André", "Albert", "01/01/1991", "n", 10)
player2 = Player("Breau", "Brigitte", "02/02/1992", "n", 12)
player3 = Player("Charles", "Charlie", "03/03/1993", "n", 3)
player4 = Player("Drap", "Dorian", "04/04/1994", "n", 40)
player5 = Player("Emph", "Ethan", "05/05/1995", "n", 5)
player6 = Player("Friand", "Felix", "06/06/1996", "n", 36)
player7 = Player("Grand", "Guy", "07/07/1997", "n", 7)
player8 = Player("Henri", "Hugo", "08/08/1998", "n", 56)
players = [player1, player8, player7, player6, player5, player4, player3, player2]


last_name_inp = input("Nom de famille")

research = filter(lambda p: p.last_name == last_name_inp, players)
joueur_selec = list(research)

for player in joueur_selec:
    print(player.__str__())
