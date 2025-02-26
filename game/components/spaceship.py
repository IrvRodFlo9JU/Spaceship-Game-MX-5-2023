import pygame
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, EXPLOSION, BULLET_PLAYER_BASIC, BULLET_PLAYER_BUFF, SHIELD_TYPE, SPACESHIP_SHIELD, SPEEDY_TYPE, SPACESHIP_SPEEDY, SPACESHIP_DAMAGE, HEART_TYPE

class Spaceship:
    WIDTH = 40
    HEIGHT = 60 
    X_POS = SCREEN_WIDTH // 2 - WIDTH
    Y_POS = 500
    LIFE = 5
    SPEED_X = 10
    SPEED_Y = 10
    POWER_TIME = 180

    def __init__(self, explosion_handler):
        self.image = SPACESHIP
        self.image_default = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.image = self.image_default
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.life = self.LIFE
        self.is_alive = True
        self.limit_plus = 0
        self.buffs = 0
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.power = False
        self.power_count = 0
        self.power_time = self.POWER_TIME
        self.has_shield = False
        self.power_up = 'none'

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
        
        if self.power:
            self.power_count += 1
            if self.power_count % self.power_time == 0:
                self.remove_powers()

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
        if self.life == 1 and damage < 0:
            self.image = self.image_default
        if not self.has_shield:
            self.life -= damage
        if self.life == 1:
            self.image = SPACESHIP_DAMAGE
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
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
        if self.life == 1:
            self.image = self.image_default
        self.life += buff
    
    def give_power(self, type_power):
        self.power = True
        self.power_up = type_power
        if type_power == SHIELD_TYPE:
            self.has_shield = True
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (65, 70))
        elif type_power == SPEEDY_TYPE:
            self.speed_x += 8
            self.speed_y += 6
            self.image = SPACESHIP_SPEEDY
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        elif type_power == HEART_TYPE:
            self.up_life(2)
    
    def remove_powers(self):
        self.image = self.image_default
        self.power = False
        self.power_count = 0
        if self.power_up == SHIELD_TYPE:
            self.has_shield = False
        elif self.power_up == SPEEDY_TYPE:
            self.speed_x -= 8
            self.speed_y -= 6
        self.power_up = 'none'
    
    def up_difficult(self):
        if self.limit_plus <= 250:
            self.limit_plus += 30
        if self.speed_x <= 25:
            self.speed_x += 2
        if self.speed_y <= 25:
            self.speed_y += 1
        if self.power_time <= 350:
            self.power_time += 15

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.life = self.LIFE
        self.is_alive = True
        self.limit_plus = 0
        self.buffs = 0
        self.power_time = self.POWER_TIME
        self.remove_powers()