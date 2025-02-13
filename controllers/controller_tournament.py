from views.tournament_view import ViewTournament
from models.tournament import Tournois

class ControllerTournament:
    def __init__(self):
        self.view_tournament = ViewTournament()
        self.current_tournament = None

    def change_tournaments(self):
        while True:
            choice = self.view_tournament.change_tournaments()
            if choice == "1":
                self.view_tournament.create_tournament()
            elif choice == "2":
                self.view_tournament.delete_tournament()
            elif choice == "3":
                tournament_name = self.view_tournament.tournament_choice()
                if tournament_name:
                    for tournament in Tournois.load_json():
                        if tournament.nom == tournament_name:
                            self.current_tournament = tournament
                            print(f"Vous gérez maintenant le tournois {tournament_name}")
                            self.manage_tournaments()
                            break

                else:
                    print("Tournois introuvable")
            elif choice == "4":
                self.view_tournament.show_tournaments()
            else:
                print("Veuillez entrer un choix valide (1,2,3 ou 4)")

    def manage_tournaments(self):
        if not self.current_tournament:
            print("Aucun tournoi sélectionné.")
            return

        while True:
            choice = self.view_tournament.manage_tournaments()
            if choice == "1":
                self.view_tournament.start_tournament(self.current_tournament)
            elif choice == "2":
                self.view_tournament.register_tournament(self.current_tournament)
            elif choice == "4":
                break
            else:
                print("Veuillez entrer un choix valide (1 ou 2)")




#gestion des joueurs / gestion des tournois => mettre à jour les scores / report = stat joueurs et tournois