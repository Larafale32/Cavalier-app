from models.tournament import Tournois
from models.player import Player
from models.tournament import Tournois_Toulouse, Tournois_Lyon
class ViewTournament:
    def show_tournaments(self):
        print("Liste des tournois :")
        for tournament in Tournois.load_json():
            print(tournament.nom)

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


    def change_tournaments(self):
        print("Gestion des tournois, sélectionnez une action : (1,2,3 ou 4)")
        print("1) Ajouter un tournoi"
              "\n2) Supprimer un tournoi"
              "\n3) Manager les tournois"
              "\n4) Afficher la liste des tournois"
              "\n5) Quitter")
        choice = input("Votre choix : ")
        return choice

    def tournament_choice(self):
        self.show_tournaments()
        while True:
            print("Sélectionner un tournois : (entrer son nom)")
            selection = input("Votre choix : ")
            selection_found = False
            for tournament in Tournois.load_json():
                if tournament.nom == selection:
                    selection_found = True
                    return selection

            if not selection_found:
                print("Tournoi introuvable")
                return None


    def manage_tournaments(self):
        while True:
            print("Quelle action voulez vous effectuer ? : (1,2,3 ou 4) ")
            print("1) Démarrer le tournoi"
                  "\n2) Inscrire des joueurs au tournoi"
                  "\n3) Afficher/modifier les scores"
                  "\n4) Retour")
            choice = input("Votre choix : ")
            return choice


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

    def register_tournament(self, tournament):
        print(tournament.player_number)
        while len(tournament.players_inscrits) < int(tournament.player_number):
            print(tournament.show_players_inscrits())
            print("Incrire des joueurs au tournoi : (entrer leurs id)")
            joueur_id = input("ID du joueur : ")
            tournament.register_player(joueur_id)
            tournament.show_players_inscrits()
            break
        else:
            print("Le tournois est complet.")


    def manage_score(self, tournament):
        print(tournament.rounds)
        pass








