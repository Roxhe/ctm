
class Round1():
    """Initialisation du tour 1"""

    def __init__(self, list_players):
        self.list_players = list_players
        self.played_match = []

    def create_pair(self, list_players):
        pair_list = []

        list_players_h1 = list_players[:len(list_players) // 2]
        list_players_h2 = list_players[len(list_players) // 2:]
        for i, j in zip(list_players_h1, list_players_h2):
            i = (i, 0)
            j = (j, 0)
            k = (i, j)
            pair_list.append(dict(k))
        return pair_list


######### Test Zone ##########

list_joueur_test = [1, 2, 3, 4, 5, 6, 7, 8]

round1 = Round1(list_joueur_test)
print(round1.create_pair(list_joueur_test))


