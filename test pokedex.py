import pygame
import json

# Initialiser Pygame
pygame.init()

# Charger les données depuis le fichier JSON
with open("pokedex.json", "r") as file:
    pokemon_data = json.load(file)

# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Définir la taille de la fenêtre
WIDTH, HEIGHT = 800, 600

# Créer la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokédex")

# Charger les images des Pokémon
pokemon_images = {}
for pokemon in pokemon_data:
    image_path = pokemon["image"]
    pokemon_images[pokemon["id"]] = pygame.image.load(image_path)

# Fonction pour afficher les informations du Pokémon sélectionné
def display_pokemon_info(pokemon):
    font = pygame.font.Font(None, 36)
    text = font.render(f"{pokemon['name']} - {pokemon['type']}", True, WHITE)
    screen.blit(text, (20, 20))

# Boucle principale
running = True
selected_pokemon = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si un Pokémon a été cliqué
            x, y = event.pos
            for pokemon in pokemon_data:
                rect = pokemon_images[pokemon["id"]].get_rect(topleft=(pokemon["x"], pokemon["y"]))
                if rect.collidepoint(x, y):
                    selected_pokemon = pokemon

    # Afficher les images des Pokémon
    screen.fill(BLACK)
    for pokemon in pokemon_data:
        image = pokemon_images[pokemon["id"]]
        screen.blit(image, (pokemon["x"], pokemon["y"]))

    # Afficher les informations du Pokémon sélectionné
    if selected_pokemon:
        display_pokemon_info(selected_pokemon)

    pygame.display.flip()

# Quitter Pygame
pygame.quit()
