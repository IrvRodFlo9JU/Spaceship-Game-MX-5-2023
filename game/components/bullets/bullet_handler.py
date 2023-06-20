
from game.utils.constants import BULLET_ENEMY_BASIC
from game.components.bullets.bullet_enemy_basic import BulletEnemyBasic

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player):
        for bullet in self.bullets:
            bullet.update(player)
            if not bullet.is_alive:
                self.bullets.remove(bullet)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet_type, center):
        if bullet_type == BULLET_ENEMY_BASIC:
            self.bullets.append(BulletEnemyBasic(center))

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)