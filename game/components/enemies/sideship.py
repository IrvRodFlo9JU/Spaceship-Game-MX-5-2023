
import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import SIDESHIP, LEFT, RIGHT, SCREEN_WIDTH

class Sideship(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SHOOTING_TIME = 40
    LIFE = 5
    SPEED_X = 10
    SPEED_Y = 3
    POINTS = 2

    def __init__(self):
        self.image = SIDESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, self.SHOOTING_TIME, self.LIFE, self.POINTS)
    
    def move(self):
        self.rect.y += self.SPEED_Y

        if self.move_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.rect.left <= 0:
                self.move_x = RIGHT

        else:
            self.rect.x += self.SPEED_X
            if self.rect.right >= SCREEN_WIDTH:
                self.move_x = LEFT
