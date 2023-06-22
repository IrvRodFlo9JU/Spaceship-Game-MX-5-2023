import pygame
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, EXPLOSION, BULLET_PLAYER_BASIC, BULLET_PLAYER_BUFF

class Spaceship:
    WIDTH = 40
    HEIGHT = 60 
    X_POS = SCREEN_WIDTH // 2 - WIDTH
    Y_POS = 500
    LIFE = 5
    SPEED_X = 10
    SPEED_Y = 10

    def __init__(self, explosion_handler):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.life = self.LIFE
        self.is_alive = True
        self.limit_plus = 0
        self.buffs = 0
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

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

        if self.buffs > 0 and user_input[pygame.K_q]:
            self.special_shoot(bullet_handler)
            self.buffs -= 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed_x

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed_x
    
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed_y

    def move_up(self):
        top_limit = (SCREEN_HEIGHT // 2) - self.limit_plus
        if self.rect.top > top_limit:
            self.rect.y -= self.speed_y

    def hitted(self, damage, explosion_handler):
        self.life -= damage
        if self.life <= 0:
            self.die(explosion_handler)

    def die(self, explosion_handler):
        explosion_handler.generate_explosion(self.WIDTH, self.HEIGHT, self.rect.center)
        self.is_alive = False

    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_PLAYER_BASIC, self.rect.center)
    
    def special_shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_PLAYER_BUFF, self.rect.center)

    def give_buff(self, buff_life):
        self.buffs += 1
        self.up_life(buff_life)
            
    def up_life(self, buff):
        self.life += buff
    
    def up_difficult(self):
        if self.limit_plus <= 50:
            self.limit_plus += 30
        if self.speed_x <= 25:
            self.speed_x += 2
        if self.speed_y <= 25:
            self.speed_y += 1

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.life = self.LIFE
        self.is_alive = True
        self.limit_plus = 0
        self.buffs = 0
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y