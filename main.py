class Player:
    """Initialisation des joueurs"""
    def __init__(self, last_name, first_name, birthdate, gender, global_rank=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.global_rank = global_rank
        self.score = 0.0
        self.id = 0

    def __str__(self):
        player_presentation = f'Nom : {self.last_name}/ Prénom : {self.first_name}/ Rang : {self.global_rank}'
        return player_presentation


players = []

while True:

    ln = input("Entrez le nom du joueur :\n")
    fn = input("Entrez le prénom du joueur :\n")
    bd = input("Entrez la date de naissance du joueur (DD/MM/AAAA) :\n")
    gd = input("Entrez le genre du joueur :\n")
    gr = int(input("Entrez le classement global du joueur :\n"))

    player = Player(ln, fn, bd, gd, gr)
    players.append(player)
    print(f"Le joueur suivant a été ajouté :"
          f"{player.__str__()}\n")

    end_or_not = input("Souhaitez vous recréer un joueur ? yes : y / no : n\n")
    if end_or_not == 'y':
        continue
    elif end_or_not == 'n':
        break

for player in players:
    print(player.__str__())
