
from game.utils.constants import SCREEN_HEIGHT

class Bullet:
    def __init__(self, image, center, damage):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.damage = damage
        self.is_alive = True

    def update(self, object):
        self.move()
        self.crash(object)
        if self.rect.y == SCREEN_HEIGHT:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        pass

    def crash(self, object):
        if self.rect.colliderect(object.rect):
            object.hitted(self.damage)
            self.is_alive = False

