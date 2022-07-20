
class Round1():
    """Initialisation du tour 1"""

    def __init__(self, list_players):
        self.list_players = list_players
        self.pair_list = []
        self.played_match = []

    def create_pair(self, list_players, pair_list):
        tuple_pair = []
        list_players_h1 = list_players[:len(list_players) // 2]
        list_players_h2 = list_players[len(list_players) // 2:]
        for i, j in zip(list_players_h1, list_players_h2):
            tuple_pair.append(((i, 0), (j, 0)))
        for k in range(len(tuple_pair)):
            print(dict(tuple_pair[k]))
            pair_list.append(dict(tuple_pair[k]))
        return pair_list


######### Test Zone ##########

list_joueur_test = [1, 2, 3, 4, 5, 6, 7, 8]

round1 = Round1(list_joueur_test)
print(round1.create_pair(list_joueur_test, pair_list=[]))


