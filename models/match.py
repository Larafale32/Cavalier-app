
from utils.constante import FILE_PLAYER

class Match:
    match_list = []

    def __init__(self, player1, player2, round_number, time, result=None):
        self.player1 = player1
        self.player2 = player2
        self.round_number = round_number
        self.time = time
        self.result = result

    def __str__(self):
        return f"Match : {self.player1.name}  {self.player1.surname} vs {self.player2.name} {self.player2.surname}\n{self.result}"

    def match_result(self):
        if self.result == self.player1.identifiant:
            self.player1.update_score(1)
            return "win_p1"

        elif self.result == self.player2.identifiant:
            self.player2.update_score(1)
            return "win_p2"

        elif self.result is None:
            self.player1.update_score(0.5)
            self.player2.update_score(0.5)
            return "draw"

    def to_dict(self):
        return {
            "player1": self.player1.name,
            "player2": self.player2.name,
            "round_number": self.round_number,
            "time": self.time,
            "result": str(self.result)
        }


print(Match.match_list)
