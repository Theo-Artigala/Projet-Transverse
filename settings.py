# settings.py
import pygame
pygame.mixer.init()

WIDTH = 1366
HEIGHT = 768
FPS = 60
GRAVITY = 1
SCORE = 0
NBR_DESSAI = 0
BACKGROUND_IMAGE = "images/bg2.jpg"
BALL_IMAGE = "images/balle.png"
HOOP_IMAGE = "images/hoop.png"
MENU_PRINCIPAL = "images/menu.png"
IMAGE_BOUTON_START = "images/bouton_start.png"
END_SCREEN = "images/endscreen.png"
IMAGE_BOUTON_RESTART = "images/bouton_restart.png"
IMAGE_BOUTON_QUIT = "images/bouton_quit.png"
niveau_actuel = 0
son = pygame.mixer.Sound('sons/death_sound.wav')


def lines_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # Vérifie si deux segments de ligne se croisent
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:
        return False  # Parallèles ou colinéaires sans intersection
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    return 0 <= ua <= 1 and 0 <= ub <= 1


def line_intersects_rect(x1, y1, x2, y2, rect):
    # Vérifie si la ligne entre (x1, y1) et (x2, y2) intersecte le rectangle
    rect_lines = [
        ((rect.left, rect.top), (rect.right, rect.top)),  # haut
        ((rect.right, rect.top), (rect.right, rect.bottom)),  # droite
        ((rect.right, rect.bottom), (rect.left, rect.bottom)),  # bas
        ((rect.left, rect.bottom), (rect.left, rect.top))  # gauche
    ]
    for (ax, ay), (bx, by) in rect_lines:
        if lines_intersect(x1, y1, x2, y2, ax, ay, bx, by):
            return True
    return False