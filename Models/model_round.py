from model_match import Match



class Round():
    """Initialisation du tour 1"""

    def __init__(self, list_players):
        self.list_players = list_players
        self.played_match = []
        self.pair_fmatch = []
        self.score_dict = {}

    def create_pair_round1(self):

        list_players_h1 = self.list_players[:len(self.list_players) // 2]
        list_players_h2 = self.list_players[len(self.list_players) // 2:]
        for i, j in zip(list_players_h1, list_players_h2):
            i = (i, 0)
            j = (j, 0)
            k = (i, j)
            self.pair_fmatch.append(dict(k))
            self.played_match.append((i[0], j[0]))

        return self.pair_fmatch, self.played_match

    def create_pair_otherr(self):
        m = []

        j = 2
        for k, l in zip(self.score_dict.keys(), self.score_dict.values()):
            a = (k, l)
            m.append(a)

        for i in range(len(self.list_players)):
            i = 0

            if len(m) == 0:
                break
            if (m[i][0], m[i + 1][0]) not in self.played_match:
                self.pair_fmatch.append(dict((m[i], m[i + 1])))
                self.played_match.append((m[i][0], m[i + 1][0]))
                m.remove(m[i])
                m.remove(m[i])
            else:
                try:
                    if (m[i][0], m[i + j][0]) not in self.played_match:
                        try:
                            self.pair_fmatch.append(dict((m[i], m[i + j])))
                            self.played_match.append((m[i][0], m[i + j][0]))
                            m.remove(m[i])
                            m.remove(m[i+j-1])
                        except IndexError:
                            self.pair_fmatch.append(dict((m[i], m[i + 1])))
                            self.played_match.append((m[i][0], m[i + 1][0]))
                            m.remove(m[i])
                            m.remove(m[i])
                    else:
                        j += 1

                except IndexError:
                    self.pair_fmatch.append(dict((m[i], m[i + 1])))
                    self.played_match.append((m[i][0], m[i + 1][0]))
                    m.remove(m[i])
                    m.remove(m[i])

    def run_match(self):

        for i in range(len(self.pair_fmatch)):
            match = Match(self.pair_fmatch[i])
            match.result()
            self.pair_fmatch[i].update
            self.score_dict.update(self.pair_fmatch[i])

        self.score_dict = dict(sorted(self.score_dict.items(), key=lambda x: x[1], reverse=True))
        self.list_players = list(self.score_dict.keys())

        self.pair_fmatch.clear()
        return self.score_dict





######### Test Zone ##########


list_joueur_test = [1, 2, 3, 4, 5, 6, 7, 8]

"""round1 = Round(list_joueur_test)
round1.create_pair_round1()
round1.run_match()
print("Fin Tour 1", round1.played_match, '\n', round1.score_dict)
round1.create_pair_otherr()
round1.run_match()
round1.create_pair_otherr()
round1.run_match()
round1.create_pair_otherr()
round1.run_match()

print(round1.score_dict)
print(round1.played_match)
"""