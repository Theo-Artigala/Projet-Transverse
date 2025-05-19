# game.py
import pygame
from settings import WIDTH, HEIGHT, BACKGROUND_IMAGE
from player import Player
from ball import Ball
from hoop import Hoop

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jeu de Tir dans les Cerceaux")
        self.clock = pygame.time.Clock()
        self.running = True

        # Charger les éléments du jeu
        self.background = pygame.image.load(BACKGROUND_IMAGE)
        self.player = Player()
        self.balls = []
        self.hoops = [Hoop(700, 300), Hoop(900, 450)]  # Cerceaux placés à différentes hauteurs

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Tirer avec la barre espace
                    self.balls.append(self.player.shoot())

    def update(self):
        for ball in self.balls:
            ball.update()
            for hoop in self.hoops:
                if hoop.check_collision(ball):
                    print("Touché !")
                    self.balls.remove(ball)
                    break  # Évite la suppression multiple

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)

        for ball in self.balls:
            ball.draw(self.screen)
        for hoop in self.hoops:
            hoop.draw(self.screen)

        pygame.display.flip()
