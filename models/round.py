class Round:

    def __init__(self, tour, state="en attente"):
        self.tour = tour
        self.state = state
        self.matches = []

    def to_dict(self):
        return {
            "tour": self.tour,
            "state": self.state,
            "matches": [match.to_dict() for match in self.matches],
        }

    def add_match(self, match):
        self.matches.append(match)

    def start_round(self):
        self.state = "En cours"

    def round_finish(self):
        self.state = "Terminé"

    def show_matches(self):
        return f"Round {self.tour} :" + "\n".join(str(match) for match in self.matches)

    def results_matches(self, results):
        """Met à jour les résultats des matchs à partir d'une liste de résultats."""
        for match, result in zip(self.matches, results):
            if result == "1":
                match.result = match.player1.identifiant
            elif result == "2":
                match.result = match.player2.identifiant
            elif result == "draw":
                match.result = None
            match.match_result()  # Met à jour le score des joueurs
