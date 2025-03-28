from models.admin import Administrator


class ViewMenu:
    def authentification(self, admin_list):
        validation_id = int(input("Entrer votre code administrateur : "))
        for admin in Administrator.load_json():
            if admin.id == int(validation_id):
                print(
                    "Authentification réussite,vous êtes connecté \nBienvenu "
                    + admin.name
                )
                return admin

            else:
                print("Échec authentification, code administrateur non reconnu")
                return False

    def display_menu(self):
        print(
            "Veuillez sélectionner une action (1,2,3 ou 4)"
            "\n1) Gestion des joueurs"
            "\n2) Gestion des tournois"
            "\n3) Report (stat : joueurs/tournois)"
            "\n4) Quitter"
        )
        return input("Votre choix : ")

    def manage_players(self):
        print("Gestion des joueurs, sélectionnez une action : (1,2,3 ou 4)")
        print(
            "1) Ajouter un joueur"
            "\n2) Supprimer un joueur"
            "\n3) Modifier les informations d'un joueur"
            "\n4) Afficher la liste des joueurs"
            "\n0) Quitter"
        )
        choice = input("Votre choix : ")
        return choice

    def change_tournaments(self):
        print("Gestion des tournois, sélectionnez une action : (1,2,3 ou 4)")
        print(
            "1) Ajouter un tournoi"
            "\n2) Supprimer un tournoi"
            "\n3) Manager les tournois"
            "\n4) Afficher la liste des tournois"
            "\n0) Retour au menu principal"
        )
        choice = input("Votre choix : ")
        return choice

    def manage_tournaments(self):
        while True:
            print("Quelle action voulez vous effectuer ? : (1,2,3 ou 4) ")
            print(
                "1) Démarrer le tournoi"
                "\n2) Inscrire des joueurs au tournoi"
                "\n3) Afficher/modifier les scores"
                "\n0) Retour"
            )
            choice = input("Votre choix : ")
            return choice

    def change_info_player(self):
        print(
            "1) Modifier le nom"
            "\n2) Modifier le prénom"
            "\n3) Modifier la date de naissance"
            "\n4) Modifier l'identifiant"
            "\n5) Modifier le score"
            "\n0) Quitter"
        )
        choice = input("Votre choix (entrer son numéro) :")
        return choice

    def report_menu(self):
        print("\nMenu Rapports :")
        print("1) Liste de tous les joueurs (ordre alphabétique)")
        print("2) Liste de tous les tournois")
        print("3) Détails d'un tournoi")
        print("4) Rounds et matchs d'un tournoi")
        print("0) Quitter")

        return input("Choisissez une option (numéro) : ")
