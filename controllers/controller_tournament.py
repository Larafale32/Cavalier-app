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
                self.utilitaire.clear_screen()  # !!
                self.view_tournament.create_tournament()
            elif choice == "2":
                self.utilitaire.clear_screen()  # !!
                self.view_tournament.delete_tournament()
            elif choice == "3":
                self.utilitaire.clear_screen()  # !!
                selected_tournament = self.return_tounraments()
                if selected_tournament:
                    self.current_tournament = selected_tournament
                    self.view_tournament.show_selected_tournament(selected_tournament)
                    self.manage_tournaments()
                    break

                else:
                    self.view_menu.entree_invalide()
            elif choice == "4":
                self.utilitaire.clear_screen()  # !!
                self.view_tournament.show_tournaments()
            elif choice == "0":
                self.utilitaire.clear_screen()  # !!
                break
            else:
                self.view_menu.entree_invalide()

    def manage_tournaments(self):
        if not self.current_tournament:
            return

        while True:
            choice = self.view_menu.manage_tournaments()
            if choice == "1":
                self.utilitaire.clear_screen()
                self.view_tournament.start_tournament(self.current_tournament)
            elif choice == "2":
                self.utilitaire.clear_screen()
                while (
                    len(self.current_tournament.players_inscrits)
                    < self.current_tournament.player_number
                ):
                    player_selected = (
                        self.view_player.choose_players()
                    )

                    if player_selected.identifiant == "0":
                        break

                    self.view_tournament.register_tournament(
                        self.current_tournament, player_selected
                    )  # Passe le joueur sélectionné

            elif choice == "3":
                self.utilitaire.clear_screen()
                if not self.current_tournament.advance_to_next_round:
                    self.view_tournament.end_tournament()
                else:
                    self.view_tournament.manage_score(self.current_tournament)
            elif choice == "0":
                self.utilitaire.clear_screen()
                break
            else:
                self.view_menu.entree_invalide()

    def return_tounraments(self):
        return self.view_tournament.tournament_choice()
