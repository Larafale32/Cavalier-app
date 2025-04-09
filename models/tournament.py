import json
import random
import uuid
from datetime import datetime

from models.player import Player
from models.match import Match
from models.round import Round
from utils.constante import FILE_TOURNAMENT


class Tournois:
    tournament_list = []

    def __init__(
        self,
        nom,
        lieu,
        date_debut,
        date_fin,
        player_number,
        state="en attente",
        description="",
        round_number=4,
        round_actuel=0,
    ):
        self.id = uuid.uuid4()
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.player_number = player_number
        self.state = state
        self.description = description
        self.round_actuel = round_actuel
        self.round_number = round_number
        self.players_inscrits = []
        self.rounds = []
        Tournois.tournament_list.append(self)

    def __str__(self):
        return f"{self.nom} : se déroulera à {self.lieu}. Il débutera le {self.date_debut} et prendra fin le {self.date_fin} "

    def delete(self):
        try:
            tournois_list = Tournois.load_json() or []
        except (FileNotFoundError, json.JSONDecodeError):
            tournois_list = []

        updated_list = [t for t in tournois_list if t.nom != self.nom]

        list_to_save = []
        for tournoi in updated_list:
            tournoi_dict = tournoi.to_dict()
            tournoi_dict["date_debut"] = (
                tournoi_dict["date_debut"].strftime("%d/%m/%Y")
                if isinstance(tournoi_dict["date_debut"], datetime)
                else tournoi_dict["date_debut"]
            )
            tournoi_dict["date_fin"] = (
                tournoi_dict["date_fin"].strftime("%d/%m/%Y")
                if isinstance(tournoi_dict["date_fin"], datetime)
                else tournoi_dict["date_fin"]
            )
            list_to_save.append(tournoi_dict)

        with open(FILE_TOURNAMENT, "w") as f:
            json.dump(list_to_save, f, indent=4)

    def register_player(self, player_selected):
        # Vérification si le joueur est déjà inscrit
        for player in self.players_inscrits:
            if int(player[0]) == int(
                player_selected.identifiant
            ):  # player[0] est l'ID du joueur
                print(f"Le joueur avec l'ID {player[0]} est déjà inscrit à ce tournoi.")
                return

        # Recherche du joueur dans la liste des joueurs existants
        for player in Player.load_json():
            if int(player.identifiant) == int(player_selected.identifiant):
                # Stockage des données du joueur dans une sous-liste [identifiant, score]
                player_data = [player.identifiant, player.score]
                self.players_inscrits.append(player_data)
                print(
                    f"Le joueur avec l'ID {player.identifiant} a été inscrit avec succès."
                )
                self.update()
                return
        else:
            print("Joueur introuvable.")

    def show_players_inscrits(self):
        if self.players_inscrits:
            print(
                f"Capacité du tournoi : {len(self.players_inscrits)}/{self.player_number}"
            )
            return "Joueurs inscrits : " + ", ".join(
                f"{player}" for player in self.players_inscrits
            )

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
            "status": self.state,
            "description": self.description,
            "round_total": self.round_number,
            "round_actuel": self.round_actuel,
            "joueurs_inscrits": self.players_inscrits,
            "rounds": [round.to_dict() for round in self.rounds],
        }

    def advance_to_next_round(self):
        if self.round_actuel == self.round_number:
            self.rounds[-1].state = "Terminé"
            self.state = "Terminé"
            self.update()
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
                match = Match(
                    pair[0], pair[1], round_number=self.round_actuel, time="15"
                )
                new_round.add_match(match)

            self.rounds.append(new_round)
            self.update()
            print(
                f"Round {self.round_actuel} ajouté avec {len(new_round.matches)} matchs."
            )
            return True

    def create_pairs(self):
        classement = self.get_classement()
        pairs = []
        for i in range(0, len(classement), 2):
            if i + 1 < len(classement):
                pairs.append((classement[i], classement[i + 1]))
        return pairs

    def get_classement(self):
        # Trier les joueurs en fonction de leur score (player[1] est le score)
        classement = sorted(
            self.players_inscrits, key=lambda player: player[1], reverse=True
        )

        print("\nClassement des joueurs :")
        for i, player in enumerate(classement, start=1):
            # player[0] est l'identifiant, player[1] est le score
            print(f"{i}. Joueur ID {player[0]} - Score: {player[1]}")
        return classement

    def start_tournament(self):
        if len(self.players_inscrits) != self.player_number:
            print(
                "Erreur, le nombre de joueurs inscrits ne permet pas de débuter le tournoi."
            )
        else:
            print("Début du tournoi")
            self.state = "en cours"
            random.shuffle(self.players_inscrits)
            round_instance = Round(int(self.round_actuel + 1))
            self.round_actuel += 1

            for i in range(0, len(self.players_inscrits), 2):
                if i + 1 < len(self.players_inscrits):
                    match = Match(
                        self.players_inscrits[i],
                        self.players_inscrits[i + 1],
                        round_number=1,
                        time="15",
                    )
                    round_instance.add_match(match)

            print("Round :", round_instance.tour)
            print("Number of matches :", len(round_instance.matches))

            self.rounds.append(round_instance)
            self.update()

            print(round_instance.show_matches())

    def save(self):
        try:
            # Charger les tournois existants s'il y en a
            with open(FILE_TOURNAMENT, "r") as f:
                try:
                    tournament_list = json.load(f)
                    if not isinstance(tournament_list, list):
                        tournament_list = []  # Corrige si ce n'est pas une liste
                except json.JSONDecodeError:
                    tournament_list = []  # Corrige si le fichier est vide ou invalide
        except FileNotFoundError:
            tournament_list = []  # Si le fichier n'existe pas, on crée une liste vide

        # Préparer les données du tournoi à sauvegarder
        tournament_data = {
            "id": str(self.id),
            "nom": self.nom,
            "lieu": self.lieu,
            "date_debut": self.date_debut.strftime("%d/%m/%Y"),
            "date_fin": self.date_fin.strftime("%d/%m/%Y"),
            "player_number": self.player_number,
            "status": self.state,
            "description": self.description,
            "round_total": self.round_number,
            "round_actuel": self.round_actuel,
            "joueurs_inscrits": self.players_inscrits,
            "rounds": [
                {
                    "tour": round_instance.tour,
                    "state": round_instance.state,
                    "matches": [
                        [
                            (match.player1_id, match.score1),
                            (match.player2_id, match.score2),
                        ]
                        for match in round_instance.matches
                    ],
                }
                for round_instance in self.rounds
            ],
        }

        # Ajouter le tournoi actuel à la liste
        tournament_list.append(tournament_data)

        # Sauvegarder la liste complète des tournois
        with open(FILE_TOURNAMENT, "w") as f:
            json.dump(tournament_list, f, indent=4)

    def update(self):
        try:
            list_tournois = (
                Tournois.load_json() or []
            )  # Charge la liste des tournois existants
        except (FileNotFoundError, json.JSONDecodeError):
            list_tournois = []

        nouveau_list_tournois = []
        tournoi_trouve = False

        for tournoi in list_tournois:
            if tournoi.nom == self.nom:  # Si c'est le tournoi à mettre à jour
                # Mettre à jour les informations du tournoi avec la version mise à jour
                nouveau_list_tournois.append(self)
                tournoi_trouve = True
            else:
                nouveau_list_tournois.append(tournoi)  # Garde les autres inchangés

        if not tournoi_trouve:  # Si le tournoi n'existe pas encore, on l'ajoute
            nouveau_list_tournois.append(self)

        # Convertir tous les objets datetime en chaîne de caractères avant de les sauvegarder
        list_to_save = []
        for tournoi in nouveau_list_tournois:
            tournoi_dict = (
                tournoi.to_dict()
            )  # On suppose que cette méthode convertit l'objet en dictionnaire
            # Conversion des dates en chaînes de caractères si ce n'est pas déjà fait
            tournoi_dict["date_debut"] = (
                tournoi_dict["date_debut"].strftime("%d/%m/%Y")
                if isinstance(tournoi_dict["date_debut"], datetime)
                else tournoi_dict["date_debut"]
            )
            tournoi_dict["date_fin"] = (
                tournoi_dict["date_fin"].strftime("%d/%m/%Y")
                if isinstance(tournoi_dict["date_fin"], datetime)
                else tournoi_dict["date_fin"]
            )

            list_to_save.append(tournoi_dict)

        # Sauvegarde des données mises à jour
        with open(FILE_TOURNAMENT, "w") as f:
            json.dump(list_to_save, f, indent=4)

    @staticmethod
    def load_json():
        with open(FILE_TOURNAMENT, "r") as f:
            tournament_data = json.load(f)
            tournament_list = []

            for data in tournament_data:

                data["date_debut"] = datetime.strptime(data["date_debut"], "%d/%m/%Y")
                data["date_fin"] = datetime.strptime(data["date_fin"], "%d/%m/%Y")

                p = Tournois(
                    data["nom"],
                    data["lieu"],
                    data["date_debut"],
                    data["date_fin"],
                    data["player_number"],
                    data["status"],
                    data["description"],
                    data["round_total"],
                    data["round_actuel"],
                )
                p.id = data["id"]

                # Chargement des joueurs inscrits
                p.players_inscrits = [
                    [
                        player[0],
                        player[1],
                    ]  # On garde le format de liste [identifiant, score]
                    for player in data["joueurs_inscrits"]
                ]

                # Chargement des rounds
                p.rounds = []
                for round_data in data["rounds"]:
                    round_instance = Round(round_data["tour"], round_data["state"])

                    # Chargement des matches
                    for match_data in round_data["matches"]:

                        if isinstance(match_data, list) and len(match_data) == 2:
                            player1 = match_data[0]  # Déjà sous forme [id, score]
                            player2 = match_data[1]  # Déjà sous forme [id, score]

                            match = Match(player1, player2, round_data["tour"], "15")
                            match.result = match_data  # [(id_joueur1, score1), (id_joueur2, score2)]
                            round_instance.add_match(match)
                        else:
                            print(
                                "Erreur : Format inattendu pour match_data :",
                                match_data,
                            )

                    p.rounds.append(round_instance)

                tournament_list.append(p)

        return tournament_list

