from views.tournament_view import ViewTournament
from views.player_view import ViewPlayer
from views.menu_view import ViewMenu
from views.report_view import ViewReport
from models.player import Player


class ControllerMenu:
    def __init__(self):
        self.view_menu = ViewMenu()
        self.admin_list = []
        self.admin_online = None

    def authentification(self):
        while self.admin_online is None:
            admin = self.view_menu.authentification(self.admin_list)
            if admin:
                self.admin_online = admin
                print(f"{admin.name} est connecté")
                return True
            else:
                print("Échec authentification, réessayez")

    def display_menu(self):
        return self.view_menu.display_menu()

    # def display_report(self):
    #     choice = self.view_menu.report_menu()
    #     if choice == "1":
    #         view_report.list_all_players()
    #     elif choice == "2":
    #         report.list_all_tournaments()
    #     elif choice == "3":
    #         name = input("Nom du tournoi : ")
    #         tournament = tournament_manager.get_tournament_by_name(name)
    #         if tournament:
    #             report.tournament_details(tournament)
    #         else:
    #             print("Tournoi introuvable.")
    #     elif choice == "4":
    #         name = input("Nom du tournoi : ")
    #         tournament = tournament_manager.get_tournament_by_name(name)
    #         if tournament:
    #             report.list_rounds_and_matches(tournament)
    #         else:
    #             print("Tournoi introuvable.")
    #     elif choice == "5":
    #         print("Retour au menu principal.")
    #         break
    #     else:
    #         print("Entrée invalide, réessayez.")




