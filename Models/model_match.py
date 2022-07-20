
class Match:
    """Initialisation d'un Match"""
    def __init__(self, pair):
        self.pair = pair

    def __str__(self):
        match_presentation = f'Ce match oppose {self.pair[0]} et {self.pair[1]}.'
        return match_presentation

    def result(self):
        list_pair = []
        for i in self.pair.keys():
            list_pair.append(i)
        print(list_pair)
        result_inp = int(input(f"Veuillez rentrer le nom du vainqueur entre {list_pair[0]} "
                           f"et {list_pair[1]}\n"
                             f"En cas d'égalité rentrez 0\n"))

        if result_inp == 0:
            self.pair[list_pair[0]] += 0.5
            self.pair[list_pair[1]] += 0.5
        elif result_inp == list_pair[0]:
            self.pair[list_pair[0]] += 1
        elif result_inp == list_pair[1]:
            self.pair[list_pair[1]] += 1

        print(self.pair)
        return self.pair



######### Test Zone ##########

match1 = Match({1: 0, 5: 0})
match1.result()
