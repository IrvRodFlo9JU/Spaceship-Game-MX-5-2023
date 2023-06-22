
import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY_B, SCREEN_HEIGHT, BULLET_BABY_BOSS, SCREEN_WIDTH, LEFT, RIGHT

class BulletBabyBoss(Bullet):
    WIDTH = 30
    HEIGHT = 9
    SPEED = 25
    DAMAGE = 2

    def __init__(self, center, direction):
        self.image = BULLET_ENEMY_B
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.player_bullet = False
        self.direction = direction
        super().__init__(self.image, center, self.DAMAGE, self.player_bullet)

    def move(self):
        if self.direction == RIGHT:
            self.rect.x += self.SPEED
        else: 
            self.rect.x -= self.SPEED