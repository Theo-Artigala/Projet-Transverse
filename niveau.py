from hoop import wall
from settings import *

class Niveau:
    def __init__(self, decor, hoop_pos, ball_start, murs=None):
        self.decor = decor
        self.hoop_pos = hoop_pos
        self.ball_start = ball_start
        self.murs = murs if murs is not None else []

# on def nos lvl et les murs
niveaux = [
    Niveau(
        BACKGROUND_IMAGE,
        (1000, 300),
        (100, 500),
        murs=[
            wall(100, 600, 200, 20),
            wall(400, 400, 300, 20),
        ]

    ),
    Niveau(
        BACKGROUND_IMAGE,
           (1000, 300),
           (100, 500),
        murs=[
            wall(156, 96, 80, 16),
            wall(267, 147, 72, 14),
            wall(295,62,61,16),
            wall(347,40,35,29),
        ]
    ),

]
