# player.py
import pygame
from settings import BALL_IMAGE, BALL_SPEED
from ball import Ball

class Player:
    def __init__(self):
        self.image = pygame.image.load("images/canon.png")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 500

    def shoot(self):
        return Ball(self.rect.centerx + 50, self.rect.centery - 20, BALL_SPEED)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
