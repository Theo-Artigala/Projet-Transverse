from hoop import wall
from settings import *

class Niveau:
    def __init__(self, decor, hoop_pos, ball_start, murs=None):
        self.decor = decor
        self.hoop_pos = hoop_pos
        self.ball_start = ball_start
        self.murs = murs if murs is not None else []

# Définition des niveaux avec murs
niveaux = [
    Niveau(
        BACKGROUND_IMAGE,
        (600, 300),
        (100, 500),
        murs=[
            wall(100, 600, 200, 20),
            wall(400, 400, 300, 20),
        ]
    ),
    # autres niveaux...
]
