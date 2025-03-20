import pygame
import jeu

pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Principal")

# Charger les images
background = pygame.image.load("images/bg2.jpg")
button_img = pygame.image.load("images/bouton.png")
button_img = pygame.transform.scale(button_img, (200, 80))

# Position du bouton
button_rect = button_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))


def menu():
    running = True
    while running:
        screen.blit(background, (0, 0))
        screen.blit(button_img, button_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False  # Quitte le menu
                    jeu.lancer_jeu()  # Démarre le jeu

        pygame.display.flip()


if __name__ == "__main__":
    menu()
