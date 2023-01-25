class DisplayMatch:

    def __init__(self):
        pass

    def enter_result(pair):
        result_inp = None
        while result_inp != 0 and result_inp != int(pair[0]) and result_inp != int(pair[1]):

            result_inp = int(input(f"Veuillez rentrer le nom du vainqueur entre {pair[0]} "
                    f"et {pair[1]}\n"
                    f"En cas d'égalité rentrez 0\n"))

        return result_inp
