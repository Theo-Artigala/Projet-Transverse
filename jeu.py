import pygame
from fleches import *
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
    angle, force = selection_parametres(screen, fond, niveau)

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
        global NBR_DESSAI
        if ball.vx ==0 and ball.vy ==0:
            son.play()
            NBR_DESSAI = NBR_DESSAI + 1
            niveau1 = niveaux[niveau_actuel]
            niveau1.ball_start = (ball.x, ball.y)
            lancer_jeu(niveau1)
        if hoop.check_collision(ball) and gamestate:
            gamestate = False
            print("Panier réussi !")

        # Dessine les murs du niveau
        for wall in niveau.murs:
            wall.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def selection_parametres(screen, fond, niveau):
    angle = 45
    force = 25
    font = pygame.font.Font(None, 30)

    x_start, y_start = niveau.ball_start

    selecting = True
    while selecting:
        screen.blit(fond, (0, 0))
        # Dessine le niveau
        for wall in niveau.murs:
            wall.draw(screen)
        hoop = Hoop(*niveau.hoop_pos)
        hoop.draw(screen)

        # Crée une balle pour la prévisualisation
        balle = Ball(x_start, y_start, force, angle)

        # Calcul de la trajectoire
        points = []
        t = 0
        dt = 0.1  # pas de temps
        vx = force * math.cos(math.radians(angle))
        vy = -force * math.sin(math.radians(angle))
        x = x_start
        y = y_start

        while y < HEIGHT and x > 0 and x < WIDTH:
            # Calcul de la position à t + dt
            x = x_start + vx * t
            y = y_start + vy * t + 0.5 * GRAVITY * t * t
            points.append((x, y))
            t += dt

        # Dessine la trajectoire
        for point in points:
            if 0 <= point[0] <= WIDTH and 0 <= point[1] <= HEIGHT:
                pygame.draw.circle(screen, (255, 255, 0, 128), (int(point[0]), int(point[1])), 3)

        # Dessine la balle à la position de départ
        balle.rect.x = x_start - balle.radius
        balle.rect.y = y_start - balle.radius
        balle.draw(screen)

        # Affiche le texte
        angle_text = font.render(f"Angle: {angle}°", True, (255, 255, 255))
        force_text = font.render(f"Force: {force}", True, (255, 255, 255))
        start_text = font.render("Entrée pour tirer", True, (255, 255, 0))
        screen.blit(angle_text, (50, 50))
        screen.blit(force_text, (50, 100))
        screen.blit(start_text, (50, 150))

        draw_fleche(screen, angle, force, (x_start, y_start))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    angle = min(angle + 5, 180)
                elif event.key == pygame.K_DOWN:
                    angle = max(angle - 5, 0)
                elif event.key == pygame.K_LEFT:
                    force = max(force - 1, 10)
                elif event.key == pygame.K_RIGHT:
                    force = min(force + 1, 100)
                elif event.key == pygame.K_RETURN:
                    selecting = False
    return angle, force
