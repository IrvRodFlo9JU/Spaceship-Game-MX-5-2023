
import pygame
from game.utils.constants import ASTEROID_ENEMY
from game.components.asteroids.asteroid import Asteroid

class AsteroidEnemy(Asteroid):
    WIDTH = 40
    HEIGHT = 40
    DAMAGE = 1
    SPEED = 12

    def __init__(self):
        self.image = ASTEROID_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, self.DAMAGE, self.SPEED)