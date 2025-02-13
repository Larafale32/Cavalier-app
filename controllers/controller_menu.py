from views.tournament_view import ViewTournament
from views.player_view import ViewPlayer
from views.menu_view import ViewMenu
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






