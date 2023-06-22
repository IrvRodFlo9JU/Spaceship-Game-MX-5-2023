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

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Other/explosion.png"))

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
HEART_LIFE = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))

BULLET_PLAYER_B = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY_B = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))

SHIP = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
RANDOMSHIP = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
SIDESHIP = pygame.image.load(os.path.join(IMG_DIR, "Enemy/sideship.png"))
BABY_BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/baby_boss.png"))

ASTEROID_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Asteroids/asteroid_enemy.png"))
ASTEROID_BUFF = pygame.image.load(os.path.join(IMG_DIR, "Asteroids/asteroid_buff.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

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

# Types of asteroids 
ASTEROID_ENEMY_TYPE = "asteroid enemy"
ASTEROID_BUFF_TYPE = "asteroid buff"
