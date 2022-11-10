from Views.match_view import DisplayMatch

class Match:
    """Initialisation d'un Match"""
    def __init__(self, pair):
        self.pair = pair
        self.match_view = DisplayMatch


    def __str__(self):
        match_presentation = f'Ce match oppose {self.pair[0]} et {self.pair[1]}.'
        return match_presentation

    def result(self):
        list_pair = []
        for i in self.pair.keys():
            list_pair.append(i)
        result = self.match_view.enter_result(list_pair)
        if result == 0:
            self.pair[list_pair[0]] += 0.5
            self.pair[list_pair[1]] += 0.5
        elif result == list_pair[0]:
            self.pair[list_pair[0]] += 1
        elif result == list_pair[1]:
            self.pair[list_pair[1]] += 1

        return self.pair
