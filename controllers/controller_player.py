from views.player_view import ViewPlayer
from views.menu_view import ViewMenu
from utils.utils import Utilitaire


class ControllerPlayer:
    def __init__(self):
        self.view_player = ViewPlayer()
        self.view_menu = ViewMenu()
        self.utilitaire = Utilitaire()

    def manage_players(self):
        while True:
            choice = self.view_menu.manage_players()
            if choice == "1":
                self.utilitaire.clear_screen()  # !!
                self.view_player.add_player()
            elif choice == "2":
                self.utilitaire.clear_screen()  # !!
                self.view_player.delete_player()
            elif choice == "3":
                self.utilitaire.clear_screen()  # !!
                self.change_info_player()
            elif choice == "4":
                self.utilitaire.clear_screen()  # !!
                self.view_player.show_players()
            elif choice == "0":
                self.utilitaire.clear_screen()
                break
            else:
                self.view_menu.entree_invalide()

    def change_info_player(self):
        player = self.view_player.choose_players()  # Sélection du joueur
        while True:
            choice = self.view_menu.change_info_player()  # Menu
            if choice == "1":
                self.view_player.change_surname(player)
            elif choice == "2":
                self.view_player.change_name(player)
            elif choice == "3":
                self.view_player.change_date_of_birth(player)
            elif choice == "4":
                self.view_player.change_identifiant(player)
            elif choice == "5":
                self.view_player.change_score(player)
            elif choice == "0":
                break  # Quitter la boucle
            else:
                self.view_menu.entree_invalide()
