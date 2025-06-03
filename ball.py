import pygame
import math
from settings import WIDTH, HEIGHT, GRAVITY, BALL_IMAGE


class Ball:
    def __init__(self, x, y, force, angle):
        original_image = pygame.image.load(BALL_IMAGE).convert_alpha()
        self.x = x
        self.y = y
        self.radius = 25 # rayon de la balle
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
            self.vy *= 0.98  # Diminution progressive
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
            # la ce qu'on va faire c'est verifier que notre balle n'est pas en contact avec le mur donc si elle est en contact on renvoie true et dans la fonction suivante on va déclancher le code du rebond
            if dx * dx + dy * dy < radius * radius:
                lacollision = True
            return lacollision

        for wall in walls:
            if circle_rect_collision(self.x, self.y, self.radius, wall.rect): #donc comme dit plutot si lacollisioin est renvoyée true on détecte une collision donc on lance le code pour le rebond
                # meme calcul que dans notre fonction d'avant on cherche le point le plus proche du mur
                closest_x = max(wall.rect.left, min(self.x, wall.rect.right))
                closest_y = max(wall.rect.top, min(self.y, wall.rect.bottom))
                dx = self.x - closest_x # la on va calculer le vecteur qui va du point de contact jusqu'a notre balle
                dy = self.y - closest_y

                # Calculer la distance du vecteur en question
                dist_squared = dx * dx + dy * dy
                dist = dist_squared ** 0.5  # racine carrée

                # Si la distance est nulle, on ne fait rien (on saute la collision) c'est le cas ou la balle elle touche le coin, ca fait bugger dcp on la saute
                if dist == 0:
                    continue

                # ici on normalise le vecteur pour avoir la direction du rebond en gros si la balle va vers le haut et touche le bord haut du mur, le vecteur ira vers le bas parceque quand la balle rebondira elle devra partir vers le bas aussi
                nx = dx / dist
                ny = dy / dist

                # comme la collision etait vérifiée la balle est en gros rentrée tres légerement dans le mur, dcp faut que on la décale
                decalage = self.radius - dist
                self.x += nx * decalage
                self.y += ny * decalage

                # Calcul du rebond
                v_dot_n = self.vx * nx + self.vy * ny #ca ca va etre la valeur de la vitesse de la balle dans la direction de la normale en gros à quel point la balle va "dans" le mur
                self.vx -= 2 * v_dot_n * nx #on calcule la  nouvelle vitesse et on l'enleve deux fois pour "réfléchir" la vitesse
                self.vy -= 2 * v_dot_n * ny

                # Amortissement de la vitesse sinon bah rebonds infini car pas de perte de vitesse
                self.vx *= 0.7
                self.vy *= 0.7

                # Mettre à jour la position de la balle
                self.rect.x = self.x - self.radius
                self.rect.y = self.y - self.radius



    # trainée de la balle
    def draw(self, screen):

        for i, pos in enumerate(self.trail):
            alpha = int(255 * (i + 1) / len(self.trail))  # Opacité progressive
            radius = int(self.radius-5 * (i + 1) / len(self.trail))  # Taille progressive de la trainée
            # Nouvelle surface temporaire carré plus grande que celle de la balle pour dessiner un seul point
            trail_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA) # init du canal alpha pour l'opacité
            # dessine le cercle sur trail_surf
            pygame.draw.circle(trail_surf, (255, 140, 0, alpha), (radius, radius), radius)
            # copie les pixels de trail_surf vers notre écran principal et décalage pour etre centré
            screen.blit(trail_surf, (pos[0] - radius, pos[1] - radius))
        # affichage de la balle au dessus de la trainé
        screen.blit(self.image, self.rect)

