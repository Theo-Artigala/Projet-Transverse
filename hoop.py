# hoop.py
import pygame
from settings import HOOP_IMAGE


class Hoop:
    def __init__(self, x, y):
        original_image = pygame.transform.rotate(pygame.image.load(HOOP_IMAGE).convert_alpha(),105)
        self.x = x
        self.y = y
        self.radius = 250
        self.image = pygame.transform.scale(original_image, (self.radius * 2, self.radius * 2))
        self.rect = self.image.get_rect(center=(x, y))

    def check_collision(self, ball):
        return self.rect.colliderect(ball.rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 255)

    def check_collision(self, ball):
        return self.rect.colliderect(ball.rect)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)