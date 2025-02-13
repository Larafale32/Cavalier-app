from views.player_view import ViewPlayer
from views.menu_view import ViewMenu

class ControllerPlayer:
    def __init__(self):
        self.view_player = ViewPlayer()
        self.view_menu = ViewMenu()

    def show_players(self):
        self.view_player.show_players()

    def add_player(self):
        self.view_player.add_player()

    def delete_player(self):
        self.view_player.delete_player()

    def update_player(self):
        self.view_player.update_player_score()

    def manage_players(self):
        while True:
            choice = self.view_menu.manage_players()
            if choice == "1":
                self.add_player()
            elif choice == "2":
                self.delete_player()
            elif choice == "3":
                self.view_player.show_players()
            elif choice == "4":
                break
            else:
                print("Choix invalide, réessayez.")




