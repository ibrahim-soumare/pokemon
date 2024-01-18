# pokemon.py
class Pokemon:
    def __init__(self, name, hp, level, attack_power, defense, types):
        self.name = name
        self.hp = hp
        self.level = level
        self.attack_power = attack_power
        self.defense = defense
        self.types = types


# combat.py
import random

class Combat:
    def __init__(self, player_pokemon, opponent_pokemon):
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon

    def calculate_damage(self, attacker_type, defender_type, attacker_attack_power):
        # Logique pour calculer les dégâts en fonction des types
        # Retourner les dégâts subis par le défenseur

    def apply_defense(self, damage):
        # Appliquer la défense pour réduire les dégâts subis par le Pokémon

    def winner(self):
        # Retourner le nom du vainqueur

    def save_to_pokedex(self, pokemon):
        # Enregistrer le Pokémon dans le Pokédex
        # Vérifier les doublons avant d'ajouter

    def loser_winner_names(self):
        # Retourner le nom du Pokémon perdant et gagnant


# pokedex.py
import json

class Pokedex:
    def __init__(self):
        self.pokemon_list = []

    def add_pokemon(self, pokemon):
        # Ajouter un Pokémon au Pokedex

    def display_pokedex(self):
        # Afficher l'ensemble des Pokémon rencontrés et leur nombre


# main.py
from tkinter import Tk, Label, Button

# Logique de l'interface graphique avec Tkinter
# ...

# Programme principal
if __name__ == "__main__":
    # Lancer une partie
    # Ajouter un Pokémon
    # Accéder au Pokedex
    # ...

    # Lors du démarrage de la partie, initialiser les objets nécessaires
    player_pokemon = Pokemon("Pikachu", 100, 10, 20, 10, ["Electric"])
    opponent_pokemon = random.choice(pokemon_list_from_json_file)

    combat_instance = Combat(player_pokemon, opponent_pokemon)
    pokedex_instance = Pokedex()

    # Lancer l'interface graphique avec Tkinter
    # ...
