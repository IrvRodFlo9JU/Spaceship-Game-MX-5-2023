
import random
from game.components.enemies.ship import Ship
from game.components.enemies.randomship import Randomship
from game.components.enemies.sideship import Sideship
from game.utils.constants import ENEMY_SHIP, ENEMY_RANDOMSHIP, ENEMY_SIDESHIP


class EnemyHandler:


    def __init__(self):
        self.enemies = []
        self.enemies_destroyed = 0
        self.wave = 0
        self.enemies_options = [ENEMY_SHIP]
        self.randomship_add = False
        self.sideship_add = False
    
    def update(self, bullet_handler, player, explosion_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler, player, explosion_handler)
            if not enemy.is_alive:
                if enemy.is_destroyed:
                    self.enemies_destroyed += enemy.points
                self.remove_enemy(enemy) 

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        while len(self.enemies) <= 2:
            new_enemy = random.choice(self.enemies_options)
            if new_enemy == ENEMY_SHIP:
                self.enemies.append(Ship())
            elif new_enemy == ENEMY_RANDOMSHIP:
                self.enemies.append(Randomship())
            elif new_enemy == ENEMY_SIDESHIP:
                self.enemies.append(Sideship())
            self.wave += 1

        if self.wave == 3 and not self.randomship_add:
            self.enemies_options.append(ENEMY_RANDOMSHIP)
            self.randomship_add = True
        elif self.wave == 6 and not self.sideship_add:
            self.enemies_options.append(ENEMY_SIDESHIP)
            self.sideship_add = True
    
        self.start_wave = False
        
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies.clear()
        self.enemies_destroyed = 0  
        self.wave = 0
        self.enemies_options = [ENEMY_SHIP]
        self.randomship_add = False
        self.sideship_add = False
    