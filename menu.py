import pygame 
import sys
from Pokedex import Pokedex  # Importez la classe du module Pokedex

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Mon Jeu")

#image de fond
fond = pygame.image.load("fond2.png")
fond = pygame.transform.scale(fond, (largeur_fenetre, hauteur_fenetre))

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0, 0)  

# Police et titre
police_titre = pygame.font.SysFont(None, 80)
titre = police_titre.render("POKEMON", True, blanc)

# Police
police_bouton = pygame.font.SysFont(None, 50) #police a changer 

# Boutons
Commencer_rect = pygame.Rect(0, 200, 300, 50)
Pokedex_rect = pygame.Rect(0, 270, 300, 50)
Nouvelle_partie_rect = pygame.Rect(0, 340, 300, 50)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                pos = pygame.mouse.get_pos()
                if Commencer_rect.collidepoint(pos):
                    print("Commencer")
                    # commencer la partie / sert aussi a continuer
                elif Pokedex_rect.collidepoint(pos):
                    print("Pokedex")
                    pokedex_instance = Pokedex()  # Créez une instance de la classe Pokedex
                    pokedex_instance.run()  # Appeler la méthode run de la classe Pokedex
                    # afficher pokedex
                elif Nouvelle_partie_rect.collidepoint(pos):
                    print("Nouvelle Partie")
                    # nouvelle partie (reset)

    # Affichage de l'image de fond
    fenetre.blit(fond, (0, 0))

    # Affichage du titre
    fenetre.blit(titre, (largeur_fenetre // 2 - titre.get_width() // 2, 50))

    # Affichage des boutons
    #pygame.draw.rect(fenetre, noir, commencer_rect)
    #pygame.draw.rect(fenetre, noir, pokedex_rect)
    #pygame.draw.rect(fenetre, noir, nouvelle_partie_rect)

    texte_commencer = police_bouton.render("Commencer", True, blanc)
    fenetre.blit(texte_commencer, (Commencer_rect.x + 10, Commencer_rect.y + 10))

    texte_pokedex = police_bouton.render("Pokedex", True, blanc)
    fenetre.blit(texte_pokedex, (Pokedex_rect.x + 10, Pokedex_rect.y + 10))

    texte_nouvelle_partie = police_bouton.render("Nouvelle Partie", True, blanc)
    fenetre.blit(texte_nouvelle_partie, (Nouvelle_partie_rect.x + 10, Nouvelle_partie_rect.y + 10))

    
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
