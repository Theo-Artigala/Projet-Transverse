import pygame
from settings import *
from ball import *
from hoop import *
from niveau import *
from hoop import *


def lancer_jeu(niveau):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    background = pygame.image.load(niveau.decor)
    fond = pygame.transform.scale(background, (WIDTH, HEIGHT))
    gamestate = True
    angle, force = selection_parametres(screen, fond)

    # Création des objets
    hoop = Hoop(*niveau.hoop_pos)
    ball = Ball(*niveau.ball_start, force, angle)

    # Boucle de jeu
    running = True
    while running:
        screen.blit(fond, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Utilise la liste de murs du niveau
        ball.update(niveau.murs)
        ball.draw(screen)
        hoop.draw(screen)
        if ball.vx ==0 and ball.vy ==0:
            son.play()
        if hoop.check_collision(ball) and gamestate:
            gamestate = False
            print("Panier réussi !")

        # Dessine les murs du niveau
        for wall in niveau.murs:
            wall.draw(screen)

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
