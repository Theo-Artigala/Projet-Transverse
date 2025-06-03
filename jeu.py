import pygame

from fleches import *


import end_screen

from settings import *
from ball import *
from niveau import *
from hoop import *





def lancer_jeu(niveau):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    background = pygame.image.load(niveau.decor)
    fond = pygame.transform.scale(background, (WIDTH, HEIGHT))
    angle, force = selection_parametres(screen, fond, niveau)
    score_font = pygame.font.Font(None, 36)
    global NBR_DESSAI
    global niveau_actuel

    # on crée nos objets
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

        # Affichage du score en haut à droite
        score_text = score_font.render(f"Essais: {NBR_DESSAI}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topright=(WIDTH - 20, 20))
        screen.blit(score_text, score_rect)

        # Affichage du niveau actuel
        niveau_text = score_font.render(f"Niveau: {niveau_actuel + 1}/{len(niveaux)}", True, (255, 255, 255))
        niveau_rect = niveau_text.get_rect(topright=(WIDTH - 20, 60))
        screen.blit(niveau_text, niveau_rect)


        if ball.vx == 0 and ball.vy == 0:
            son.play()
            NBR_DESSAI = NBR_DESSAI + 1
            niveau1 = niveaux[niveau_actuel]
            niveau1.ball_start = (ball.x, ball.y)
            lancer_jeu(niveau1)
        if hoop.check_collision(ball):
            print(niveau_actuel)
            print("Niveau terminé !")
            if niveau_actuel + 1 < len(niveaux):
                niveau_actuel += 1
                print(niveau_actuel)
                lancer_jeu(niveaux[niveau_actuel])

            else:
                print(len(niveaux))
                print("Tous les niveaux terminés !")
                print(niveau_actuel)
                end_screen.end_screen()
            return

        # met les murs du niveau dans le code
        for wall in niveau.murs:
            wall.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def selection_parametres(screen, fond, niveau):
    angle = 45
    force = 25
    font = pygame.font.Font(None, 30)

    # Variables pour contrôler l'affichage
    show_trajectory = False
    show_arrow = True

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

        if show_trajectory:
            while y < HEIGHT and x > 0 and x < WIDTH and y > 0:
                # Calcul de la position à t + dt
                x = x_start + vx * t
                y = y_start + vy * t + 0.5 * GRAVITY * t * t
                points.append((x, y))
                t += dt

            # Dessine la trajectoire
            for point in points:
                if 0 <= point[0] <= WIDTH and 0 <= point[1] <= HEIGHT:
                    pygame.draw.circle(screen, (255, 255, 0), (int(point[0]), int(point[1])), 3)

        # Afficher la flèche si activée
        if show_arrow:
            draw_fleche(screen, angle, force, (x_start, y_start))

        # Dessine la balle à la position de départ
        balle.rect.x = x_start - balle.radius
        balle.rect.y = y_start - balle.radius
        balle.draw(screen)

        score_font = pygame.font.Font(None, 36)
        global NBR_DESSAI
        global niveau_actuel

        # Affichage du score en haut à droite
        score_text = score_font.render(f"Essais: {NBR_DESSAI}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topright=(WIDTH - 20, 20))
        screen.blit(score_text, score_rect)

        # Affichage du niveau actuel
        niveau_text = score_font.render(f"Niveau: {niveau_actuel + 1}/{len(niveaux)}", True, (255, 255, 255))
        niveau_rect = niveau_text.get_rect(topright=(WIDTH - 20, 60))
        screen.blit(niveau_text, niveau_rect)

        # Affiche le texte
        angle_text = font.render(f"Angle: {angle}°", True, (255, 255, 255))
        force_text = font.render(f"Force: {force}", True, (255, 255, 255))
        start_text = font.render("Entrée pour tirer", True, (255, 255, 0))

        # Instructions pour les touches de contrôle
        trajectory_text = font.render(f"Touche A: {'Masquer' if show_trajectory else 'Afficher'} trajectoire", True,
                                      (255, 255, 255))
        arrow_text = font.render(f"Touche Z: {'Masquer' if show_arrow else 'Afficher'} flèche", True, (255, 255, 255))

        screen.blit(angle_text, (50, 50))
        screen.blit(force_text, (50, 100))
        screen.blit(start_text, (50, 150))
        screen.blit(trajectory_text, (50, 200))
        screen.blit(arrow_text, (50, 250))

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
                elif event.key == pygame.K_a:
                    # Activer/désactiver la trajectoire
                    show_trajectory = not show_trajectory
                elif event.key == pygame.K_z:
                    # Activer/désactiver la flèche
                    show_arrow = not show_arrow

    return angle, force

