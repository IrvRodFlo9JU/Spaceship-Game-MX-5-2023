import pygame
import random 
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT, UP, DOWN

class Enemy_2(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_X = 4
    SPEED_UP = 1
    SPEED_DOWN = 4
    INTERVAL_X = [50, 70, 80, 100, 150]
    INTERVAL_Y = [20, 40, 50, 60, 75]
    MOV_Y = [UP, DOWN]

    def __init__(self):
        self.image = ENEMY_2
        self.index_up = 0
        self.move_y = DOWN
        self.interval_x = random.choice(self.INTERVAL_X)
        self.interval_y = random.choice(self.INTERVAL_Y)
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
    
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


        
