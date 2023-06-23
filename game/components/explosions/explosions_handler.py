
from game.components.explosions.explosion_simple import ExplosionSimple
from game.components.explosions.explosion_buff import ExplosionBuff
from game.utils.constants import EXPLOSION_BUFF, EXPLOSION_SIMPLE

class ExplosionHandler:
    def __init__(self):
        self.explosions = []

    def update(self):
        for explosion in self.explosions:
            explosion.update()
            if not explosion.is_alive:
                self.remove_explosion(explosion)
    
    def draw(self, screen):
        for explosion in self.explosions:
            explosion.draw(screen)

    def generate_explosion(self, width, height, center, type_explosion = EXPLOSION_SIMPLE):
        if type_explosion == EXPLOSION_SIMPLE:
            self.explosions.append(ExplosionSimple(width, height, center))
        else:   
            self.explosions.append(ExplosionBuff(width, height, center))

    def remove_explosion(self, explosion):
        self.explosions.remove(explosion)

    def reset(self):
        self.explosions.clear()