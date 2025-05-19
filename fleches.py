
import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

fleche_image = pygame.image.load("images/boulet_de_canon.png")

def draw_fleche(angle, force):

    original_size = fleche_image.get_size()
    scale_factor = 1.0 + 0.01 * force
    new_width = original_size[0]
    new_height = int(original_size[1] * scale_factor)
    stretched_image = pygame.transform.scale(fleche_image, (new_width, new_height))
    rotated_image = pygame.transform.rotate(stretched_image, -angle)
    rotated_rect = rotated_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(rotated_image, rotated_rect)

running = True
force = 10
angle = 0
step = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if step == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    force += 5
                elif event.key == pygame.K_DOWN:
                    force = max(0, force - 5)
                elif event.key == pygame.K_SPACE:
                    step = 2


        elif step == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    angle -= 5
                elif event.key == pygame.K_RIGHT:
                    angle += 5
                elif event.key == pygame.K_SPACE:
                    print(f"Lancement ! Force: {force}, Angle: {angle}")

                    step = 1
                    force = 10
                    angle = 0


    screen.fill((255, 255, 255))
    draw_fleche(angle, force)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

