
import random
from game.utils.constants import ASTEROID_ENEMY, SCREEN_HEIGHT, EXPLOSION_BUFF, EXPLOSION_SIMPLE

class Asteroid:
    Y_POS = -5
    X_POS_LIST = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

    def __init__(self, image, damage, speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.is_alive = True
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.damage = damage
        self.speed = speed

    def update(self, player, explosion_handler):
        if self.rect.top >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()
        self.crash(player, explosion_handler)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def crash(self, player, explosion_handler):
        if self.rect.colliderect(player.rect):
            player.hitted(self.damage, explosion_handler)
            self.die(explosion_handler)
    
    def move(self):
        self.rect.y += self.SPEED
    
    def die(self, explosion_handler):
        if self.damage <= 0:
            type_explosion = EXPLOSION_BUFF
        else:
            type_explosion = EXPLOSION_SIMPLE
        explosion_handler.generate_explosion(self.WIDTH, self.HEIGHT, self.rect.center, type_explosion)
        self.is_alive = False