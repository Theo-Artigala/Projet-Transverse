import pygame
import math
from settings import WIDTH, HEIGHT, GRAVITY
from jeu import *

class Ball:
    def __init__(self, x, y, force, angle):
        self.x = x
        self.y = y
        self.radius = 15
        self.color = (255, 0, 0)
        self.force = force
        self.angle = math.radians(angle)
        self.vx = force * math.cos(self.angle)
        self.vy = -force * math.sin(self.angle)
        self.bounces = 0
        self.max_bounces = 3
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def update(self, walls):
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

        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        for wall in walls:
            if wall.check_collision(self):
                # Rebond simple : inverser vx ou vy selon le côté
                if abs(self.rect.right - wall.rect.left) < 10 and self.vx > 0:
                    self.x = wall.rect.left - self.radius * 2
                    self.vx = -self.vx * 0.7
                elif abs(self.rect.left - wall.rect.right) < 10 and self.vx < 0:
                    self.x = wall.rect.right
                    self.vx = -self.vx * 0.7
                elif abs(self.rect.bottom - wall.rect.top) < 10 and self.vy > 0:
                    self.y = wall.rect.top - self.radius * 2
                    self.vy = -self.vy * 0.7
                    self.vx *= 0.9
                    self.bounces += 1
                elif abs(self.rect.top - wall.rect.bottom) < 10 and self.vy < 0:
                    self.y = wall.rect.bottom
                    self.vy = -self.vy * 0.7

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
