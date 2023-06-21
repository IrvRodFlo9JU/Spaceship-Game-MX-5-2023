
import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_PLAYER_B


class BulletPlayerBasic(Bullet):
    WIDTH = 9
    HEIGHT = 30
    SPEED = 18
    DAMAGE = 1

    def __init__(self, center):
        self.image = BULLET_PLAYER_B
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.player_bullet = True
        super().__init__(self.image, center, self.DAMAGE, self.player_bullet)

    def move(self):
        self.rect.y -= self.SPEED
    
