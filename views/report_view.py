from models.tournament import Tournois
from models.player import Player
from views.tournament_view import ViewTournament

class ViewReport:
    def list_all_players(self):
        players = []
        for player in Player.load_json():
            players.append(player)
        players = sorted(players, key=lambda p: p.name)
        print("\nListe des joueurs (ordre alphabétique) :")
        for player in players:
            print(f"- {player.name}")

    def list_all_tournaments(self):
        tournaments = []
        for tournament in Tournois.load_json():
            tournaments.append(tournament)
        print("\nListe des tournois :")
        for tournament in tournaments:
            print(f"- {tournament.nom} (date de début : {tournament.date_debut})")

    def tournament_details(self):
    
        name = input("Entrer nom du tournois : " )
        for tournament in Tournois.load_json():
            if name == tournament.name:
                print(f"\nDétails du tournoi {tournament.name} :")
                print(f"Date : {tournament.date}")
                print("Joueurs inscrits :")
                for player in sorted(tournament.players, key=lambda p: p.name):
                    print(f"- {player.name}")

    def list_rounds_and_matches(self):
        name = input("Entrer nom du tournois : " )
        for tournament in Tournois.load_json():
            if name == tournament.name:
                print(f"\nRounds et matchs du tournoi {tournament.name} :")
                for round_instance in tournament.rounds:
                    print(f"\n{round_instance.name}")
                    for match in round_instance.matches:
                        print(f"  - {match.player1.name} vs {match.player2.name} | Résultat : {match.result}")
