import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
TITLE_IMG = pygame.image.load(os.path.join(IMG_DIR, "Other/title.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
SPEEDY = pygame.image.load(os.path.join(IMG_DIR, 'Other/speedy.png'))
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

BG_INICIAL = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track_2.png'))
BG_2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track_3.jpg'))
BG_3 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track_4.png'))
BG_4 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track_5.jpg'))
BG_5 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track_6.jpg'))
BG_6 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track_7.jpg'))

EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Other/explosion.png"))
BLUE_EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Other/blue_explosion.png"))

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
HEART_LIFE = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_SPEEDY = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_speedy.png"))
SPACESHIP_DAMAGE = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_damage.png"))

BULLET_PLAYER_B = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY_B = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))

SHIP = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
RANDOMSHIP = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
SIDESHIP = pygame.image.load(os.path.join(IMG_DIR, "Enemy/sideship.png"))
BABY_BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/baby_boss.png"))

ASTEROID_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Asteroids/asteroid_enemy.png"))
ASTEROID_BUFF = pygame.image.load(os.path.join(IMG_DIR, "Asteroids/asteroid_buff.png"))

HOME = pygame.image.load(os.path.join(IMG_DIR, 'Other/home.png'))

DEFAULT_TYPE = "default"

#  Types of power ups
SPEEDY_TYPE = "speedy"
SHIELD_TYPE = 'shield'
HEART_TYPE = "heart"

#  Types of enemies
ENEMY_SHIP = "ship"
ENEMY_RANDOMSHIP = "randomship"
ENEMY_SIDESHIP = "sideship"
ENEMY_BABY_BOSS = "baby boss"

FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

#  Moves
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

# Bullets 
BULLET_ENEMY_BASIC = "bullet enemy basic"
BULLET_PLAYER_BASIC = "bullet player basic"
BULLET_PLAYER_BUFF = "bullet player buff"
BULLET_BABY_BOSS = "bullet baby boss"

# Types of asteroids 
ASTEROID_ENEMY_TYPE = "asteroid enemy"
ASTEROID_BUFF_TYPE = "asteroid buff"

# Types of explosion
EXPLOSION_SIMPLE = "simple explosion"
EXPLOSION_BUFF = "explosion de buff"
