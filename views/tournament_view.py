from models.tournament import Tournois
from datetime import datetime
from utils.utils import Utilitaire


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
        while True:
            nom = input("Nom du tournoi : ").strip()
            if not nom:
                print("Veuillez entrer un nom de tournoi.")
            else:
                break

        while True:
            lieu = input("Lieu du tournoi :").strip()
            if not lieu:
                print("Veuillez entrer un lieu de tournoi.")
            else:
                break

        while True:
            date_debut = input("Date de début du tournoi (jj/mm/aaaa) : ")
            try:
                date_debut = datetime.strptime(date_debut, "%d/%m/%Y")
                break
            except ValueError:
                print("Veuillez entrer une date de début valide (jj/mm/aaaa).")

        while True:
            date_fin = input("Date de fin du tournoi (jj/mm/aaaa) : ")
            try:
                date_fin = datetime.strptime(date_fin, "%d/%m/%Y")
                if date_fin < date_debut:
                    print("Erreur, la date de fin doit être supérieur à celle de début")
                else:
                    break
            except ValueError:
                print("Veuillez entrer une date de fin valide (jj/mm/aaaa).")

        while True:
            try:
                player_number = int(
                    input("Nombre de joueurs pouvant y participer : ").strip()
                )
                if player_number < 4:
                    print("Le nombre de joueurs doit être au moins de 4.")
                else:
                    break
            except ValueError:
                print("Erreur : veuillez entrer un nombre valide.")

        while True:
            try:
                round_number = int(input("Nombre de rounds : ").strip())
                if round_number < 2:
                    print("Le nombre de round soit être supérieur à 1")
                else:
                    break
            except ValueError:
                print("Erreur, veuillez entrer un nombre valide.")

        description = input("Description du tournoi : ")
        new_tournament = Tournois(
            nom, lieu, date_debut, date_fin, player_number, round_number, description
        )
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
                    tournament.state = "Commencé"
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
            print(tournament.players_inscrits)
            print(tournament.show_players_inscrits())
            break
        else:
            print("Le tournois est complet.")

    def manage_score(self, tournament):

        for round_instance in tournament.rounds:
            if round_instance.state == "en attente":

                print(f"Modification des scores :")

                for match in round_instance.matches:
                    print(
                        f"{match.player1} vs {match.player2} - Résultat actuel: {match.result}"
                    )

                    while True:
                        new_result = input(
                            f"1: {match.player1} gagne, 2: {match.player2} gagne, 0: match nul) : "
                        )

                        if new_result == "1":
                            match.match_result(
                                match.player1, tournament.players_inscrits
                            )
                            break
                        elif new_result == "2":
                            match.match_result(
                                match.player2, tournament.players_inscrits
                            )
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
