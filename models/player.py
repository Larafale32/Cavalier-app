import json
import random
import uuid
from utils.constante import FILE_PLAYER
# générer un id aléatoire unique pour chaque player
class Player :

    def __init__(self, surname, name, date_of_birth, identifiant=None, score=0):
        self.surname = surname
        self.name = name
        self.date_of_birth = date_of_birth
        self.identifiant = identifiant
        self.score = score
        self.id = uuid.uuid4()



    def __str__(self):
        return f"Player : {self.name} {self.surname}, Birth : {self.date_of_birth}, ID : {self.identifiant}"


    def to_dict(self): # convertir un objet en dictionnaire
        return {
            "surname": self.surname,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "identifiant": self.identifiant,
            "score": self.score,
            "id": str(self.id)
     }


    def update_score(self, points):
        self.score += points

    def save(self):
        list_player = Player.load_json()
        list_player.append(self)
        players_data = [player.to_dict() for player in list_player]
        with open(FILE_PLAYER, "w") as file:
            json.dump(players_data, file, indent=4)

    @staticmethod
    def load_json():
            with open(FILE_PLAYER, "r") as file:
                players_data = json.load(file)
                list = []
                for player_data in players_data:
                    p = Player(player_data["surname"], player_data["name"], player_data["date_of_birth"], player_data["identifiant"], player_data["score"])
                    p.id = player_data["id"]
                    list.append(p)
                return list



players_list = Player.load_json()


# Player("de Kertanguy", "Arnaud", "30/04/2000", 2451).save()
# Player("Lionel", "Messi", "24/02/1974", 7865).save()
# P3 = Player("Federer", "Roger", "08/08/1981", 9876)
# P3.save()
# Player("Nadal", "Rafael", "03/06/1986", 8045).save()
# Player("Djokovic", "Novak", "22/05/1987", 4521).save()
# Player("Murray", "Andy", "15/05/1987", 1782).save()
# Player("Williams", "Serena", "26/09/1981",2001).save()
# Player("Borg", "Bjorn", "06/06/1956", 9812).save()
#

