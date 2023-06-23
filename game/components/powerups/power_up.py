
import pygame, random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT, SHIELD_TYPE

class PowerUp:
    WIDTH = 30
    HEIGHT = 30
    POS_Y = 0
    OPTIONS_MOVE = [LEFT, RIGHT]

    def __init__(self, image, speed, power):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = self.POS_Y
        self.move_x = random.choice(self.OPTIONS_MOVE)
        self.rect.x = random.randint(50, SCREEN_WIDTH - 50)
        self.speed = speed
        self.is_alive = True
        self.type_power = power

    def update(self, player, explosion_handler):
        self.move()
        self.crash(player, explosion_handler)
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
    
    def crash(self, player, explosion_handler):
        if self.rect.colliderect(player.rect):
            player.give_power(self.type_power)
            self.die(explosion_handler)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.y += self.speed

        if self.move_x == LEFT:
            self.rect.x -= self.speed // 2
            if self.rect.left <= 0:
                self.move_x = RIGHT
        else:
            self.rect.x += self.speed // 2
            if self.rect.right >= SCREEN_WIDTH:
                self.move_x = LEFT
    
    def die(self, explosion_handler):
        explosion_handler.generate_explosion(self.WIDTH, self.HEIGHT, self.rect.center)
        self.is_alive = False

