import json

class Player :
    def __init__(self, surname, name, date_of_birth, identifiant, score=0):
        self.surname = surname
        self.name = name
        self.date_of_birth = date_of_birth
        self.identifiant = identifiant
        self.score = score
        self.players = []

    def __str__(self):
        return f"Player : {self.name} {self.surname}, Birth : {self.date_of_birth}, ID : {self.identifiant}"

    def to_dict(self): # convertir un objet en dictionnaire
        return {
            "surname": self.surname,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "identifiant": self.identifiant,
            "score": self.score
        }

    def update_score(self, points):
        self.score += points

    @staticmethod
    def save_json():
        players_data = [player.to_dict() for player in players]
        with open("/Users/arnauddekertanguy/Documents/openclassrooms/Projets-Soutenance/Projet3-app_cavalier/cavalier_app/data/players.json", "w") as file:
            json.dump(players_data, file, indent=2)

    @staticmethod
    def load_json():
        with open("/Users/arnauddekertanguy/Documents/openclassrooms/Projets-Soutenance/Projet3-app_cavalier/cavalier_app/data/players.json", "r") as f:
            players_data = json.load(f)
            return [Player(**player_data) for player_data in players_data]




Player1 = Player("de Kertanguy", "Arnaud", "30/04/2000", 4352)
Player3 = Player("Lionel", "Messi", "24/02/1974", 2101)


players = Player.load_json()
players.append(Player3)

for player in players:
    Player.save_json()

