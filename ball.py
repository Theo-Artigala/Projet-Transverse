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
        self.max_bounces = 6
        self.trail = []  # Liste des anciennes positions [(x, y), ...]
        self.max_trail_length = 15  # Nombre de points dans la traînée

    def update(self):
        # Mise à jour des positions
        self.vy += GRAVITY
        self.x += self.vx
        self.y += self.vy

        # Rebond sur le sol
        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy * 0.7  # amortissement
            self.vx *= 0.9
            self.bounces += 1
            if self.bounces >= self.max_bounces:
                self.vx = 0
                self.vy = 0

        # Rebond sur les murs (gauche et droite)
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx * 0.7
        elif self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
            self.vx = -self.vx * 0.7
        self.rect.center = (self.x, self.y)

        self.trail.append((self.x, self.y))
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)

    def draw(self, screen):

        for i, pos in enumerate(self.trail):
            alpha = int(255 * (i + 1) / len(self.trail))  # Opacité progressive
            radius = int(self.radius-5 * (i + 1) / len(self.trail))  # Taille progressive
            trail_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(trail_surf, (255, 140, 0, alpha), (radius, radius), radius)
            screen.blit(trail_surf, (pos[0] - radius, pos[1] - radius))

        screen.blit(self.image, self.rect)

