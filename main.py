from controllers.controller_player import ControllerPlayer
from controllers.controller_tournament import ControllerTournament
from views.menu_view import ViewMenu
from views.player_view import ViewPlayer
from views.tournament_view import ViewTournament
from controllers.controller_menu import ControllerMenu

class Application:
    def __init__(self):
        self.view_menu = ViewMenu()
        self.view_player = ViewPlayer()
        self.view_tournament = ViewTournament()

        self.controller_menu = ControllerMenu()
        self.controller_player = ControllerPlayer()
        self.controller_tournament = ControllerTournament()

    def run(self):
        if self.controller_menu.authentification():
            while True:
                choice = self.view_menu.display_menu()
                if choice == "1":
                    self.controller_player.manage_players()
                if choice == "2":
                    self.controller_tournament.change_tournaments()

                else:
                    print("Option inconnue")

App_main = Application()
App_main.run()

#rajouter des numéros pour les tournois
#générer le report avec le report, avoir le résultat stocké dans un fichier html