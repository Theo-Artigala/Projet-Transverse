import pygame
import math

# Constantes
g = 9.81  # Gravité en m/s²
WIDTH, HEIGHT = 800, 600  # Taille de la fenêtre

# Charger l'image de la balle
pygame.init()
ball_image = pygame.image.load("images/boulet_de_canon.png")  # Assurez-vous que l'image est bien placée dans le dossier 'images'
ball_size = ball_image.get_rect().size  # Taille de l'image pour ajuster le positionnement


# Fonction pour calculer la position du projectile
def equation_horaire(force, angle, t):
    angle_rad = math.radians(angle)
    v0 = force  # On suppose une masse unité
    x = v0 * math.cos(angle_rad) * t
    y = v0 * math.sin(angle_rad) * t - 0.5 * g * t ** 2
    return x, y


# Simulation avec pygame
def simulate_projectile(force, angle):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    t = 0
    dt = 0.1  # Intervalle de temps

    # Position initiale
    start_x, start_y = 50, HEIGHT - 50
    trajectory = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fond noir

        # Calcul des nouvelles coordonnées
        x, y = equation_horaire(force, angle, t)
        x, y = start_x + int(x), start_y - int(y)  # Adapter au repère pygame

        # Stocker la trajectoire
        if y < HEIGHT - 50:
            trajectory.append((x, y))
        else:
            running = False

        # Afficher la trajectoire
        for point in trajectory:
            pygame.draw.circle(screen, (255, 0, 0), point, 3)

        # Dessiner l'image de la balle
        screen.blit(ball_image, (x - ball_size[0] // 2, y - ball_size[1] // 2))

        pygame.display.flip()
        clock.tick(30)
        t += dt

    # Attendre la fermeture de la fenêtre
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


# Lancer la simulation
simulate_projectile(force=50, angle=45)