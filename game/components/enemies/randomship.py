import pygame
import random 
from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT, UP, DOWN, RANDOMSHIP

class Randomship(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_X = 4
    SPEED_UP = 1
    SPEED_DOWN = 4
    INTERVAL_X = [50, 70, 80, 100, 150]
    INTERVAL_Y = [20, 40, 50, 60, 75]
    MOV_Y = [UP, DOWN]
    SHOOTING_INTERVALS = [20, 25, 30, 15]
    LIFE = 2
    POINTS = 2

    def __init__(self):
        self.image = RANDOMSHIP
        self.index_up = 0
        self.move_y = DOWN
        self.interval_x = random.choice(self.INTERVAL_X)
        self.interval_y = random.choice(self.INTERVAL_Y)
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.shooting_interval = random.choice(self.SHOOTING_INTERVALS)
        super().__init__(self.image, self.shooting_interval, self.LIFE, self.POINTS)
    
    def move(self):
        if self.move_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.interval_x:
                self.move_x = random.choice(self.MOV_X)
                self.index = 0
                self.interval_x = random.choice(self.INTERVAL_X)

            if self.rect.left <= 0:
                self.move_x = RIGHT
                self.index = 0
                self.interval_x = random.choice(self.INTERVAL_X)
        else:
            self.rect.x += self.SPEED_X
            if self.index > self.interval_x:
                self.move_x = random.choice(self.MOV_X)
                self.index = 0
                self.interval_x = random.choice(self.INTERVAL_X)
            
            if self.rect.right >= SCREEN_WIDTH:
                self.move_x = LEFT
                self.index = 0
                self.interval_x = random.choice(self.INTERVAL_X)

        if self.move_y == UP:
            self.rect.y -= self.SPEED_UP
            if self.index_up > self.interval_y:
                self.move_y = random.choice(self.MOV_Y)
                self.index_up = 0
                self.interval_y = random.choice(self.INTERVAL_Y)
        else:
            self.rect.y += self.SPEED_DOWN
            if self.index_up > self.interval_y:
                self.move_y = random.choice(self.MOV_Y)
                self.index_up = 0     
                self.interval_y = random.choice(self.INTERVAL_Y)  

        if self.rect.top <= 0:
            self.move_y = DOWN

        self.index_up += 1
        self.index += 1


        
