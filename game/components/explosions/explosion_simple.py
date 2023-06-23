
import pygame
from game.utils.constants import EXPLOSION
from game.components.explosions.explosion import Explosion

class ExplosionSimple(Explosion):
    def __init__(self, width, height, center):
        self.image = EXPLOSION
        super().__init__(self.image, width, height, center)