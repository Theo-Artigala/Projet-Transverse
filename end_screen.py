import pygame
import jeu
from settings import *
from menu import *

def end_screen():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(END_SCREEN)

    background = pygame.image.load(BACKGROUND_IMAGE)
    button_img = pygame.image.load(IMAGE_BOUTON_START)
    button_img = pygame.transform.scale(button_img, (200, 80))
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
                    menu.menu

        pygame.display.flip()
