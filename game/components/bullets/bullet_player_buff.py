
import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_PLAYER_B


class BulletPlayerBuff(Bullet):
    WIDTH = 15
    HEIGHT = 90
    SPEED = 25
    DAMAGE = 5

    def __init__(self, center):
        self.image = BULLET_PLAYER_B
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.player_bullet = True
        super().__init__(self.image, center, self.DAMAGE, self.player_bullet)

    def move(self):
        self.rect.y -= self.SPEED
    
