from views.tournament_view import ViewTournament
from views.menu_view import ViewMenu
from views.player_view import ViewPlayer
from utils.utils import Utilitaire

class ControllerTournament:
    def __init__(self):
        self.view_tournament = ViewTournament()
        self.view_menu = ViewMenu()
        self.view_player = ViewPlayer()
        self.utilitaire = Utilitaire()
        self.current_tournament = None

    def change_tournaments(self):
        while True:
            choice = self.view_menu.change_tournaments()
            if choice == "1":
                self.utilitaire.clear_screen()# !!
                self.view_tournament.create_tournament()
            elif choice == "2":
                self.utilitaire.clear_screen()# !!
                self.view_tournament.delete_tournament()
            elif choice == "3":
                self.utilitaire.clear_screen()# !!
                selected_tournament = self.return_tounraments()
                if selected_tournament:
                    self.current_tournament = selected_tournament
                    print(f"Vous gérez maintenant le tournoi {selected_tournament.nom}")
                    self.manage_tournaments()
                    break

                else:
                    print("Tournois introuvable")
            elif choice == "4":
                self.utilitaire.clear_screen()# !!
                self.view_tournament.show_tournaments()
            elif choice == "0":
                self.utilitaire.clear_screen()# !!
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
                while len(self.current_tournament.players_inscrits) < self.current_tournament.player_number:
                    print("\nSélectionnez un joueur à inscrire (ou entrez 0 pour arrêter) :")
                    player_selected = self.view_player.choose_players()  # Sélection AVANT l'inscription

                    if player_selected.identifiant == "0":
                        print("Arrêt de l'inscription des joueurs.")
                        break

                    self.view_tournament.register_tournament(self.current_tournament,
                                                             player_selected)  # Passe le joueur sélectionné

            elif choice == "3":
                if not self.current_tournament.advance_to_next_round:
                    print("Tous les rounds sont terminés, le tournoi est terminé")

                else:
                    self.view_tournament.manage_score(self.current_tournament)
            elif choice == "0":
                break
            else:
                print("Veuillez entrer un choix valide (1 ou 2)")

    def return_tounraments(self):
        return self.view_tournament.tournament_choice()

#gestion des joueurs / gestion des tournois => mettre à jour les scores / report = stat joueurs et tournois