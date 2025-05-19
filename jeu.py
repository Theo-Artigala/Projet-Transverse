import pygame
from settings import *
from ball import Ball
from hoop import Hoop

def lancer_jeu():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    fond = pygame.image.load(BACKGROUND_IMAGE)
    fond = pygame.transform.scale(fond, (WIDTH, HEIGHT))
    gamestate = True
    angle, force = selection_parametres(screen, fond)

    # Création des objets
    ball = Ball(50, HEIGHT - 50, force,angle)
    hoop = Hoop(WIDTH - 150, HEIGHT // 2)

    # Boucle de jeu
    running = True
    while running:
        screen.blit(fond, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball.update()
        ball.draw(screen)
        hoop.draw(screen)

        if hoop.check_collision(ball) and gamestate == True:
            gamestate = False

            print("Panier réussi !")

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def selection_parametres(screen, fond):
    angle = 45
    force = 25
    font = pygame.font.Font(None, 30)

    selecting = True
    while selecting:
        screen.blit(fond, (0, 0))
        angle_text = font.render(f"Angle: {angle}°", True, (255, 255, 255))
        force_text = font.render(f"Force: {force}", True, (255, 255, 255))
        start_text = font.render("Entrée pour tirer", True, (255, 255, 0))

        screen.blit(angle_text, (50, 50))
        screen.blit(force_text, (50, 100))
        screen.blit(start_text, (50, 150))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    angle = min(angle + 5, 90)
                elif event.key == pygame.K_DOWN:
                    angle = max(angle - 5, 0)
                elif event.key == pygame.K_LEFT:
                    force = max(force - 1, 10)
                elif event.key == pygame.K_RIGHT:
                    force = min(force + 1, 100)
                elif event.key == pygame.K_RETURN:
                    selecting = False

    return angle, force
