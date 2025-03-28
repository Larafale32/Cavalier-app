# Gestionnaire de Tournois d'Échecs

## Description

Ce programme permet d'organiser et de gérer des tournois d'échecs en mode hors ligne. Il permet l'ajout de joueurs, la gestion des tournois, l'enregistrement des matchs et la génération automatique des paires selon un système de classement basé sur les scores.

L'application fonctionne en mode console et utilise des fichiers JSON pour stocker les données des joueurs et des tournois.

## Fonctionnalités

- **Connexion** :
  - L'administateur devra se connecter à l'application avec un code à 4 chiffres

- **Gestion des joueurs** :
  - Ajout des joueurs avec nom, prénom, date de naissance et identifiant national d'échecs.
  - Possibilité de modifier/supprimer un joueur
  
- **Organisation des tournois** :
  - Création de tournois avec nom, lieu, dates, nombre de tours, etc.
  - Modififcation/supression des tournois
  - Enregistrement des joueurs dans un tournoi.
  - Lancer un toutnois
  - Modifier les scores d'un round et passer au suivant jusqu'au dernier round 
  - Afficher le classement
    
- **Génération automatique des paires** :
  - Mélange des joueurs au premier tour.
  - Attribution des adversaires en fonction des scores des joueurs.
  - Évitement des matchs en double.
    
- **Système de points** :
  - Victoire : 1 point.
  - Défaite : 0 point.
  - Match nul : 0,5 point pour chaque joueur.
    
- **Rapports** :
  - Liste des joueurs (par ordre alphabétique).
  - Liste des tournois.
  - Détails d'un tournoi (dates, joueurs, tours, matchs).
  - Détails des rounds et des matches d'un tournois
    
- **Sauvegarde et chargement des données** :
  - Les données des joueurs, des administrateurs et des tournois sont rangées dans des fichiers JSON.
  - Chargement des données à l'exécution pour restaurer l'état précédent.
    
- **Architecture propre et maintenable** :
  - Respect du modèle MVC (Modèle-Vue-Contrôleur).
  - Conformité avec PEP 8 grâce à Flake8.

## Installation

### Prérequis

- Python 3.x installé
- Pip installé

### Étapes d'installation

1. **Cloner le repository** :
   ```bash
   git clone <URL_DU_REPO>
   cd <NOM_DU_REPO>
2- **Installer les dépendances** :
  pip install -r requirements.txt


### Utilisation

**Lancer le programme**
Dans le terminal, exécuter la commande suivante :
  python main.py
  
**Navigation dans l'application**
  Connexion: 
    "Entrer votre code administrateur : "
    Code administrateur : 2312
    
  Menu : 
    Veuillez sélectionner une action (1,2,3 ou 4)
    1) Gestion des joueurs
    2) Gestion des tournois
    3) Report (stat : joueurs/tournois)
    4) Quitter
    

### Structure du projet

/cavalier-app 

    ```/data                 # Contient les fichiers JSON pour la persistance des données```
    
    ```/models               # Définit les classes des joueurs, tournois, tours, matchs```
  
    
     ```/views                # Gère l'affichage et l'interaction avec l'utilisateur```
     
    ```/controllers          # Contient la logique du programme et les actions utilisateurs```
    
    ```requirements.txt      # Liste des dépendances```
    
    ```main.py               # Point d'entrée du programme```
    
    ```README.md             # Documentation du projet```


## Améliorations futures

Ajout d'une interface graphique.
Exportation des rapports en format HTML/PDF.


