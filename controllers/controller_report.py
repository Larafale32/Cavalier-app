from views.report_view import ViewReport
from views.menu_view import ViewMenu
from controllers.controller_tournament import ControllerTournament
from utils.utils import Utilitaire


class ControllerReport:
    def __init__(self):
        self.view_report = ViewReport()
        self.view_menu = ViewMenu()
        self.controller_tournament = ControllerTournament()
        self.utilitaire = Utilitaire()

    def display_report(self):
        while True:
            choice = self.view_menu.report_menu()
            if choice == "1":
                self.utilitaire.clear_screen()  # !!
                self.view_report.list_all_players()
            elif choice == "2":
                self.utilitaire.clear_screen()  # !!
                self.view_report.list_all_tournaments()
            elif choice == "3":
                self.utilitaire.clear_screen()  # !!
                tournament_choice = self.controller_tournament.return_tounraments()
                self.view_report.tournament_details(tournament_choice)
            elif choice == "4":
                self.utilitaire.clear_screen()  # !!
                tournament_choice = self.controller_tournament.return_tounraments()
                self.view_report.list_rounds_and_matches(tournament_choice)
            elif choice == "0":
                self.utilitaire.clear_screen()  # !!
                print("Retour au menu principal.")
                break
            else:
                print("Entrée invalide, réessayez.")
