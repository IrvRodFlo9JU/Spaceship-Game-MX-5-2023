
from game.utils.constants import BULLET_ENEMY_BASIC, BULLET_PLAYER_BASIC, BULLET_PLAYER_BUFF, BULLET_BABY_BOSS, LEFT, RIGHT
from game.components.bullets.bullet_enemy_basic import BulletEnemyBasic
from game.components.bullets.bullet_player_basic import BulletPlayerBasic
from game.components.bullets.bullet_player_buff import BulletPlayerBuff
from game.components.bullets.bullet_baby_boss import BulletBabyBoss

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemy_handler, explosion_handler):
        for bullet in self.bullets:
            bullet.update(enemy_handler, explosion_handler, player)
            if not bullet.is_alive:
                self.bullets.remove(bullet)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet_type, center):
        if bullet_type == BULLET_ENEMY_BASIC:
            self.bullets.append(BulletEnemyBasic(center))
        elif bullet_type == BULLET_PLAYER_BASIC:
            self.bullets.append(BulletPlayerBasic(center))
        elif bullet_type == BULLET_PLAYER_BUFF:
            self.bullets.append(BulletPlayerBuff(center))
        elif bullet_type == BULLET_BABY_BOSS:
            self.bullets.append(BulletBabyBoss(center, LEFT))
            self.bullets.append(BulletBabyBoss(center, RIGHT))

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def reset(self):
        self.bullets.clear()