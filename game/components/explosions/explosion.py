
import pygame
from game.utils.constants import EXPLOSION

class Explosion:
    DURATION = 7

    def __init__(self, image,width, height, center):
        self.width = width
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.is_alive = True
        self.count = 0

    def update(self):
        if self.count == self.DURATION:
            self.is_alive = False
        self.count += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)