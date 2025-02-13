from models.tournament import Tournois
from models.player import Player
from models.admin import Administrator

class ViewMenu:
    def authentification(self, admin_list):
        validation_id = int(input("Entrer votre code administrateur : "))
        for admin in Administrator.load_json():
            if admin.id == int(validation_id) :
                print("Authentification réussite,vous êtes connecté \nBienvenu " + admin.name)
                return admin

            else:
                print("Échec authentification, code administrateur non reconnu")
                return False


    def display_menu(self):
        print("Veuillez sélectionner une action (1,2,3 ou 4)"
              "\n1) Gestion des joueurs"
              "\n2) Gestion des tournois"
              "\n3) Report (stat : joueurs/tournois)"
              "\n4) Quitter")
        return input("Votre choix : ")

    def manage_players(self):
        print("Gestion des joueurs, sélectionnez une action : (1,2,3 ou 4)")
        print("1) Ajouter un joueur"
              "\n2) Supprimer un joueur"
              "\n3) Afficher la liste des joueurs"
              "\n4) Quitter")
        choice = input("Votre choix : ")
        return choice








