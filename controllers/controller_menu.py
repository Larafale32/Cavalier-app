from views.menu_view import ViewMenu
from models.admin import Administrator


class ControllerMenu:
    def __init__(self):
        self.view_menu = ViewMenu()
        self.admin = Administrator
        self.admin_list = []


    def authentification(self):
        admin_list = self.admin.load_json()
        while True:
            if not self.view_menu.authentification(admin_list):
                continue
            else:
                break
        return True


    def display_menu(self):
        return self.view_menu.display_menu()
