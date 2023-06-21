
from game.utils.constants import SCREEN_HEIGHT

class Bullet:
    def __init__(self, image, center, damage, player_bullet):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.damage = damage
        self.is_alive = True
        self.player_bullet = player_bullet

    def update(self, enemy_handler, explosion_handler, player):
        self.move()
        if self.player_bullet:
            for enemy in enemy_handler.enemies:
                self.crash(enemy, explosion_handler)
            if self.rect.y <= 0:
                self.is_alive = False
        else:
            self.crash(player, explosion_handler)
            if self.rect.y >= SCREEN_HEIGHT:
                self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        pass

    def crash(self, object, explosion_handler):
        if self.rect.colliderect(object.rect):
            object.hitted(self.damage, explosion_handler)
            self.is_alive = False

