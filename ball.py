# ball.py
import pygame
import math
from settings import GRAVITY, BALL_IMAGE

class Ball:
    def __init__(self, x, y, speed):
        self.image = pygame.image.load(BALL_IMAGE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.angle = math.radians(45)  # Angle fixe pour l'instant
        self.vel_x = math.cos(self.angle) * self.speed
        self.vel_y = -math.sin(self.angle) * self.speed

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.vel_y += GRAVITY * 0.1  # Appliquer la gravité

    def draw(self, screen):
        screen.blit(self.image, self.rect)
