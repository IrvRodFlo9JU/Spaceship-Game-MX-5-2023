

import random
from game.utils.constants import ASTEROID_ENEMY_TYPE, ASTEROID_BUFF_TYPE
from game.components.asteroids.asteroid_enemy import AsteroidEnemy
from game.components.asteroids.asteroid_buff import AsteroidBuff


class AsteroidsHandler:
    def __init__(self):
        self.asteroids = []
        self.asteroids_options = [ASTEROID_ENEMY_TYPE, ASTEROID_BUFF_TYPE]
        self.limit_asteroids = 1
    
    def update(self, player, explosion_handler):
        self.add_asteroid()
        for asteroid in self.asteroids:
            asteroid.update(player, explosion_handler)
            if not asteroid.is_alive:
                self.asteroids.remove(asteroid)

    def draw(self, screen):
        for asteroid in self.asteroids:
            asteroid.draw(screen)
    
    def add_asteroid(self):
        while len(self.asteroids) < self.limit_asteroids:
            new_asteroid = random.choice(self.asteroids_options)
            if new_asteroid == ASTEROID_BUFF_TYPE:
                self.asteroids.append(AsteroidBuff())
            else:
                self.asteroids.append(AsteroidEnemy())
    
    def up_difficult(self):
        self.asteroids_options.append(ASTEROID_ENEMY_TYPE)
        self.limit_asteroids += 1

    def reset(self):
        self.asteroids.clear()
        self.asteroids_options = [ASTEROID_ENEMY_TYPE, ASTEROID_BUFF_TYPE]
        self.limit_asteroids = 1