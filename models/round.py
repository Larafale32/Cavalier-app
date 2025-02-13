
class Round:

    def __init__(self, tour):
        self.tour = tour
        self.state = "En attente"
        self.matches = []


    def add_match(self, match):
        self.matches.append(match)

    def start_round(self):
        self.state = "En cours"

    def round_finish(self):
        self.state = "Terminé"


    def show_matches(self):
        return f"Round {self.tour} :" + "\n".join(str(match) for match in self.matches)

    def results_matches(self):
        for match in self.matches:
            result = input("Qui à gagné ? : (1,2 ou draw")
            if result == "1":
                match.result = match.player1.identifiant
                match.match_result()

            if result == "2":
                match.result = match.player2.identifiant
                match.match_result()

            if result == "draw":
                match.result = None
                match.match_result()

            else:
                print("Entrée invalide, veuillez entrer '1', '2' ou 'draw'.")

        return f"Résultats du round {self.tour} :" + "\n".join(str(match) for match in self.matches)

Round1 = Round(1)
Round1.show_matches()
