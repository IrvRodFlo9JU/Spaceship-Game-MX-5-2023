import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import SHIP


class Ship(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SHOOTING_TIME = 30
    LIFE = 1

    def __init__(self):
        self.image = SHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, self.SHOOTING_TIME,self.LIFE)