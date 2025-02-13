import json
from utils.constante import FILE_PLAYER
from models.player import Player, players_list


class ViewPlayer:
    def show_players(self):
       print("Liste des joueurs inscrits : ")
       for player in Player.load_json():
           print(player)

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

