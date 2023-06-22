import random
import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, LEFT, RIGHT, BULLET_ENEMY_BASIC, EXPLOSION


class Enemy:
    Y_POS = -5
    X_POS_LIST = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]
    SPEED_X = 5
    SPEED_Y = 3
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 100

    def __init__(self, image, shooting_interval, life, points = 1):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.move_x = random.choice(self.MOV_X)
        self.is_alive = True
        self.index = 0
        self.shooting_time = 0
        self.shooting_interval = shooting_interval
        self.damage = 2 
        self.life = life
        self.is_destroyed = False
        self.points = points

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, bullet_handler, player, explosion_handler):
        if self.rect.top >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()
        self.shooting_time += 1
        self.shoot(bullet_handler)
        self.crash(player, explosion_handler)

    def move(self):
        self.rect.y += self.SPEED_Y

        if self.move_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.left <= 0:
                self.move_x = RIGHT
                self.index = 0
        else:
            self.rect.x += self.SPEED_X
            if self.index > self.INTERVAL or self.rect.right >= SCREEN_WIDTH:
                self.move_x = LEFT
                self.index = 0
        
        self.index += 1

    def shoot(self, bullet_handler):
        if self.shooting_time % self.shooting_interval == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_BASIC, self.rect.center)

    def crash(self, player, explosion_handler):
        if self.rect.colliderect(player.rect):
            player.hitted(self.damage, explosion_handler)
            self.die(explosion_handler)

    def hitted(self, damage, explosion_handler):
        self.life -= damage
        if self.life <= 0:
            self.die(explosion_handler)
        
    def die(self, explosion_handler):
        explosion_handler.generate_explosion(self.WIDTH, self.HEIGHT, self.rect.center)
        self.is_alive = False
        self.is_destroyed = True