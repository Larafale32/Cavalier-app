import random
from player import Player, players

class Tournois:
    def __init__(self, nom, lieu, date_debut, date_fin, description="", round_actuel=1, round_number=4 ):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.round_actuel = round_actuel
        self.description = description
        self.round_number = round_number
        self.players_inscrits = []

    def __str__(self):
        return (f"Le tournois, {self.nom} se déroulera à {self.lieu}. Il débutera le {self.date_debut} et prendra fin le "
                f"{self.date_fin}.\n Joueurs inscris : "
                f"{self.players_inscrits}")

    def add_player(self, players_list):
        self.players_inscrits.extend(players_list)

    def show_players_inscrits(self):
        player_info = "\n".join([str(player) for player in self.players_inscrits])
        return f"Joueurs inscrits :\n{player_info}"


    def to_dict(self):
        return {
            "Nom" : self.nom,
            "Lieu" : self.lieu,
            "Date de début" : self.date_debut,
            "Date de fin" : self.date_fin,
            "Round total" : self.round_number,
            "Round actuel" : self.round_actuel,
            "Description" : self.description
        }

    def start_tournament(self):
        if len(self.players_inscrits) in [8, 16, 32, 64, 128]:
            print("Début du tournois")
            random.shuffle(self.players_inscrits)
            pairs = []
            for i in range (0, len(self.players_inscrits), 2):
                if i+1 < len(self.players_inscrits):
                 pairs.append(f"{self.players_inscrits[i]} vs {self.players_inscrits[i+1]}")
            print("\n".join(pairs))
        else:
            print("Erreur, le nombre de joueurs inscrit ne permet pas de débuter le tournois.")

Tournois_Lyon = Tournois("Master100", "Lyon", "12/02/2025", "15/02/2025")
Tournois_Lyon.add_player((players[0], players[1], players[2], players[3], players[4], players[5], players[6], players[7]))

print(Tournois_Lyon.show_players_inscrits())
Tournois_Lyon.start_tournament()