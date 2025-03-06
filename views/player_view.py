import json
import re
from datetime import datetime
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
        while True:
            player.surname = input(f"Nouveau nom pour {player.name} {player.surname}: ")
            if player.surname is int():
                print("Entrée invalide")
            else:
                player.update()
                print("Nom mis à jour avec succès.")
                break

    def change_name(self, player):
        while True:
            player.name = input(f"Nouveau prénom pour {player.name} {player.surname}: ")
            if player.name is int():
                print("Entrée invalide")
            else:
                player.update()
                print("Prénom mis à jour avec succès.")
                break

    def change_date_of_birth(self, player):
        while True:
            player.date_of_birth = input(
                f"Nouvelle date de naissance pour {player.name} {player.surname} (JJ/MM/AAAA) : ")
            try:
                # Vérifie si la date respecte le format JJ/MM/AAAA
                datetime.strptime(player.date_of_birth, "%d/%m/%Y")
                break  # Sort de la boucle si l'entrée est valide
            except ValueError:
                print("Format invalide ! Veuillez entrer une date au format JJ/MM/AAAA.")

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
        while True:
            surname = input("Nom du joueur : ")
            if surname.isalpha():
                break
            else:
                print("Entrée invalide")
        while True:
            name = input("Prénom du joueur : ")
            if name.isalpha():
                break
            else:
                print("Entrée invalide")
        while True:
            date_of_birth = input("Date de naissance du joueur (JJ/MM/YYYY) : ")
            try:
                # Vérifie si la date respecte le format JJ/MM/AAAA
                datetime.strptime(date_of_birth, "%d/%m/%Y")
                break  # Sort de la boucle si l'entrée est valide
            except ValueError:
                print("Format invalide ! Veuillez entrer une date au format JJ/MM/AAAA.")
        while True:
            identifiant = input("Entrez l'identifiant (AB12345) : ")

            if re.match(r"^[A-Za-z]{2}\d{5}$", identifiant):
                print(f"Identifiant valide : {identifiant}")
                break
            else:
                print("Format invalide. Veuillez entrer 2 lettres suivies de 5 chiffres.")

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

