
from utils.constante import FILE_PLAYER

class Match:
    match_list = []

    def __init__(self, player1, player2, round_number, time, result=None):
        self.player1 = player1
        self.player2 = player2
        self.round_number = round_number
        self.time = time
        self.result = result if result else [[player1, 0], [player2, 0]]

    def __str__(self):
        return f"Match : {self.player1[0]} vs {self.player2[0]} | Résultat : {self.result}"

    def match_result(self, winner, players_inscrits):

        # Récupérer les identifiants des joueurs
        player1_id = self.player1[0]  # self.player1 est une liste [identifiant, score]
        player2_id = self.player2[0]

        # Déterminer les scores en fonction du gagnant
        if winner == self.player1:
            self.result = [(player1_id, 1), (player2_id, 0)]
            score_p1, score_p2 = 1, 0
        elif winner == self.player2:
            self.result = [(player1_id, 0), (player2_id, 1)]
            score_p1, score_p2 = 0, 1
        else:  # Match nul
            self.result = [(player1_id, 0.5), (player2_id, 0.5)]
            score_p1, score_p2 = 0.5, 0.5

        # Mettre à jour les scores des joueurs dans players_inscrits
        for player in players_inscrits:
            if player[0] == player1_id:
                player[1] += score_p1  # Ajouter le score au joueur 1
            elif player[0] == player2_id:
                player[1] += score_p2  # Ajouter le score au joueur 2

    def to_dict(self):
        return [[player if isinstance(player, int) else player[0], score] for player, score in self.result]


print(Match.match_list)
