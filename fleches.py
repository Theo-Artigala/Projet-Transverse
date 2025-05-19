import pygame


WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

fleche_image = pygame.image.load("images/boulet_de_canon.png")


def fleche_direction(angle):

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                #calcul des nouvelles coordonnées de la flèche

                if event.key == pygame.K_LEFT:
                    angle = angle - 5

                elif event.key == pygame.K_RIGHT:
                    angle = angle + 5


        screen.fill((255, 255, 255))

        # Rotation de l'image
        rotated_image = pygame.transform.rotate(fleche_image, -angle)
        rotated_rect = rotated_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Affichage
        screen.blit(rotated_image, rotated_rect)
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()

    return angle

def fleche_force(force):
    original_size = fleche_image.get_size()
    scale_factor = 1.0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    force = force - 5
                    scale_factor -= 0.1

                elif event.key == pygame.K_UP:
                    force = force + 5
                    scale_factor += 0.1

        new_width = int(original_size[0] * scale_factor)
        new_height = original_size[1]  # On garde la hauteur constante
        stretched_image = pygame.transform.scale(fleche_image, (new_width, new_height))

        # Centrer l'image
        stretched_rect = stretched_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Affichage
        screen.fill((255, 255, 255))
        screen.blit(stretched_image, stretched_rect)
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()

    return force

angle=fleche_direction(0)
print(angle)


force=fleche_force(10)
print(force)

