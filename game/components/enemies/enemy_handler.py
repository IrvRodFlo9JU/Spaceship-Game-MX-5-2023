
import random
from game.components.enemies.ship import Ship
from game.components.enemies.randomship import Randomship
from game.components.enemies.sideship import Sideship
from game.components.enemies.baby_boss import BabyBoss
from game.utils.constants import ENEMY_SHIP, ENEMY_RANDOMSHIP, ENEMY_SIDESHIP, ENEMY_BABY_BOSS


class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies_destroyed = 0
        self.enemies_options = [ENEMY_SHIP]
        self.randomship_add = False
        self.sideship_add = False
        self.baby_boss_add = False
        self.limit_enemies = 1
    
    def update(self, bullet_handler, player, explosion_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler, player, explosion_handler)
            if not enemy.is_alive:
                if enemy.is_destroyed:
                    self.enemies_destroyed += enemy.points
                self.remove_enemy(enemy) 
        
        if self.enemies_destroyed >= 100:
            self.enemies.clear()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        while len(self.enemies) < self.limit_enemies and self.enemies_destroyed < 100:
            new_enemy = random.choice(self.enemies_options)
            if new_enemy == ENEMY_SHIP:
                self.enemies.append(Ship())
            elif new_enemy == ENEMY_RANDOMSHIP:
                self.enemies.append(Randomship())
            elif new_enemy == ENEMY_SIDESHIP:
                self.enemies.append(Sideship())
            elif new_enemy == ENEMY_BABY_BOSS:
                self.enemies.append(BabyBoss())
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def up_difficult(self):
        if self.limit_enemies <= 12:
            self.limit_enemies += 1
            
        if self.limit_enemies == 2 and not self.randomship_add:
            self.enemies_options.append(ENEMY_RANDOMSHIP)
            self.randomship_add = True
        elif self.limit_enemies == 4 and not self.sideship_add:
            self.enemies_options.append(ENEMY_SIDESHIP)
            self.sideship_add = True
        elif self.limit_enemies == 5 and not self.baby_boss_add:
            self.enemies_options.append(ENEMY_BABY_BOSS)
            self.baby_boss_add == True
        elif self.limit_enemies == 7:
            self.enemies_options.append(ENEMY_BABY_BOSS)
            self.enemies_options.append(ENEMY_SIDESHIP)

    def reset(self):
        self.enemies.clear()
        self.enemies_destroyed = 0
        self.enemies_options = [ENEMY_SHIP]
        self.randomship_add = False
        self.sideship_add = False
        self.baby_boss_add = False
        self.limit_enemies = 1
    