import json
import random
import uuid
import csv
import os

from models import match
from models.player import Player, players_list
from models.match import Match
from models.round import Round, Round1
from utils.constante import FILE_TOURNAMENT

class Tournois:
    tournament_list = []
    def __init__(self, nom, lieu, date_debut, date_fin, player_number, description="", round_number=4,  round_actuel=0):
            self.id = uuid.uuid4()
            self.nom = nom
            self.lieu = lieu
            self.date_debut = date_debut
            self.date_fin = date_fin
            self.player_number = player_number
            self.description = description
            self.round_actuel = round_actuel
            self.round_number = round_number
            self.players_inscrits = []
            self.rounds = []
            Tournois.tournament_list.append(self)

    def __str__(self):
        return f"{self.nom} : se déroulera à {self.lieu}. Il débutera le {self.date_debut} et prendra fin le {self.date_fin} "

    def register_player(self, player_selected):
        for player in self.players_inscrits:
            if int(player["identifiant"]) == int(player_selected.identifiant):
                print(f"Le joueur avec l'ID {player['identifiant']} est déjà inscrit à ce tournoi.")
                return

        # Recherche du joueur dans la liste
        for player in Player.load_json():
            if int(player.identifiant) == int(player_selected.identifiant):
                player_data = {"identifiant": player.identifiant,
                               "score": player.score}  # Stocker uniquement les infos nécessaires
                self.players_inscrits.append(player_data)
                print(f"Le joueur avec l'ID {player.identifiant} a été inscrit avec succès.")
                self.update()
                return
        else:
            print("Joueur introuvable.")

    def show_players_inscrits(self):
        if self.players_inscrits:
            print(f"Capacité du tournoi : {len(self.players_inscrits)}/{self.player_number}")
            return "Joueurs inscrits : " + ", ".join(
                f"{player}" for player in self.players_inscrits)

        else:
            return "Aucun joueur n'est inscrit au tournoi."

    def to_dict(self):
        return {
            "id": str(self.id),
            "nom": self.nom,
            "lieu": self.lieu,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "player_number": self.player_number,
            "description": self.description,
            "round_total": self.round_number,
            "round_actuel": self.round_actuel,
            "joueurs_inscrits": [[player["identifiant"], player["score"]] for player in self.players_inscrits],
            "rounds": [round.to_dict() for round in self.rounds]
        }

    def advance_to_next_round(self):
        if self.round_actuel == self.round_number:
            self.rounds[-1].state = "Terminé"
            print("Tous les rounds ont été terminés. Fin du tournoi.")
            print("Classement final :\n", self.get_classement())
            return False
        else:
            self.rounds[-1].state = "Terminé"
            new_pairs = self.create_pairs()
            print("Nouveaux matchs pour le round suivant :", new_pairs)
            self.round_actuel += 1
            new_round = Round(self.round_actuel)

            for pair in new_pairs:
                match = Match(pair[0], pair[1], round_number=self.round_actuel, time="15")
                new_round.add_match(match)

            self.rounds.append(new_round)
            self.update()
            print(f"Round {self.round_actuel} ajouté avec {len(new_round.matches)} matchs.")
            return True

    def create_pairs(self):
        classement = self.get_classement()
        pairs = []
        for i in range(0, len(classement), 2):
            if i + 1 < len(classement):
                pairs.append((classement[i], classement[i+1]))
        return pairs


    def get_classement(self):
        classement = sorted(self.players_inscrits, key=lambda player: player["score"], reverse=True)

        print("\nClassement des joueurs :")
        for i, player in enumerate(classement, start=1):
            print(f"{i}. Joueur ID {player['identifiant']} - Score: {player['score']}")
        return classement

    def start_tournament(self):
        if len(self.players_inscrits) != self.player_number:
            print("Erreur, le nombre de joueurs inscrits ne permet pas de débuter le tournoi.")
        else:
            print("Début du tournoi")
            random.shuffle(self.players_inscrits)
            round_instance = Round(int(self.round_actuel + 1))
            self.round_actuel += 1

            for i in range(0, len(self.players_inscrits), 2):
                if i + 1 < len(self.players_inscrits):
                    match = Match(self.players_inscrits[i], self.players_inscrits[i+1], round_number=1, time="15")
                    round_instance.add_match(match)

            print("Round :", round_instance.tour)
            print("Number of matches :", len(round_instance.matches))

            self.rounds.append(round_instance)
            self.update()

            print(round_instance.show_matches())

    def save(self):

        list_tournois = self.load_json()
        list_tournois.append(self)
        tournament_data = [tournois.to_dict() for tournois in list_tournois]

        with open(FILE_TOURNAMENT, "w") as f:
            json.dump(tournament_data, f, indent=4)

    def update(self):
        try:
            list_tournois = Tournois.load_json() or []  # Charge la liste des tournois existants
        except (FileNotFoundError, json.JSONDecodeError):
            list_tournois = []

        nouveau_list_tournois = []
        tournoi_trouve = False

        for tournoi in list_tournois:
            if tournoi.nom == self.nom:  # Si c'est le tournoi à mettre à jour
                nouveau_list_tournois.append(self)  # Ajoute la version mise à jour
                tournoi_trouve = True
            else:
                nouveau_list_tournois.append(tournoi)  # Garde les autres inchangés

        if not tournoi_trouve:  # Si le tournoi n'existe pas encore, on l'ajoute
            nouveau_list_tournois.append(self)

        # Sauvegarde des données mises à jour
        with open(FILE_TOURNAMENT, "w") as f:
            json.dump([t.to_dict() for t in nouveau_list_tournois], f, indent=4)

    @staticmethod
    def load_json():
        with open(FILE_TOURNAMENT, "r") as f:
            tournament_data = json.load(f)
            tournament_list = []

            for data in tournament_data:
                # Création de l'objet Tournois
                p = Tournois(
                    data['nom'],
                    data['lieu'],
                    data['date_debut'],
                    data['date_fin'],
                    data['player_number'],
                    data['description'],
                    data['round_total'],
                    data['round_actuel'],
                )
                p.id = data['id']

                # Chargement des joueurs inscrits
                p.players_inscrits = [
                    {"identifiant": identifiant, "score": score}
                    for identifiant, score in data["joueurs_inscrits"]
                ]

                # Chargement des rounds
                p.rounds = []
                for round_data in data["rounds"]:
                    round_instance = Round(round_data["tour"], round_data["state"])

                    # Chargement des matches
                    for match_data in round_data["matches"]:

                        if isinstance(match_data, list) and len(match_data) == 2:
                            player1_id = match_data[0][0]  # ID du premier joueur
                            player2_id = match_data[1][0]  # ID du deuxième joueur

                            match = Match(player1_id, player2_id, round_data["tour"], "15")
                            match.result = match_data  # [(id_joueur1, score1), (id_joueur2, score2)]
                            round_instance.add_match(match)
                        else:
                            print("Erreur : Format inattendu pour match_data :", match_data)

                    p.rounds.append(round_instance)

                tournament_list.append(p)

        return tournament_list

    # def generate_report(self, tournament, round_instance):
    #
    #     file_exists = os.path.exists('tournament_report.csv')
    #     with open('tournament_report.csv', mode='a', newline='') as file:
    #         writer = csv.writer(file)
    #
    #         if not file_exists:
    #             writer.writerow(['Tournament', 'Round', 'Player 1', 'Player 2', 'Score Player 1', 'Score Player 2'])
    #
    #         for match in round_instance.matches:
    #             player1 = Player.get_player_by_id(match.players[0].identifiant, Player.load_json())
    #             player2 = Player.get_player_by_id(match.players[1].identifiant, Player.load_json())
    #             score1 = match.result[0][1] if match.result and len(match.result) > 0 else 'N/A'
    #             score2 = match.result[1][1] if match.result and len(match.result) > 1 else 'N/A'
    #
    #         writer.writerow([tournament.nom, round_instance.tour, f"{player1.name} {player1.surname}",
    #                          f"{player2.name} {player2.surname}", score1, score2])
    #     print("Rapport généré dans 'tournament_report.csv'.")
    #

Tournois_Toulouse = Tournois("Toulouse Master1000", "Toulouse", "14/03/2025", "17/03/2025", 16, 5)
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
