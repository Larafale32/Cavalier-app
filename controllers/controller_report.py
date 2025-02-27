from views.report_view import ViewReport
from views.menu_view import ViewMenu

class ControllerReport:
    def __init__(self):
        self.view_report = ViewReport()
        self.view_menu = ViewMenu()

    def display_report(self):
        while True:
            choice = self.view_menu.report_menu()
            if choice == "1":
                self.view_report.list_all_players()
            elif choice == "2":
                self.view_report.list_all_tournaments()
            elif choice == "3":
                self.view_report.tournament_details()
            elif choice == "4":
                self.view_report.list_rounds_and_matches()
            elif choice == "0":
                print("Retour au menu principal.")
                break
            else :
                print("Entrée invalide, réessayez.")

