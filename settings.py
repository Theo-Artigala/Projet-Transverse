
import pygame
pygame.mixer.init()

WIDTH = 1366
HEIGHT = 768
FPS = 60
GRAVITY = 1
SCORE = 0
NBR_DESSAI = 0
BACKGROUND_IMAGE = "images/bg.png"
BALL_IMAGE = "images/balle.png"
HOOP_IMAGE = "images/hoop.png"
MENU_PRINCIPAL = "images/menu.png"
IMAGE_BOUTON_START = "images/bouton_start.png"
END_SCREEN = "images/endscreen.png"
IMAGE_BOUTON_MENU = "images/menu-button.png"
IMAGE_BOUTON_QUIT = "images/bouton_quit.png"
niveau_actuel = 0
son = pygame.mixer.Sound('sons/death_sound.wav')

