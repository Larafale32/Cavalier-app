from views.report_view import ViewReport
from views.menu_view import ViewMenu
from controllers.controller_tournament import ControllerTournament

class ControllerReport:
    def __init__(self):
        self.view_report = ViewReport()
        self.view_menu = ViewMenu()
        self.controller_tournament = ControllerTournament()

    def display_report(self):
        while True:
            choice = self.view_menu.report_menu()
            if choice == "1":
                self.view_report.list_all_players()
            elif choice == "2":
                self.view_report.list_all_tournaments()
            elif choice == "3":
                tournament_choice = self.controller_tournament.return_tounraments()
                self.view_report.tournament_details(tournament_choice)
            elif choice == "4":
                tournament_choice = self.controller_tournament.return_tounraments()
                self.view_report.list_rounds_and_matches(tournament_choice)
            elif choice == "0":
                print("Retour au menu principal.")
                break
            else :
                print("Entrée invalide, réessayez.")

