
import pygame

import math
import pygame

def draw_fleche(screen, angle, force, origin):
    fleche_image = pygame.transform.rotate(pygame.image.load("images/fleche.png").convert_alpha(), 90)
    fleche_image = pygame.transform.scale(fleche_image, (150, 150))

    # Calcul de la nouvelle taille de la flèche
    original_size = fleche_image.get_size()
    scale_factor = 1.0 + 0.01 * force
    new_width = original_size[0]
    new_height = int(original_size[1] * scale_factor)
    stretched_image = pygame.transform.scale(fleche_image, (new_width, new_height))

    rotated_image = pygame.transform.rotate(stretched_image, angle - 90)
    rotated_rect = rotated_image.get_rect()

    # Calcul du décalage pour avancer de 30 pixels dans la direction de l'angle
    offset_x = math.cos(math.radians(angle)) * 50
    offset_y = math.sin(math.radians(angle)) * -50

    # Position de départ ajustée
    start_x = origin[0] + offset_x
    start_y = origin[1] + offset_y

    # La flèche commence à cette position
    blit_pos = (start_x - rotated_rect.width / 2, start_y - rotated_rect.height / 2)

    screen.blit(rotated_image, blit_pos)

