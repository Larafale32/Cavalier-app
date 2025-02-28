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

    def tournament_details(self, tournament_choice):
        print(f"\nDétails du tournoi {tournament_choice.nom} :")
        print(f"Date de début: {tournament_choice.date_debut}")
        print(f"Date de fin: {tournament_choice.date_fin}")
        print("Joueurs inscrits :")
        for player in tournament_choice.players_inscrits:
            print(f"- {player}")

    def list_rounds_and_matches(self, tournament_choice):
        print(f"\nRounds et matchs du tournoi {tournament_choice.nom} :")
        for round_instance in tournament_choice.rounds:
            print(f"\n Round numéro : {round_instance.tour} statut : {round_instance.state}")
            for match in round_instance.matches:
                print(f"  - {match.player1} vs {match.player2} | Résultat : {match.result}")
