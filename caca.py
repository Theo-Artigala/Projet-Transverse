import pygame
from pygame.locals import *
import math

# Initialisation de Pygame
pygame.init()
horloge = pygame.time.Clock()

# Chargement du fond
fond = pygame.image.load("images/tennis_court.png")
fenetre_size = fond.get_rect().size
fenetre = pygame.display.set_mode(fenetre_size)
fenetre_rect = pygame.Rect((0, 0), fenetre_size)
fond = fond.convert()

# Constantes
fps = 120  # Taux de rafraîchissement (fps = frame per second)

# Demander à l'utilisateur un angle et une force de lancement
angle_deg = float(input("Entrez l'angle de lancement (en degrés, vers la droite) : "))
force = float(input("Entrez la force de lancement (en Newton) : "))

# Convertir l'angle en radians
angle_rad = math.radians(angle_deg)

# Calculer la vitesse initiale en fonction de la force et de l'angle
# On suppose que la force est utilisée pour calculer une vitesse initiale de 10 m/s à l'angle donné
vitesse_initiale = force  # Par exemple, la force est prise directement comme la vitesse initiale en m/s
vx = vitesse_initiale * math.cos(angle_rad)  # Composante horizontale de la vitesse
vy = -vitesse_initiale * math.sin(angle_rad)  # Composante verticale de la vitesse (négatif car vers le bas)

# La balle
ball = {"file": "images/balle.png",  # Le fichier 'image'
        "p": [200, 500],  # Position initiale
        "v": [vx, vy],  # Vitesse initiale calculée
        "m": 0.1,  # Masse
        "r": 0  # Rayon initial
        }

# Chargement et initialisation de la balle
def init_objet(obj):
    objet = pygame.image.load(obj["file"])
    obj["r"] = objet.get_rect().size[0] / 2  # Rayon de la balle
    return objet

# Objet pygame pour la balle
ball["pg"] = init_objet(ball).convert()

# Fonction de calcul des forces
def calc_force(objet, position_systeme_exterieur, **parametres):
    # Par exemple, force gravitationnelle
    g = 9.81  # Accélération due à la gravité (m/s^2)
    Fx = 0  # Pas de force horizontale dans cet exemple
    Fy = objet["m"] * g  # Force verticale (poids de la balle)

    return Fx, Fy

# Boucle principale du jeu
continuer = True
while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = False

    # Calcul des forces
    Fx, Fy = calc_force(ball, ball["p"])

    # Mise à jour de la vitesse en fonction des forces
    dt = 3 / fps  # Intervalle de temps entre chaque frame
    ax = Fx / ball["m"]  # Accélération en x
    ay = Fy / ball["m"]  # Accélération en y

    ball["v"][0] += ax * dt  # Mise à jour de la vitesse horizontale
    ball["v"][1] += ay * dt  # Mise à jour de la vitesse verticale

    # Calcul de la nouvelle position
    ball["p"][0] += ball["v"][0] * dt  # Nouvelle position horizontale
    ball["p"][1] += ball["v"][1] * dt  # Nouvelle position verticale

    # Gestion des collisions avec le sol (rebond)
    if ball["p"][1] + ball["r"] > fenetre_size[1]:  # Collision avec le bas de l'écran
        ball["p"][1] = fenetre_size[1] - ball["r"]  # Empêcher la balle de sortir de l'écran
        ball["v"][1] = -ball["v"][1] * 0.9  # Rebonds avec un peu d'atténuation (réduction de la vitesse verticale)

    # Re-collage des éléments
    fenetre.blit(fond, (0, 0))  # Re-dessiner le fond
    fenetre.blit(ball["pg"], ball["p"])  # Dessiner la balle à sa nouvelle position

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limiter la fréquence de rafraîchissement
    horloge.tick(fps)

pygame.quit()
