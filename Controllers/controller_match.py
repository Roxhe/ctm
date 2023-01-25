from Views.match_view import DisplayMatch
from Models.model_match import Match


class MatchC:
    """Initialisation d'un Match"""
    def __init__(self, pair):
        self.match = Match(pair)
        self.match_view = DisplayMatch
        self.match_and_result = 0

    def __str__(self):
        match_presentation = f'Ce match oppose {self.match.pair[0]} et {self.match.pair[1]}.'
        return match_presentation

    def result(self):
        list_pair = []
        for i in self.match.pair.keys():
            list_pair.append(i)
        result = self.match_view.enter_result(list_pair)
        if result == 0:
            self.match.pair[list_pair[0]] += 0.5
            self.match.pair[list_pair[1]] += 0.5
        elif result == list_pair[0]:
            self.match.pair[list_pair[0]] += 1
        elif result == list_pair[1]:
            self.match.pair[list_pair[1]] += 1

        self.match_and_result = (list_pair[0], list_pair[1], result)
        return self.match.pair
