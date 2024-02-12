import pygame  # Importation de la bibliothèque Pygame pour créer des jeux
import sys     # Importation du module sys pour accéder à certaines fonctionnalités du système
import json    # Importation du module json pour travailler avec des données au format JSON

class Pokedex:
    def __init__(self):
        pygame.init()  # Initialisation de Pygame

        # Génération de la fenêtre de notre jeu avec une taille de 850x531 pixels
        pygame.display.set_caption("Mon Pokedex")  # Définition du titre de la fenêtre
        self.screen = pygame.display.set_mode((850, 531))  # Création de la surface de la fenêtre

        # Importation de l'image de notre Pokedex qui servira de fond d'écran
        self.background = pygame.image.load('image/pokedex.png')  # Chargement de l'image du Pokedex
        self.background = pygame.transform.scale(self.background, (850, 531))  # Redimensionnement de l'image

        # Création d'une surface avec un fond blanc pour afficher des éléments par-dessus le fond d'écran
        self.white_background = pygame.Surface(self.screen.get_size())  # Création d'une surface de la même taille que la fenêtre
        self.white_background.fill((255, 255, 255))  # Remplissage de la surface avec une couleur blanche

        self.running = True  # Variable pour contrôler l'exécution de la boucle principale du jeu

        # Chargement des données des Pokemon à partir du fichier JSON
        self.pokemon_data = self.load_pokemon_data()  

        # Index du Pokémon actuellement affiché
        self.current_pokemon_index = 0  

        # Chargement de l'image du Pokémon actuel
        self.load_current_pokemon_image()  

    def load_pokemon_data(self):
        with open('pokedex.json', 'r') as file:  # Ouverture du fichier JSON contenant les données des Pokémon
            data = json.load(file)  # Chargement des données depuis le fichier JSON
        return data  # Renvoi des données chargées

    def load_current_pokemon_image(self):
        current_pokemon = self.pokemon_data[self.current_pokemon_index]  # Récupération des données du Pokémon actuel
        image_path = f"image/{current_pokemon['image']}"  # Chemin d'accès à l'image du Pokémon
        self.current_pokemon_image = pygame.image.load(image_path)  # Chargement de l'image du Pokémon
        self.current_pokemon_image = pygame.transform.scale(self.current_pokemon_image, (150, 150))  # Redimensionnement de l'image

    def run(self):
        # Boucle principale du jeu
        while self.running:  
            self.handle_events()  # Gestion des événements pygame
            self.update_display()  # Mise à jour de l'affichage

        pygame.quit()  # Fermeture de Pygame
        print("Fermeture du Pokedex")  

    def handle_events(self):
        for event in pygame.event.get():  # Parcours de tous les événements pygame
            if event.type == pygame.QUIT:  # Si l'événement est de fermeture de la fenêtre
                self.running = False  # Mettre fin à l'exécution de la boucle principale
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Si l'événement est un clic de souris
                mouse_pos = pygame.mouse.get_pos()  # Obtenir la position du clic de souris
                if self.is_click_on_left_arrow(mouse_pos):  # Si le clic est sur la flèche gauche
                    self.previous_pokemon()  # Changer pour le Pokémon précédent
                elif self.is_click_on_right_arrow(mouse_pos):  # Si le clic est sur la flèche droite
                    self.next_pokemon()  # Changer pour le Pokémon suivant

    def update_display(self):
        # Appliquer le fond blanc
        self.screen.blit(self.white_background, (0, 0))

        # Appliquer l'arrière-plan Pokedex
        self.screen.blit(self.background, (0, 0))

        # Dessiner des flèches directionnelles avec coins arrondis
        self.draw_arrows()

        # Afficher les données du Pokémon actuel
        self.display_current_pokemon_data()

        # Afficher l'image du Pokémon actuel
        self.display_current_pokemon_image()

        # Mettre à jour l'écran
        pygame.display.flip()

    # La fonction draw_arrows dessine les flèches directionnelles sur l'écran
    def draw_arrows(self):
        # Flèche vers la gauche
        pygame.draw.rect(self.screen, (179, 0, 255), pygame.Rect(125, 388, 38, 25), border_radius=10)
        # Flèche vers la droite
        pygame.draw.rect(self.screen, (179, 0, 255), pygame.Rect(190, 388, 38, 25), border_radius=10)
        # Flèche vers le haut
        pygame.draw.rect(self.screen, (179, 0, 255), pygame.Rect(164, 355, 25, 34), border_radius=10)
        # Flèche vers le bas
        pygame.draw.rect(self.screen, (179, 0, 255), pygame.Rect(164, 412, 25, 30), border_radius=10)

    # La fonction display_current_pokemon_data affiche les données du Pokémon actuel sur l'écran
    def display_current_pokemon_data(self):
        font = pygame.font.Font(None, 30)  # Chargement de la police de caractères
        y_position = 325  # Position verticale de départ pour afficher les données

        current_pokemon = self.pokemon_data[self.current_pokemon_index]  # Récupération des données du Pokémon actuel

        # Affichage de chaque attribut du Pokémon sur une nouvelle ligne, en excluant l'attribut 'image'
        for attribute, value in current_pokemon.items():
            if attribute.lower() != 'image':
                text = font.render(f"{attribute.capitalize()}: {value}", True, (0, 0, 0))  # Création du texte à afficher
                self.screen.blit(text, (280, y_position))  # Affichage du texte sur l'écran
                y_position += 30  # Déplacement de la position verticale pour afficher le prochain attribut

        y_position += 20  # Ajout d'un espacement vertical entre chaque Pokémon

    # La fonction display_current_pokemon_image affiche l'image du Pokémon actuel sur l'écran
    def display_current_pokemon_image(self):
        x_position = 350  # Position horizontale de l'image
        y_position = 60   # Position verticale
