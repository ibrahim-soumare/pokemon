import pygame
import sys
import random

pygame.init()

# exemple couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

#taille de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Combat Pokémon")

#images des Pokémon
pokemon_joueur_image = pygame.image.load("sala.png")
pokemon_adverse_image = pygame.image.load("pika.png")

# Position 
pokemon_joueur_position = (100, 300)
pokemon_adverse_position = (500, 300)

jauge_vie_adverse = 100  # sert d'exemple
jauge_vie_joueur = 100   # sert d'exemple

#puissances des attaques
puissance_attaque1_joueur = 30
puissance_attaque2_joueur = 20

puissance_attaque1_adverse = 25
puissance_attaque2_adverse = 18

# Affichage des Pokémon
def afficher_pokemon():
    fenetre.blit(pokemon_joueur_image, pokemon_joueur_position)
    fenetre.blit(pokemon_adverse_image, pokemon_adverse_position)
    

#Boucle principal du jeu
def jeu():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    attaque_joueur()

                # touche 1 et 2 du clavier pour attaque 1 et 2
                # soucis a regler : le combat se fais automatiquement, ne laisse pas le choix de l'attaque 1 ou 2
                elif event.key == pygame.K_1:
                    attaque_joueur(1)
                elif event.key == pygame.K_2:
                    attaque_joueur(2)

        attaque_adverse()
        afficher_pokemon()
        pygame.display.flip()
        clock.tick(30)


def attaque_joueur(choix_attaque):
    print("1. Attaque 1") #les attaques seront changé en fonction du pokemon (pokedex)
    print("2. Attaque 2") #les attaques seront changé en fonction du pokemon (pokedex)

    if choix_attaque == 1:
        puissance_attaque = puissance_attaque1_joueur
    elif choix_attaque == 2:
        puissance_attaque = puissance_attaque2_joueur
    else:
        print("Choix invalide. Attaque manquée!")
        return

    # Formule test pour calculer les degats 
    degats = random.randint(1, 10) + puissance_attaque

    #jauge de vie du Pokémon adverse
    global jauge_vie_adverse
    jauge_vie_adverse -= degats

    print(f"Le joueur attaque avec {choix_attaque} et inflige {degats} dégâts au Pokémon adverse!")
    #le message s'affiche sur le terminal , a modifier pour qu'ils s'affichent directement sur le jeu

    if jauge_vie_adverse <= 0:
        print("Le Pokémon adverse a été vaincu!")
        #le message s'affiche sur le terminal , a modifier pour qu'ils s'affichent directement sur le jeu
        pygame.quit()
        sys.exit()

# Fonction d'attaque adverse
def attaque_adverse():
    attaque_aleatoire = random.choice(["attaque1", "attaque2"])

    if attaque_aleatoire == "attaque1":
        puissance_attaque_adverse = puissance_attaque1_adverse
    elif attaque_aleatoire == "attaque2":
        puissance_attaque_adverse = puissance_attaque2_adverse

    # Formule formule test pour calculer les degats 
    degats_adverses = random.randint(1, 10) + puissance_attaque_adverse

    # Réduire la jauge de vie du Pokémon du joueur
    global jauge_vie_joueur
    jauge_vie_joueur -= degats_adverses

    print(f"Le Pokémon adverse attaque avec {attaque_aleatoire} et inflige {degats_adverses} dégâts au Pokémon du joueur!")

    if jauge_vie_joueur <= 0:
        print("Le Pokémon du joueur a été vaincu!")
        pygame.quit()
        sys.exit()

# Lancement du jeu
if __name__ == "__main__":
    jeu()

#soucis dans la boucle il y a que le pokemon adverse qui attaque, peut etre rajouter une fonction "tour par tour"