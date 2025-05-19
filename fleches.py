def draw_arrow(screen, origin, angle_deg, length=50):
    import math, pygame
    angle_rad = math.radians(angle_deg)
    end_pos = (
        origin[0] + length * math.cos(angle_rad),
        origin[1] - length * math.sin(angle_rad)
    )
    pygame.draw.line(screen, (255, 0, 0), origin, end_pos, 3)
    pygame.draw.circle(screen, (255, 0, 0), end_pos, 5)
