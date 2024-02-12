import pygame
import sys
import json

class Pokedex:
    def __init__(self):
        pygame.init()

        # Génération de la fenêtre de notre jeu
        pygame.display.set_caption("Mon Pokedex")
        self.screen = pygame.display.set_mode((850, 531))

        # Importation de l'image de notre pokedex qui sera en arrière-plan
        self.background = pygame.image.load('image/pokedex.png')
        self.background = pygame.transform.scale(self.background, (850, 531))

        # Créer une surface avec un fond blanc
        self.white_background = pygame.Surface(self.screen.get_size())
        self.white_background.fill((255, 255, 255))

        self.running = True

        # Charger les données du fichier JSON
        self.pokemon_data = self.load_pokemon_data()

        # Index du Pokémon actuellement affiché
        self.current_pokemon_index = 0

        # Charger l'image du Pokémon actuel
        self.load_current_pokemon_image()

    def load_pokemon_data(self):
        with open('pokedex.json', 'r') as file:
            data = json.load(file)
        return data

    def load_current_pokemon_image(self):
        current_pokemon = self.pokemon_data[self.current_pokemon_index]
        image_path = f"image/{current_pokemon['image']}"
        self.current_pokemon_image = pygame.image.load(image_path)
        self.current_pokemon_image = pygame.transform.scale(self.current_pokemon_image, (150, 150))

    def run(self):
        # Boucle tant que cette condition est vrai
        while self.running:
            self.handle_events()
            self.update_display()

        pygame.quit()
        print("Fermeture du Pokedex")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.is_click_on_left_arrow(mouse_pos):
                    self.previous_pokemon()
                elif self.is_click_on_right_arrow(mouse_pos):
                    self.next_pokemon()

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

    def draw_arrows(self):
        # Flèche vers la gauche
        pygame.draw.rect(self.screen, (179, 0, 255), pygame.Rect(125, 388, 38, 25), border_radius=10)
        # Flèche vers la droite
        pygame.draw.rect(self.screen, (179, 0, 255), pygame.Rect(190, 388, 38, 25), border_radius=10)
        # Flèche vers le haut
        pygame.draw.rect(self.screen, (179, 0, 255), pygame.Rect(164, 355, 25, 34), border_radius=10)
        # Flèche vers le bas
        pygame.draw.rect(self.screen, (179, 0, 255), pygame.Rect(164, 412, 25, 30), border_radius=10)

    def display_current_pokemon_data(self):
        font = pygame.font.Font(None, 30)
        y_position = 325

        current_pokemon = self.pokemon_data[self.current_pokemon_index]

        # Afficher chaque attribut sur une nouvelle ligne, en excluant "image"
        for attribute, value in current_pokemon.items():
            if attribute.lower() != 'image':
                text = font.render(f"{attribute.capitalize()}: {value}", True, (0, 0, 0))
                self.screen.blit(text, (280, y_position))
                y_position += 30

        # Ajouter un espacement vertical entre chaque Pokémon
        y_position += 20

    def display_current_pokemon_image(self):
        # Afficher l'image du Pokémon actuel
        x_position = 350
        y_position = 60
        self.screen.blit(self.current_pokemon_image, (x_position, y_position))

    def is_click_on_left_arrow(self, mouse_pos):
        return 125 <= mouse_pos[0] <= 163 and 388 <= mouse_pos[1] <= 413

    def is_click_on_right_arrow(self, mouse_pos):
        return 190 <= mouse_pos[0] <= 228 and 388 <= mouse_pos[1] <= 413

    def next_pokemon(self):
        # Passer au Pokémon suivant
        self.current_pokemon_index = (self.current_pokemon_index + 1) % len(self.pokemon_data)
        # Charger l'image du Pokémon actuel
        self.load_current_pokemon_image()

    def previous_pokemon(self):
        # Passer au Pokémon précédent
        self.current_pokemon_index = (self.current_pokemon_index - 1) % len(self.pokemon_data)
        # Charger l'image du Pokémon actuel
        self.load_current_pokemon_image()

if __name__ == "__main__":
    pokedex = Pokedex()
    pokedex.run()
