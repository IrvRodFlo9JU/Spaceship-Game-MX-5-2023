
import random
from game.components.enemies.ship import Ship
from game.components.enemies.randomship import Randomship
from game.utils.constants import ENEMY_SHIP, ENEMY_RANDOMSHIP


class EnemyHandler:

    ENEMIES = [ENEMY_SHIP, ENEMY_RANDOMSHIP]

    def __init__(self):
        self.enemies = []
        self.enemies_destroyed = 0
    
    def update(self, bullet_handler, player, explosion_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler, player, explosion_handler)
            if not enemy.is_alive:
                if enemy.is_destroyed:
                    self.enemies_destroyed += 1
                self.remove_enemy(enemy) 

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) <= 2:
            new_enemy = random.choice(self.ENEMIES)
            if new_enemy == ENEMY_SHIP:
                self.enemies.append(Ship())
            else:
                self.enemies.append(Randomship())
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies.clear()
        self.enemies_destroyed = 0  