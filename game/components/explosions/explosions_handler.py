
from game.components.explosions.explosion import Explosion

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

    def generate_explosion(self, widht, height, center):
        self.explosions.append(Explosion(widht, height, center))

    def remove_explosion(self, explosion):
        self.explosions.remove(explosion)

    def reset(self):
        self.explosions.clear()