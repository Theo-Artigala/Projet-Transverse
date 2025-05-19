import pygame
import math
import time

# Constantes
g = 9.81  # Gravité en m/s²
WIDTH, HEIGHT = 800, 600  # Taille de la fenêtre

# Charger l'image de la balle
pygame.init()
ball_image = pygame.image.load(
    "images/boulet_de_canon.png")  # Assurez-vous que l'image est bien placée dans le dossier 'images'
ball_size = ball_image.get_rect().size  # Taille de l'image pour ajuster le positionnement


# Fonction pour calculer la position du projectile
def equation_horaire(force, angle, t):
    angle_rad = math.radians(angle)
    v0 = force  # On suppose une masse unité
    x = v0 * math.cos(angle_rad) * t
    y = v0 * math.sin(angle_rad) * t - 0.5 * g * t ** 2
    return x, y


# Simulation avec pygame
def simulate_projectile(force, angle):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    t = 0
    dt = 0.1  # Intervalle de temps

    # Position initiale
    start_x, start_y = 50, HEIGHT - 50
    trajectory = []
    ball_x, ball_y = start_x, start_y
    prev_x, prev_y = ball_x, ball_y  # Position précédente pour tracer la ligne

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((255, 255, 255))  # Fond blanc

        # Calcul des nouvelles coordonnées
        x, y = equation_horaire(force, angle, t)
        ball_x, ball_y = start_x + int(x / 100), start_y - int(y / 100)  # Adapter l'échelle du mouvement

        # Stocker la trajectoire
        if ball_y < HEIGHT - 50:
            trajectory.append((ball_x, ball_y))
        else:
            running = False

        # Afficher la trajectoire avec des lignes
        for i in range(1, len(trajectory)):
            pygame.draw.line(screen, (0, 0, 255), trajectory[i - 1], trajectory[i], 2)  # Ligne bleue

        # Dessiner l'image de la balle
        screen.blit(ball_image, (ball_x - ball_size[0] // 2, ball_y - ball_size[1] // 2))

        pygame.display.flip()
        clock.tick(60)
        t += dt

    # Attendre 1 seconde après que la balle ait touché le sol
    time.sleep(1)
    pygame.quit()


# Lancer la simulation
simulate_projectile(force=200, angle=45)


class Jeu:
    # caractéristique du jeu
    def __init__(self):
        self.sol = Sol()
        self.enJeu = False
        self.ToutDecor = pygame.sprite.Group()
        self.utiliser = {}
        self.ToutDecor.add(self.mur)

    def lancement(self):
        self.enJeu = True
        self.apparaitreEnnemi()
        self.apparaitreEnnemi()

    # Retour a l'écran d'accueil
    def gameOver(self):
        self.joueur.rect.x = 0
        self.toutEnnemi = pygame.sprite.Group()
        self.joueur.sante = self.joueur.max_sante
        self.enJeu = False

    def MAJ(self):
        # Afficher le joueur
        ecran.blit(self.joueur.image, self.joueur.rect)

        # Afficher la boule
        golfBall.draw(ecran)

        pygame.draw.line(ecran, (255, 255, 255), line[0], line[1])

        # Barre de Vie du Joueur
        self.joueur.barreDeVie(ecran)

        # Afficher le decor
        self.ToutDecor.draw(ecran)

        # Afficher l'ennemi
        self.toutEnnemi.draw(ecran)

        # Afficher le sol
        self.sol.afficherSol(ecran)

        # Recuperer les ennemis
        for ennemi in self.toutEnnemi:
            ennemi.deplacement()
            ennemi.barreDeVie(ecran)

        # Voir si on veut aller a droite ou a gauche
        if self.utiliser.get(pygame.K_RIGHT) and self.joueur.rect.x + self.joueur.rect.width < ecran.get_width():
            self.joueur.dep_droite()
        elif self.utiliser.get(pygame.K_LEFT) and self.joueur.rect.x > 0:
            self.joueur.dep_gauche()

    def apparaitreEnnemi(self):
        ennemi = Ennemi(self)
        self.toutEnnemi.add(ennemi)

    # collisionn avec les ennemi
    def verifCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


class ball(object):
    def __init__(self, x, y, radius, color):
        self.joueur = Joueur(self)
        self.x = self.joueur.rect.x + 150
        self.y = self.joueur.rect.y + 80
        self.radius = radius
        self.color = color
        self.toutBoule = pygame.sprite.Group()

    def draw(self, ecran):
        pygame.draw.circle(ecran, (0, 0, 0), (self.x + 150, self.y + 80), self.radius)
        pygame.draw.circle(ecran, self.color, (self.x + 150, self.y + 80), self.radius - 1)

    def dep(self):
        # Toucher et supprimer la boule l'ennemeie
        for ennemie in self.joueur.jeu.verifCollision(self, self.joueur.jeu.toutEnnemie):
            ennemie.degats(self.joueur.degat)
            self.toutBoule.remove(self)

    @staticmethod
    def ballPath(startx, starty, power, angle, time):
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time) ** 2) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)

        return (newx, newy)


def findAngle(pos):
    sX = golfBall.x
    sY = golfBall.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle


golfBall = ball(500, 494, 5, (255, 255, 255))
x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False
# Créer une fenetre
pygame.init()
pygame.display.set_caption("Jeu de l'arché")
ecran = pygame.display.set_mode((1080, 720))
running = True

# Mettre un arrière plan
fond = pygame.image.load("bg.jpg")

# Image d'accueil
accueil = pygame.image.load("banner.png")
accueil = pygame.transform.scale(accueil, (500, 500))
accueil_rect = accueil.get_rect()
accueil_rect.x = math.ceil(ecran.get_width() / 4)

# Bouton de lancement
bouton = pygame.image.load("button.png")
bouton = pygame.transform.scale(bouton, (400, 150))
bouton_rect = bouton.get_rect()
bouton_rect.x = math.ceil(ecran.get_width() / 3.33)
bouton_rect.y = math.ceil(ecran.get_height() / 1.5)

# Charger le jeu
jeu = Jeu()

# Maintenir la fentre ouverte
while running:
    # Afficher le jeu
    ecran.blit(fond, (0, -200))

    # Vérifier si le jeu a commencer
    if jeu.enJeu:
        jeu.MAJ()

    # Vérifier si le jeu n'a pas commencer
    else:
        # Ecran d'accueil
        ecran.blit(bouton, bouton_rect)
        ecran.blit(accueil, accueil_rect)

    # Eviter que la fenetre se ferme automatiquement
    pygame.display.flip()
    pos = pygame.mouse.get_pos()
    line = [(golfBall.x + 150, golfBall.y + 80), pos]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu ")

        # Detecter si un joueur utilise une touche du clavier
        elif event.type == pygame.KEYDOWN:
            jeu.utiliser[event.key] = True


        elif event.type == pygame.KEYUP:
            jeu.utiliser[event.key] = False

        # Detecter si le joueur clique sur le bouton jouer et si oui lancer le jeu
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_rect.collidepoint(event.pos):
                jeu.lancement()
            if shoot == False:
                shoot = True
                x = golfBall.x
                y = golfBall.y
                time = 0
                power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][0]) ** 2) / 8
                angle = findAngle(pos)

    if shoot:
        if golfBall.y < 500 - golfBall.radius:
            time += 0.5
            po = ball.ballPath(x, y, power, angle, time)
            golfBall.x = po[0]
            golfBall.y = po[1]
        else:
            shoot = False
            golfBall.y = 494