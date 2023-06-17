import random
import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT

class Enemy:
    Y_POS = -5
    X_POS_LIST = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]
    SPEED_X = 5
    SPEED_Y = 3
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 100

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.move_x = random.choice(self.MOV_X)
        self.is_alive = True
        self.index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.rect.top >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()

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
        

