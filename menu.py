import pygame
import jeu
from settings import *
from niveau import *

def menu():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(MENU_PRINCIPAL)
    global niveau_actuel
    niveau_actuel = 0
    niveau_choisi = niveaux[niveau_actuel]

    background = pygame.image.load(BACKGROUND_IMAGE)
    button_img = pygame.image.load(IMAGE_BOUTON_START)
    button_img = pygame.transform.scale(button_img, (200, 150))
    button_rect = button_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    running = True
    while running:
        screen.blit(background, (0, 0))
        screen.blit(button_img, button_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False
                    jeu.lancer_jeu(niveau_choisi)

        pygame.display.flip()
