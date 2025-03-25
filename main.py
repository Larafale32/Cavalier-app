
from controllers.controller_player import ControllerPlayer
from controllers.controller_tournament import ControllerTournament
from views.menu_view import ViewMenu
from views.player_view import ViewPlayer
from views.tournament_view import ViewTournament
from controllers.controller_menu import ControllerMenu
from controllers.controller_report import ControllerReport
from utils.utils import Utilitaire

class Application:
    def __init__(self):
        self.view_menu = ViewMenu()
        self.view_player = ViewPlayer()
        self.view_tournament = ViewTournament()

        self.controller_menu = ControllerMenu()
        self.controller_player = ControllerPlayer()
        self.controller_tournament = ControllerTournament()
        self.controller_report = ControllerReport()  # à ajouter dans le main.py pour l'appel à la fonction de génération du report.'

    def run(self):
        if self.controller_menu.authentification():
            while True:
                choice = self.view_menu.display_menu()

                if choice == "1":
                    Utilitaire.clear_screen()
                    self.controller_player.manage_players()
                elif choice == "2":
                    Utilitaire.clear_screen()
                    self.controller_tournament.change_tournaments()
                elif choice == "3":
                    Utilitaire.clear_screen()
                    self.controller_report.display_report()
                else:
                    Utilitaire.clear_screen()
                    print("Option inconnue")




App_main = Application()
App_main.run()

#rajouter des numéros pour les tournois
#générer le report avec le report, avoir le résultat stocké dans un fichier html