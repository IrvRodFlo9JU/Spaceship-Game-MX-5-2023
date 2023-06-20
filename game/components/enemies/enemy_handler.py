
import random
from game.components.enemies.ship import Ship
from game.components.enemies.enemy_2 import Enemy_2
from game.utils.constants import ENEMY_SHIP, ENEMY_TWO


class EnemyHandler:

    ENEMIES = ["ship", "enemy_2"]

    def __init__(self):
        self.enemies = []
    
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_alive:
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
                self.enemies.append(Enemy_2())
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)