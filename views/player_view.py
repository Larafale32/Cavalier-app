import json
from utils.constante import FILE_PLAYER
from models.player import Player, players_list

class ViewPlayer:
    def show_players(self):
        players = Player.load_json()
        print("Liste des joueurs : ")
        count = 1
        for player in players:
            print(f"{count}: --> {player}")
            count += 1

    def choose_players(self):
        self.show_players()
        players = Player.load_json()
        while True:
            try:
                index = int(input("Choisi un joueur (par son numéro): "))
                real_index = index - 1
                if 0 <= real_index < len(players):  # Vérification que l'index est valide
                    return players[real_index]
                else:
                    print("Numéro invalide, réessayez.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier.")

    def change_surname(self, player):
        player.surname = input(f"Nouveau nom pour {player.name} {player.surname}: ")
        player.update()
        print("Nom mis à jour avec succès.")

    def change_name(self, player):
        player.name = input(f"Nouveau prénom pour {player.name} {player.surname}: ")
        player.update()
        print("Prénom mis à jour avec succès.")

    def change_date_of_birth(self, player):
        player.date_of_birth = input(f"Nouvelle date de naissance pour {player.name} {player.surname} (JJ/MM/YYYY): ")
        player.update()
        print("Date de naissance mise à jour avec succès.")

    def change_identifiant(self, player):
        player.identifiant = input(f"Nouvel identifiant pour {player.name} {player.surname}: ")
        player.update()
        print("Identifiant mis à jour avec succès.")

    def change_score(self, player):
        player.score = int(input(f"Nouveau score pour {player.name} {player.surname}: "))
        player.update()
        print("Score mis à jour avec succès.")


    def delete_player(self):
        identifiant = input("Entrez l'identifiant du joueur à supprimer : ")
        print(players_list)
        for player in Player.load_json():
            if player.identifiant == identifiant:
                delete_player = input(f"Voulez-vous supprimer, {player.name, player.surname} ?  (OUI/NON) ")
                if delete_player.upper() == "OUI":
                    players_list.pop(player)
                    players_data = [player.to_dict() for player in players_list]
                    with open(FILE_PLAYER, "w") as file:
                        json.dump(players_data, file, indent=4)
                    print("Joueur supprimé avec succès.")

                    break  # Sort de la boucle une fois le joueur trouvé et supprimé

                else:
                    print("Aucun joueur trouvé avec cet identifiant.")

    def add_player(self):
        surname = input("Nom du joueur : ")
        name = input("Prénom du joueur : ")
        date_of_birth = input("Date de naissance du joueur (JJ/MM/YYYY) : ")
        identifiant = input("Identifiant du joueur")
        new_player = Player(surname, name, date_of_birth, identifiant)
        new_player.save()
        print("Joueur ajouté avec succès")

    def update_player_score(self):
        identifiant = input("Entrer l'identifiant du joueur")
        for player in Player.load_json():
            if player.identifiant == identifiant:
                points = int(input("Points ajoutés : "))
                player.update_score(points)
                print(f"Score du joueur, {player.name} mis à jour de {points} points")

