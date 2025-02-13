import json
import random
from models.player import Player, players_list
from models.match import Match
from models.round import Round, Round1
from utils.constante import FILE_TOURNAMENT

class Tournois:
    tournament_list = []
    def __init__(self, nom, lieu, date_debut, date_fin, player_number, round_number, description="", round_actuel=0): #rajouter un id
            self.nom = nom
            self.lieu = lieu
            self.date_debut = date_debut
            self.date_fin = date_fin
            self.player_number = player_number
            self.round_actuel = round_actuel
            self.description = description
            self.round_number = round_number
            self.players_inscrits = []
            self.rounds = []
            Tournois.tournament_list.append(self)

    def __str__(self):
        return f"{self.nom} : se déroulera à {self.lieu}. Il débutera le {self.date_debut} et prendra fin le {self.date_fin} "

    def register_player(self, player_id):
        for player in self.players_inscrits:
            if int(player.identifiant) == int(player_id):
                print(f"Le joueur {player.name} {player.surname} est déjà inscrit à ce tournoi.")
                return

            # Recherche du joueur dans la liste
        for player in Player.load_json():
            if int(player.identifiant) == int(player_id):
                self.players_inscrits.append(player)
                print(f"Le joueur {player.name} {player.surname} a été inscrit avec succès.")
                return
        else:
            print("Joueur introuvable.")

    def show_players_inscrits(self):
        if self.players_inscrits:
            print(f"Capacité du tournoi : {len(self.players_inscrits)}/{self.player_number}")
            return "Joueurs inscrits : " + ", ".join(
                f"{player.name} {player.surname}" for player in self.players_inscrits)

        else:
            return "Aucun joueur n'est inscrit au tournoi."

    def to_dict(self):
        return {
            "Nom" : self.nom,
            "Lieu" : self.lieu,
            "Date de debut" : self.date_debut,
            "Date de fin" : self.date_fin,
            "Player number" : self.player_number,
            "Round total" : self.round_number,
            "Description" : self.description,
            "Round actuel": self.round_actuel,
            "Joueurs inscrits" : [[player.name, player.surname] for player in self.players_inscrits]
        }


    def start_tournament(self):
        if len(self.players_inscrits) != self.player_number:
            print("Erreur, le nombre de joueurs inscrit ne permet pas de débuter le tournois.")

        else:
            print("Début du tournois")
            random.shuffle(self.players_inscrits)
            round_instance = Round(int(self.round_actuel + 1))
            for i in range (0, len(self.players_inscrits), 2):
                print("i =", i)
                if i+1 < len(self.players_inscrits):
                 match = Match(self.players_inscrits[i], self.players_inscrits[i+1], round_number=1, time="15")
                 round_instance.add_match(match)
            print("Round :", vars(round_instance))
            print("Number of matches :", len(round_instance.matches))

            self.rounds.append(round_instance)

            print(round_instance.show_matches())


    def save(self):
        try:
            list_tournois = Tournois.load_json() or []  # Évite les erreurs si le fichier est vide
        except (FileNotFoundError, json.JSONDecodeError):
            list_tournois = []

        list_tournois.append(self)
        tournament_data = [tournois.to_dict() for tournois in list_tournois]

        with open(FILE_TOURNAMENT, "w") as f:
            json.dump(tournament_data, f, indent=4)

    @staticmethod
    def load_json():
        with open(FILE_TOURNAMENT, "r") as f:
            tournament_data = json.load(f)
            tournament_list = []
            for data in tournament_data:
                p = Tournois(data["Nom"],
                             data['Lieu'],
                             data['Date de debut'],
                             data['Date de fin'],
                             data['Player number'],
                             data['Round total'],
                             data['Description'],
                             data['Round actuel'],
                             )
                p.players_inscrits = [Player(name, surname, None) for name, surname in data["Joueurs inscrits"]]
                tournament_list.append(p)
            return tournament_list

Tournois_Toulouse = Tournois("Toulouse Master1000", "Toulouse", "14/03/2025", "17/03/2025", 16, 5)
# Tournois_Toulouse.save()
Tournois_Lyon = Tournois("Lyon Master1000", "Lyon", "12/02/2025", "15/02/2025", 8, 4, "aucune", 0)


#print(Tournois_Toulouse.players_inscrits)
#Tournois_Toulouse.add_player(players_list)
#print(Tournois_Toulouse.players_inscrits)
#print(len(Tournois_Toulouse.players_inscrits))
#print(players_list)
#Tournois_Lyon.add_player(players_list)
#print(Tournois_Lyon.players_inscrits)
#print(Tournois_Lyon.players_inscrits[1])
# players_list = Player.load_json()
# Tournois_Lyon.add_player(players_list[:8])
# print(Tournois_Lyon.show_players_inscrits())
# Tournois_Lyon.start_tournament()
# Tournois_Lyon.save_json()

