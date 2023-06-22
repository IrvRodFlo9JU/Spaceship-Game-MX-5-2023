
import pygame
from game.utils.constants import ASTEROID_BUFF
from game.components.asteroids.asteroid import Asteroid

class AsteroidBuff(Asteroid):
    WIDTH = 40
    HEIGHT = 40
    DAMAGE = -1
    SPEED = 8

    def __init__(self):
        self.image = ASTEROID_BUFF
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, self.DAMAGE, self.SPEED)