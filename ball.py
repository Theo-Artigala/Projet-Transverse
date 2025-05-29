import pygame
import math
from settings import WIDTH, HEIGHT, GRAVITY, BALL_IMAGE


class Ball:
    def __init__(self, x, y, force, angle):
        original_image = pygame.image.load(BALL_IMAGE).convert_alpha()
        self.x = x
        self.y = y
        self.radius = 25
        self.image = pygame.transform.scale(original_image, (self.radius * 2, self.radius * 2))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (255, 0, 0)
        self.force = force
        self.angle = math.radians(angle)
        self.vx = force * math.cos(self.angle)
        self.vy = -force * math.sin(self.angle)
        self.bounces = 0
        self.max_bounces = 15
        self.trail = []  # Liste des anciennes positions pour faire la trainee en gros on copie tt les anciennes positioins de la balle pour un effet style
        self.max_trail_length = 15  # Nombre de points dans la traînée

    def update(self, walls):
        # Limiter la vitesse en descente
        if self.vy > 0:  # La balle descend
            self.vy *= 0.98  # Diminution progressive, ajustez le facteur
            if abs(self.vy) < 0.1:
                self.vy = 0

        # Limite la vitesse horizontale
        max_speed = 20
        self.vx = max(-max_speed, min(self.vx, max_speed))

        # Mouvement
        self.vy += GRAVITY
        self.x += self.vx
        self.y += self.vy

        # Mise à jour du rect
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

        restitution = 0.7

        self.trail.append((self.x, self.y))
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)

        # Rebond sur le sol
        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy * restitution
            # Si la vitesse est trop faible, on la met à zéro pour éviter des rebonds infinis
            if abs(self.vy) < 1:
                self.vy = 0
            self.bounces += 1
            if self.bounces >= self.max_bounces:
                self.vx = 0
                self.vy = 0

        # Rebond sur les murs (gauche et droite)
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx * restitution
        elif self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
            self.vx = -self.vx * restitution

        elif self.y - self.radius <0:
            self.y =  self.radius
            self.vy = -self.vy * restitution


        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

        def circle_rect_collision(cx, cy, radius, rect):
            # la on va check le point de nos murs qui sera le plus proche du centre de notre balle
            lacollision = False
            closest_x = max(rect.left, min(cx, rect.right))
            closest_y = max(rect.top, min(cy, rect.bottom))
            # mtn on calcule la distance entre ce point et le centre de la balle.
            dx = cx - closest_x
            dy = cy - closest_y
            if dx * dx + dy * dy < radius * radius:
                lacollision = True
            return lacollision

        for wall in walls:
            if circle_rect_collision(self.x, self.y, self.radius, wall.rect):
                # Trouver le point du mur le plus proche du centre de la balle
                closest_x = max(wall.rect.left, min(self.x, wall.rect.right))
                closest_y = max(wall.rect.top, min(self.y, wall.rect.bottom))
                dx = self.x - closest_x
                dy = self.y - closest_y

                # Calculer la distance
                dist_squared = dx * dx + dy * dy
                dist = dist_squared ** 0.5  # racine carrée

                # Si la distance est nulle, on ne fait rien (on saute la collision)
                if dist == 0:
                    continue

                # Normaliser le vecteur (dx, dy)
                nx = dx / dist
                ny = dy / dist

                # Repousser la balle hors du mur
                overlap = self.radius - dist
                self.x += nx * overlap
                self.y += ny * overlap

                # Calcul du rebond (projection sur la normale)
                v_dot_n = self.vx * nx + self.vy * ny
                self.vx -= 2 * v_dot_n * nx
                self.vy -= 2 * v_dot_n * ny

                # Amortissement
                self.vx *= 0.7
                self.vy *= 0.7

                # Mettre à jour le rect
                self.rect.x = self.x - self.radius
                self.rect.y = self.y - self.radius

                break  # On ne traite qu'une collision par frame


    def draw(self, screen):

        for i, pos in enumerate(self.trail):
            alpha = int(255 * (i + 1) / len(self.trail))  # Opacité progressive
            radius = int(self.radius-5 * (i + 1) / len(self.trail))  # Taille progressive
            trail_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(trail_surf, (255, 140, 0, alpha), (radius, radius), radius)
            screen.blit(trail_surf, (pos[0] - radius, pos[1] - radius))

        screen.blit(self.image, self.rect)

