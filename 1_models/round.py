from player import Player
from match import Match
from match import Match1, Matche_R1
import json


class Round:
    def __init__(self, tour, state):
        self.tour = tour
        self.state = state
        self.matches = []


    def add_match(self, match):
        self.matches.append(match)

    def start_round(self):
        self.state = "En cours"

    def round_finish(self):
        self.state = "Terminé"
        self.matches = [match.to_dict() for match in self.matches]

    def show_matches(self):
        return f"Round {self.tour} :" + "\n".join(str(match) for match in self.matches)

    @staticmethod
    def save_json(matches):
        round_data = [match.to_dict() for match in matches]
        with open("/Users/arnauddekertanguy/Documents/openclassrooms/Projets-Soutenance/Projet3-app_cavalier/cavalier_app/data/tournaments.json", "w") as f:
            json.dump(round_data, f, indent=4)



Round1 = Round(1, "en attente")
Round1.add_match(Match1)
print(Round1.show_matches())

Round1.save_json(Matche_R1)