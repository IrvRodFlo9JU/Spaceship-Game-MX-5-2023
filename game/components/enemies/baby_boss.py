
import pygame 
from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT, UP, DOWN, BABY_BOSS

class BabyBoss(Enemy):
    WIDTH = 90
    HEIGHT = 100
    SHOOTING_TIME = 45
    LIFE = 8
    SPEED_X = 1
    SPEED_Y = 2
    INTERVAL = 8
    POINTS = 5

    def __init__(self):
        self.image = BABY_BOSS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, self.SHOOTING_TIME, self.LIFE, self.POINTS)    

    def move(self):
        self.rect.y += self.SPEED_Y

        if self.move_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.left <= 0:
                self.move_x = RIGHT
                self.index = 0
        else:
            self.rect.x += self.SPEED_X
            if self.index > self.INTERVAL or self.rect.right >= SCREEN_WIDTH:
                self.move_x = LEFT
                self.index = 0
        
        self.index += 1