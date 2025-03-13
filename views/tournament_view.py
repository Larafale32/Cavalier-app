from models.tournament import Tournois

class ViewTournament:
    def show_tournaments(self):
        print("Liste des tournois :")
        count = 1
        tournaments = Tournois.load_json()
        for tournament in tournaments:
            print(f"{count}: --> {tournament.nom}")
            count += 1


    def create_tournament(self):
        print("Création d'un tournois")
        nom = input("Nom du tournoi : ")
        lieu = input("Lieu du tournoi :")
        date_debut = input("Date de début du tournoi (jj/mm/aaaa) : ")
        date_fin = input("Date de fin du tournoi (jj/mm/aaaa) : ")
        player_number = int(input("Nombre de joueurs pouvant y participer : "))
        round_number = int(input("Nombre de rounds : "))
        description = input("Description du tournoi : ")
        new_tournament = Tournois(nom, lieu, date_debut, date_fin, player_number, round_number, description)
        new_tournament.save()
        print("Tournois créé avec succès.")

    def delete_tournament(self):
        print("Suppression d'un tournois")
        tournament_name = input("Nom du tournoi à supprimer : ")
        for tournament in Tournois.load_json():
            if tournament.nom == tournament_name:
                Tournois.tournament_list.pop(tournament)
                Tournois.load_json().pop(tournament)
                print(f"Tournois {tournament_name} supprimé avec succès.")
                return
        print(f"Tournois {tournament_name} introuvable.")


    def tournament_choice(self):
        self.show_tournaments()  # Afficher la liste des tournois
        while True:
            try:
                # Demander à l'utilisateur de sélectionner un tournoi par son numéro
                selection = int(input("Sélectionner un tournoi (par son numéro) : "))
                tournaments = Tournois.load_json()

                # Vérifier si le numéro du tournoi sélectionné est valide
                if 1 <= selection <= len(tournaments):
                    selected_tournament = tournaments[selection - 1]
                    print(selected_tournament.nom)
                    return selected_tournament
                else:
                    print("Numéro de tournoi invalide, réessayez.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")


    def start_tournament(self, tournament):
        if int(tournament.round_actuel) == 0:
            while True:
                start = input("Voulez vous démarré le tournoi ? (OUI/NON)")
                if start.upper() == "OUI":
                    tournament.start_tournament()
                    break
                elif start.upper() == "NON":
                    break
                else:
                    print("Veuillez saisir 'OUI' ou 'NON'.")

        elif int(tournament.round_actuel) > 0:
            print("Le tournoi a déja commencé")

    def register_tournament(self, tournament, player_selected):
        while len(tournament.players_inscrits) < tournament.player_number:
            tournament.register_player(player_selected)
            print(tournament.show_players_inscrits())
            break
        else:
            print("Le tournois est complet.")

    def manage_score(self, tournament):

        for round_instance in tournament.rounds:
            if round_instance.state == "en attente":

                print(f"Modification des scores :")

                for match in round_instance.matches:
                    print(f"{match.player1} vs {match.player2} - Résultat actuel: {match.result}")

                    while True:
                        new_result = input(
                            f"1: {match.player1} gagne, 2: {match.player2} gagne, 0: match nul) : ")


                        if new_result == "1":
                            match.match_result(match.player1, tournament.players_inscrits)
                            break
                        elif new_result == "2":
                            match.match_result(match.player2, tournament.players_inscrits)
                            break
                        elif new_result == "0":
                            match.match_result(None, tournament.players_inscrits)
                            break
                        else:
                            print("Entrée invalide, aucun changement appliqué.")

                tournament.update()
                print("Scores mis à jour avec succès.")

                # Vérifier si tous les matchs ont un résultat pour avancer au round suivant
                if all(match.result is not None for match in round_instance.matches):
                    tournament.advance_to_next_round()

                break














