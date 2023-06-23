
import pygame
from game.utils.constants import BLUE_EXPLOSION
from game.components.explosions.explosion import Explosion

class ExplosionBuff(Explosion):
    def __init__(self, width, height, center):
        self.image = BLUE_EXPLOSION
        super().__init__(self.image, width, height, center)
