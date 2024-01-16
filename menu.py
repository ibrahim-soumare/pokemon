import pygame
import sys


pygame.init()


largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Mon Jeu")

# Chargement de l'image de fond
fond = pygame.image.load("fond2.png")
fond = pygame.transform.scale(fond, (largeur_fenetre, hauteur_fenetre))

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0, 0)  # La valeur alpha 0 rend la couleur transparente

# Police et titre
police_titre = pygame.font.SysFont(None, 80)
titre = police_titre.render("Mon Super Jeu", True, blanc)

# Police et boutons
police_bouton = pygame.font.SysFont(None, 50)

# Boutons
commencer_rect = pygame.Rect(0, 200, 300, 50)
pokedex_rect = pygame.Rect(0, 270, 300, 50)
nouvelle_partie_rect = pygame.Rect(0, 340, 300, 50)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                pos = pygame.mouse.get_pos()
                if commencer_rect.collidepoint(pos):
                    print("Commencer")
                    # commencer la game
                elif pokedex_rect.collidepoint(pos):
                    print("Pokedex")
                    # afficher pokedex
                elif nouvelle_partie_rect.collidepoint(pos):
                    print("Nouvelle Partie")
                    # nouvella partie

    # Affichage de l'image de fond
    fenetre.blit(fond, (0, 0))

    # Affichage du titre
    fenetre.blit(titre, (largeur_fenetre // 2 - titre.get_width() // 2, 50))

    # Affichage des boutons
    #pygame.draw.rect(fenetre, noir, commencer_rect)
    #pygame.draw.rect(fenetre, noir, pokedex_rect)
    #pygame.draw.rect(fenetre, noir, nouvelle_partie_rect)

    # Texte des boutons
    texte_commencer = police_bouton.render("Commencer", True, blanc)
    fenetre.blit(texte_commencer, (commencer_rect.x + 10, commencer_rect.y + 10))

    texte_pokedex = police_bouton.render("Pokedex", True, blanc)
    fenetre.blit(texte_pokedex, (pokedex_rect.x + 10, pokedex_rect.y + 10))

    texte_nouvelle_partie = police_bouton.render("Nouvelle Partie", True, blanc)
    fenetre.blit(texte_nouvelle_partie, (nouvelle_partie_rect.x + 10, nouvelle_partie_rect.y + 10))

    
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
