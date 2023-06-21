import pygame
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, EXPLOSION, BULLET_PLAYER_B

class Spaceship:
    WIDTH = 40
    HEIGHT = 60 
    X_POS = SCREEN_WIDTH // 2 - WIDTH
    Y_POS = 500
    LIFE = 5

    def __init__(self, explosion_handler):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.life = self.LIFE
        self.is_alive = True

    def update(self, user_input, bullet_handler):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        elif user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        elif user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        elif user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
    
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10

    def move_up(self):
        top_limit = SCREEN_HEIGHT // 2
        if self.rect.top > top_limit:
            self.rect.y -= 10

    def hitted(self, damage, explosion_handler):
        self.life -= damage
        if self.life <= 0:
            self.die(explosion_handler)

    def die(self, explosion_handler):
        explosion_handler.generate_explosion(self.WIDTH, self.HEIGHT, self.rect.center)
        self.is_alive = False

    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_PLAYER_B, self.rect.center)

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.life = self.LIFE
        self.is_alive = True