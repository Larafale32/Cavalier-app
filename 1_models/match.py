from player import Player

class Match:
    def __init__(self, player1, player2, round_number, time):
        self.player1 = player1
        self.player2 = player2
        self.round_number = round_number
        self.time = time
        self.result = " "

    def __str__(self):
        return f"Match : {self.player1.name}  {self.player1.surname} vs {self.player2.name} {self.player2.surname}\n{self.result}"

    def match_result(self):
        if self.result == self.player1:
            self.player1.update_score(1)
            return "win_p1"

        elif self.result == self.player2:
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


Player1 = Player("de Kertanguy", "Arnaud", "30/04/2000", 4352)
Player2 = Player("Dafoe", "James", "24/02/1988", 9801)


Match1 = Match(Player1, Player2, 1, "10:00")
Match1.result = None
Matche_R1 = [Match1]
# Match1.result = Player1
# Match1.match_result()
# print(Match1)
# print(Player1.score)
#
# Match1.result = Player2
# Match1.match_result()
# print(Match1)
# print(Player2.score)
#
# Match1.result = None
# Match1.match_result()
# print(Match1)
# print(Player2.score)
# print(Player1.score)

