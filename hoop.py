# hoop.py
import pygame
import math
from settings import HOOP_IMAGE


class Hoop:
    def __init__(self, x, y):
        original_image = pygame.transform.rotate(pygame.image.load(HOOP_IMAGE).convert_alpha(), 105)
        self.x = x
        self.y = y
        self.radius = 250

        # Paramètres pour la collision en forme d'anneau
        self.ring_thickness = 20  # Épaisseur de l'anneau du cerceau
        self.ring_radius = 65  # Rayon de l'anneau (à ajuster selon l'image)

        self.image = pygame.transform.scale(original_image, (self.radius * 2, self.radius * 2))
        self.rect = self.image.get_rect(center=(x, y))

    def check_collision(self, ball):
        # Calculer la distance entre le centre du cerceau et le centre de la balle
        dx = self.rect.centerx - ball.rect.centerx
        dy = self.rect.centery - ball.rect.centery
        distance = math.sqrt(dx * dx + dy * dy)

        return abs(distance - self.ring_radius) < self.ring_thickness + ball.radius

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)

    def check_collision(self, ball):
        return self.rect.colliderect(ball.rect)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
