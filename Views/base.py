class View:

#   def menu(self):

    def inp_create_player(self):
        ln = input("Entrez le nom du joueur :\n")
        fn = input("Entrez le prénom du joueur :\n")
        bd = input("Entrez la date de naissance du joueur (DD/MM/AAAA) :\n")
        gd = input("Entrez le genre du joueur :\n")
        gr = input("Entrez le classement global du joueur :\n")

        return ln, fn, bd, gd, gr
