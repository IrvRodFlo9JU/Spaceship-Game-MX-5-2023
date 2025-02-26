
import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY_B, SCREEN_HEIGHT

class BulletEnemyBasic(Bullet):
    WIDTH = 9
    HEIGHT = 30
    SPEED = 18
    DAMAGE = 1

    def __init__(self, center):
        self.image = BULLET_ENEMY_B
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.player_bullet = False
        super().__init__(self.image, center, self.DAMAGE, self.player_bullet)

    def move(self):
        self.rect.y += self.SPEED
