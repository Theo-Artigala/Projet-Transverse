import math

def calcul_trajectoire(x0, y0, angle_deg, vitesse, t, g=9.81):
    angle_rad = math.radians(angle_deg)
    vx = vitesse * math.cos(angle_rad)
    vy = vitesse * math.sin(angle_rad)
    x = x0 + vx * t
    y = y0 - vy * t + 0.5 * g * t**2
    return x, y
