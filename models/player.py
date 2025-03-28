import json
import uuid
from utils.constante import FILE_PLAYER


class Player:

    def __init__(self, surname, name, date_of_birth, identifiant=None, score=0):
        self.surname = surname
        self.name = name
        self.date_of_birth = date_of_birth
        self.identifiant = identifiant
        self.score = score
        self.id = uuid.uuid4()

    def __str__(self):
        return (
            f"Player : {self.name} {self.surname}, Birth : {self.date_of_birth}, ID : {self.identifiant}, "
            f"Score : {self.score}"
        )

    def to_dict(self):  # convertir un objet en dictionnaire
        return {
            "surname": self.surname,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "identifiant": self.identifiant,
            "score": self.score,
            "id": str(self.id),
        }

    @staticmethod
    def get_player_by_id(player_id, all_players):
        """Récupère un objet Player à partir de son identifiant."""
        for player in all_players:
            if player.identifiant == player_id:
                return player
        return None

    def update_score(self, points):
        self.score += points

    def save(self):
        list_player = Player.load_json()
        list_player.append(self)
        players_data = [player.to_dict() for player in list_player]
        with open(FILE_PLAYER, "w") as file:
            json.dump(players_data, file, indent=4)

    def update(self):
        try:
            players_list = (
                self.load_json() or []
            )  # Charge la liste des tournois existants
        except (FileNotFoundError, json.JSONDecodeError):
            players_list = []

        new_players_list = []
        player_found = False

        for player in players_list:
            if (
                player.identifiant == self.identifiant
            ):  # Si c'est le tournoi à mettre à jour
                new_players_list.append(self)  # Ajoute la version mise à jour
                player_found = True
            else:
                new_players_list.append(player)  # Garde les autres inchangés

        if not player_found:  # Si le tournoi n'existe pas encore, on l'ajoute
            new_players_list.append(self)

        # Sauvegarde des données mises à jour
        with open(FILE_PLAYER, "w") as f:
            json.dump([p.to_dict() for p in new_players_list], f, indent=4)

    @staticmethod
    def load_json():
        with open(FILE_PLAYER, "r") as file:
            players_data = json.load(file)
            list = []
            for player_data in players_data:
                p = Player(
                    player_data["surname"],
                    player_data["name"],
                    player_data["date_of_birth"],
                    (
                        player_data["identifiant"]
                        if player_data["identifiant"] is not None
                        else None
                    ),
                    player_data["score"],
                )
                p.id = player_data["id"]
                list.append(p)
            return list
