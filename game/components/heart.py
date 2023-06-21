
from game.utils.constants import HEART_LIFE
import pygame

class Heart:
    WIDHT = 20
    HEIGHT = 20
    POS_X = 100
    POS_Y = 40

    def __init__(self, pos_x, pos_y):
        self.image = HEART_LIFE
        self.image = pygame.transform.scale(self.image, (self.WIDHT, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)