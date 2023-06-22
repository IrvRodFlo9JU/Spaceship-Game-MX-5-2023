

import random
from game.utils.constants import ASTEROID_ENEMY_TYPE, ASTEROID_BUFF_TYPE
from game.components.asteroids.asteroid_enemy import AsteroidEnemy
from game.components.asteroids.asteroid_buff import AsteroidBuff


class AsteroidsHandler:
    LUCKY = 9

    def __init__(self):
        self.asteroids = []
        self.asteroids_options = [ASTEROID_ENEMY_TYPE, ASTEROID_ENEMY_TYPE, ASTEROID_BUFF_TYPE]
    
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
        while len(self.asteroids) < 2:
            new_asteroid = random.choice(self.asteroids_options)
            if new_asteroid == ASTEROID_BUFF_TYPE:
                self.asteroids.append(AsteroidBuff())
            else:
                self.asteroids.append(AsteroidEnemy())
    
    def reset(self):
        self.asteroids.clear()