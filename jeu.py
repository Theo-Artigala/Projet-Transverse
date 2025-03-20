import pygame

pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Tir dans les Cerceaux")

# Charger les images
background = pygame.image.load("images/bg.jpg")
canon_img = pygame.image.load("images/canon.png")
balle_img = pygame.image.load("images/boulet_de_canon.png")
cerceau_img = pygame.image.load("images/hoop.png")


# Classes du jeu
class Balle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.lancee = False

    def lancer(self, angle, puissance):
        self.vx = puissance * pygame.math.cos(angle)
        self.vy = -puissance * pygame.math.sin(angle)
        self.lancee = True

    def update(self):
        if self.lancee:
            self.x += self.vx
            self.y += self.vy
            self.vy += 0.5  # Gravité

    def draw(self):
        screen.blit(balle_img, (self.x, self.y))


def lancer_jeu():
    running = True
    balle = Balle(100, 500)

    while running:
        screen.blit(background, (0, 0))
        balle.update()
        balle.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

        pygame.display.flip()


if __name__ == "__main__":
    lancer_jeu()
