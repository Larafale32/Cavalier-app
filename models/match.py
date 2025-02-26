
from utils.constante import FILE_PLAYER

class Match:
    match_list = []

    def __init__(self, player1, player2, round_number, time, result=None):
        self.player1 = player1
        self.player2 = player2
        self.round_number = round_number
        self.time = time
        self.result = result if result else [(player1, 0), (player2, 0)]

    def __str__(self):
        return f"Match : {self.player1['identifiant']} vs {self.player2['identifiant']} | Résultat : {self.result}"

    def match_result(self, winner, players_inscrits):
        if winner == self.player1:
            self.result = [(self.player1, 1), (self.player2, 0)]
            self.player1["score"] += 1
        elif winner == self.player2:
            self.result = [(self.player1, 0), (self.player2, 1)]
            self.player2["score"] += 1
        else:
            self.result = [(self.player1, 0.5), (self.player2, 0.5)]
            self.player1["score"] += 0.5
            self.player2["score"] += 0.5

        for player in players_inscrits:
            if player["identifiant"] == self.player1["identifiant"]:
                player["score"] = self.player1["score"]
            elif player["identifiant"] == self.player2["identifiant"]:
                player["score"] = self.player2["score"]

    def to_dict(self):
        return {
            "players": self.result  # [(id_joueur1, score1), (id_joueur2, score2)]
        }

print(Match.match_list)
