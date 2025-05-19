import pygame
from pygame.locals import *
import math

# Initialisation de Pygame
pygame.init()
horloge = pygame.time.Clock()

# Fenêtre en mode plein écran fenêtré
largeur, hauteur = 1200, 700  # Taille de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur), pygame.RESIZABLE)

# Chargement du fond (terrain)
fond = pygame.image.load("images/tennis_court.png")
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Constantes
fps = 120  # Taux de rafraîchissement (fps)

# Paramètres initiaux
angle_deg = 45  # Angle initial en degrés
force = 10  # Force initiale en Newton
vitesse = force  # La vitesse initiale de la balle

# Fonction pour afficher du texte
def afficher_texte(texte, position, taille=30):
    font = pygame.font.Font(None, taille)
    texte_surface = font.render(texte, True, (255, 255, 255))
    fenetre.blit(texte_surface, position)

# Sélection des paramètres
def selection_parametres():
    global angle_deg, force, vitesse
    saisie = True
    while saisie:
        fenetre.blit(fond, (0, 0))  # Afficher le terrain
        afficher_texte(f"Angle: {angle_deg}° (flèches haut/bas)", (50, 50))
        afficher_texte(f"Force: {force} N (flèches gauche/droite)", (50, 100))
        afficher_texte(f"Vitesse: {vitesse} m/s (W/S)", (50, 150))
        afficher_texte("Appuyez sur 'Entrée' pour démarrer", (50, 200))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    angle_deg = min(angle_deg + 5, 90)
                elif event.key == K_DOWN:
                    angle_deg = max(angle_deg - 5, 0)
                elif event.key == K_LEFT:
                    force = max(force - 10, 0)
                elif event.key == K_RIGHT:
                    force = max(force + 10, 0)
                elif event.key == K_w:
                    vitesse += 10
                elif event.key == K_s:
                    vitesse = max(vitesse - 10, 0)
                elif event.key == K_RETURN:
                    return True
    return False

# Fonction de calcul des forces
def calc_force(objet, **parametres):
    g = 9.81
    Fx, Fy = 0, objet["m"] * g  # Force gravité
    return Fx, Fy

# Simulation
def simulation():
    angle_rad = math.radians(angle_deg)
    vx = vitesse * math.cos(angle_rad)
    vy = -vitesse * math.sin(angle_rad)

    ball = {
        "file": "images/balle.png",
        "position": [50, hauteur - 50],  # Position en bas à gauche
        "vitesse": [vx, vy],
        "m": 0.1,
        "r": 0,
        "count": 10,
        "gagné":False
    }

    # Chargement et initialisation de la balle
    def init_objet(obj):
        objet = pygame.image.load(obj["file"])
        objet = pygame.transform.scale(objet, (30, 30))  # Taille fixe
        obj["r"] = objet.get_rect().size[0] / 2
        return objet

    ball["pg"] = init_objet(ball).convert_alpha()

    # Boucle du jeu
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer = False  # Quitter avec Échap
            if ball["vitesse"] == 0 : continuer = False


        # Calcul des forces
        Fx, Fy = calc_force(ball)

        # Mise à jour de la vitesse
        dt = 3 / fps
        ax = Fx / ball["m"]
        ay = Fy / ball["m"]
        # inverse la gravité, jsp pk par contre : ball["v"][1] -= 1
        if ball["vitesse"][0] > 0:
            ball["vitesse"][0] -= 0.01

        ball["vitesse"][0] += ax * dt
        ball["vitesse"][1] += ay * dt

        # Mise à jour de la position
        ball["position"][0] += ball["vitesse"][0] * dt
        ball["position"][1] += ball["vitesse"][1] * dt

        # Collision avec les murs
        if ball["position"][0] - ball["r"] < 0:  # Mur gauche
            ball["position"][0] = ball["r"]
            ball["vitesse"][0] = -ball["vitesse"][0] * 0.8  # Atténuation
        if ball["position"][0] + ball["r"] > largeur:  # Mur droit
            ball["position"][0] = largeur - ball["r"]
            ball["vitesse"][0] = -ball["vitesse"][0] * 0.8
        if ball["position"][1] - ball["r"] < 0:  # Plafond
            ball["position"][1] = ball["r"]
            ball["vitesse"][1] = -ball["vitesse"][1] * 0.8
        if ball["position"][1] + ball["r"] > hauteur:  # Sol
            ball["position"][1] = hauteur - ball["r"]
            ball["vitesse"][1] = -ball["vitesse"][1] * 0.8
            ball["count"] -=1
            if ball["count"] == 0:
                ball["vitesse"][0] = 0

        # Affichage
        fenetre.blit(fond, (0, 0))
        fenetre.blit(ball["pg"], (ball["position"][0] - ball["r"], ball["position"][1] - ball["r"]))
        pygame.display.flip()

        horloge.tick(fps)

    pygame.quit()

# Exécution
if selection_parametres():
    simulation()
