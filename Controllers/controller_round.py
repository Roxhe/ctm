from Controllers.controller_match import MatchC
from Models.model_round import Round


class RoundController:
    """Initialisation du tour 1"""

    def __init__(self, list_players):
        self.list_players = list_players
        self.m_round = Round()
        self.match_and_result = []

    def create_pair_round1(self):

        list_players_h1 = self.list_players[:len(self.list_players) // 2]
        list_players_h2 = self.list_players[len(self.list_players) // 2:]
        for i, j in zip(list_players_h1, list_players_h2):
            i = (i, 0)
            j = (j, 0)
            k = (i, j)
            self.m_round.pair_fmatch.append(dict(k))
            self.m_round.played_match.append((i[0], j[0]))

        return self.m_round.pair_fmatch, self.m_round.played_match

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
            if (m[i][0], m[i + 1][0]) not in self.m_round.played_match:
                self.m_round.pair_fmatch.append(dict((m[i], m[i + 1])))
                self.m_round.played_match.append((m[i][0], m[i + 1][0]))
                m.remove(m[i])
                m.remove(m[i])
            else:
                try:
                    if (m[i][0], m[i + j][0]) not in self.m_round.played_match:
                        try:
                            self.m_round.pair_fmatch.append(dict((m[i], m[i + j])))
                            self.m_round.played_match.append((m[i][0], m[i + j][0]))
                            m.remove(m[i])
                            m.remove(m[i+j-1])
                        except IndexError:
                            self.m_round.pair_fmatch.append(dict((m[i], m[i + 1])))
                            self.m_round.played_match.append((m[i][0], m[i + 1][0]))
                            m.remove(m[i])
                            m.remove(m[i])
                    else:
                        j += 1

                except IndexError:
                    self.m_round.pair_fmatch.append(dict((m[i], m[i + 1])))
                    self.m_round.played_match.append((m[i][0], m[i + 1][0]))
                    m.remove(m[i])
                    m.remove(m[i])

    def run_match(self):

        for i in range(len(self.m_round.pair_fmatch)):
            match = MatchC(self.m_round.pair_fmatch[i])
            match.result()
            self.match_and_result.append(match.match_and_result)
            self.m_round.pair_fmatch[i].update
            self.m_round.score_dict.update(self.m_round.pair_fmatch[i])

        self.score_dict = dict(sorted(self.m_round.score_dict.items(), key=lambda x: x[1], reverse=True))
        self.list_players = list(self.score_dict.keys())

        self.m_round.pair_fmatch.clear()
        return self.score_dict
