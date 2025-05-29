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
           (100, 500),
        murs=[
            wall(400, 530, 169, 43),
            wall(611, 397, 47, 209),
            wall(728,186,169,48),
            wall(731,435,167,40),
        ]
    ),
    Niveau(
        BACKGROUND_IMAGE,
           (1081, 451),
           (100, 500),
        murs= [
            wall(357,466,187,46),
            wall(447,411,52,238),
            wall(722,391,204,43),
            wall(862,593,56,291),
        ]
    )
]
