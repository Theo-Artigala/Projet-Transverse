
import pygame

def draw_fleche(screen, angle, force, origin):
    fleche_image = pygame.image.load("images/boulet_de_canon.png")

    original_size = fleche_image.get_size()
    scale_factor = 1.0 + 0.01 * force
    new_width = original_size[0]
    new_height = int(original_size[1] * scale_factor)
    stretched_image = pygame.transform.scale(fleche_image, (new_width, new_height))

    rotated_image = pygame.transform.rotate(stretched_image, angle-90)
    rotated_rect = rotated_image.get_rect(center=origin)
    screen.blit(rotated_image, rotated_rect)
