from settings import BACKGROUND_IMAGE


class Niveau:
    def __init__(self, decor, hoop_pos, ball_start, force, angle):
        self.decor = decor
        self.hoop_pos = hoop_pos
        self.ball_start = ball_start
        self.force = force
        self.angle = angle


niveaux = [
    Niveau(BACKGROUND_IMAGE, (600, 300), (100, 500), 20, 45),
    Niveau("niveau2.png", (700, 200), (100, 500), 22, 40),
    Niveau("niveau3.png", (550, 250), (150, 520), 18, 55),
]
