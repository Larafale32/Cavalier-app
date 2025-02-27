from views.tournament_view import ViewTournament
from views.menu_view import ViewMenu
from views.player_view import ViewPlayer

class ControllerTournament:
    def __init__(self):
        self.view_tournament = ViewTournament()
        self.view_menu = ViewMenu()
        self.view_player = ViewPlayer()
        self.current_tournament = None

    def change_tournaments(self):
        while True:
            choice = self.view_menu.change_tournaments()
            if choice == "1":
                self.view_tournament.create_tournament()
            elif choice == "2":
                self.view_tournament.delete_tournament()
            elif choice == "3":
                selected_tournament = self.view_tournament.tournament_choice()
                if selected_tournament:
                    self.current_tournament = selected_tournament
                    print(f"Vous gérez maintenant le tournoi {selected_tournament.nom}")
                    self.manage_tournaments()
                    break

                else:
                    print("Tournois introuvable")
            elif choice == "4":
                self.view_tournament.show_tournaments()
            elif choice == "0":
                break
            else:
                print("Veuillez entrer un choix valide (1,2,3 ou 4)")

    def manage_tournaments(self):
        if not self.current_tournament:
            print("Aucun tournoi sélectionné.")
            return

        while True:
            choice = self.view_menu.manage_tournaments()
            if choice == "1":
                self.view_tournament.start_tournament(self.current_tournament)
            elif choice == "2":
                player_selected = self.view_player.choose_players()
                self.view_tournament.register_tournament(self.current_tournament, player_selected)
            elif choice == "3":
                self.view_tournament.manage_score(self.current_tournament)
            elif choice == "0":
                break
            else:
                print("Veuillez entrer un choix valide (1 ou 2)")




#gestion des joueurs / gestion des tournois => mettre à jour les scores / report = stat joueurs et tournois