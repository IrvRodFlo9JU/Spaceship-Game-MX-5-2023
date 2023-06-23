
import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, TITLE_IMG
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.explosions.explosions_handler import ExplosionHandler
from game.components.hearts.hearts_handler import HeartsHandler
from game.components.asteroids.asteroids_handle import AsteroidsHandler
from game.components.powerups.powerup_handler import PowerUpHandler
from game.utils import text_utils


class Game:
    SCORE_STEP_BUFF = 7
    SCORE_STEP_DIFFICULT = 5

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.finish_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.explosion_handler = ExplosionHandler()
        self.player = Spaceship(self.explosion_handler)
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.asteroids_handler = AsteroidsHandler()
        self.player_life = HeartsHandler()
        self.power_up_handler = PowerUpHandler()
        self.number_dead = 0
        self.score = 0
        self.scores = []
        self.max_score = 0
        self.scores_buff = []
        self.counter_score_buffs = 1
        self.scores_difficult = []
        self.counter_score_difficult = 1
        self.player_buffs = 0
        self.level = 1
        self.levels = []
        self.max_score = 0

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
        event = pygame.key.get_pressed()
        if event[pygame.K_r] and not self.playing:
                self.playing = True
                self.reset()

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler, self.player, self.explosion_handler)
            self.bullet_handler.update(self.player, self.enemy_handler, self.explosion_handler)
            self.explosion_handler.update()
            self.asteroids_handler.update(self.player, self.explosion_handler)
            self.player_life.update(self.player)
            self.power_up_handler.update(self.player, self.explosion_handler)
            self.score = self.enemy_handler.enemies_destroyed
            self.difficult_controler()
            self.score_buff()
            self.player_buffs = self.player.buffs
            if not self.player.is_alive:
                self.finish_count += 1
                pygame.time.delay(300)
                self.scores.append(self.score)
                self.levels.append(self.level)
                if self.finish_count == 1:
                    self.playing = False
                    self.number_dead += 1

    def draw(self):
        self.draw_background()
        if not self.playing:
            self.draw_menu()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.explosion_handler.draw(self.screen)
            self.asteroids_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.draw_score()
            self.draw_buff()
            self.draw_level()
            self.player_life.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_menu(self):
        if self.number_dead == 0:
            self.title = TITLE_IMG
            self.title = pygame.transform.scale(self.title, (600, 200))
            self.title_rect = self.title.get_rect()
            self.title_rect.centerx = SCREEN_WIDTH//2
            self.title_rect.centery = 200
            text, text_rect = text_utils.get_message("Press R to Start", 30, WHITE_COLOR, height=500)
        else:
            self.max_score = max(self.scores)
            self.max_level = max(self.levels)
            self.title = pygame.transform.scale(self.title, (330, 110))
            self.title_rect = self.title.get_rect()
            self.title_rect.centerx = SCREEN_WIDTH//2
            self.title_rect.centery = 90
            text, text_rect = text_utils.get_message("Press R to restart", 30, WHITE_COLOR)
            score, score_rect = text_utils.get_message("Your score was: " + str(self.score), 18, WHITE_COLOR, height=SCREEN_HEIGHT//2 + 50)
            max_score, max_score_rect = text_utils.get_message("Max score: " + str(self.max_score), 15, WHITE_COLOR, 1000, 560)
            attempts, attempts_rect = text_utils.get_message("Attempts: " + str(self.number_dead), 15, WHITE_COLOR, 100, 560)
            level, level_rect = text_utils.get_message("Level reached " + str(self.level), 15, WHITE_COLOR, height=SCREEN_HEIGHT//2 + 80)
            max_level, max_level_rect = text_utils.get_message("Max level: " + str(self.max_level), 15, WHITE_COLOR, 1000, 530)
            self.screen.blit(level, level_rect)
            self.screen.blit(max_level, max_level_rect)
            self.screen.blit(attempts, attempts_rect)
            self.screen.blit(max_score, max_score_rect)
            self.screen.blit(score, score_rect)
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(text, text_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message("Score: " + str(self.score), 18, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)

    def score_buff(self):
        while self.counter_score_buffs <= 20:
            self.scores_buff.append(self.counter_score_buffs * self.SCORE_STEP_BUFF)
            self.counter_score_buffs += 1
        
        if self.score in self.scores_buff:
            self.player.give_buff(1)
            self.scores_buff.remove(self.score)

    def draw_buff(self):
        buff, buff_rect = text_utils.get_message("Buffs: " + str(self.player_buffs), 18, WHITE_COLOR, 1000, 80)
        self.screen.blit(buff, buff_rect) 
    
    def difficult_controler(self):
        while self.counter_score_difficult <= 20:
            self.scores_difficult.append(self.counter_score_difficult * self.SCORE_STEP_DIFFICULT)
            self.counter_score_difficult += 1 
        
        if self.score in self.scores_difficult:
            self.up_difficult()
            self.scores_difficult.remove(self.score)

    def draw_level(self):
        level, level_rect = text_utils.get_message("Level " + str(self.level), 18, WHITE_COLOR, 1000, 120)
        self.screen.blit(level, level_rect)

    def up_difficult(self):
        self.game_speed += 1
        self.level += 1
        self.player.up_difficult()
        self.enemy_handler.up_difficult()
        self.asteroids_handler.up_difficult()
        self.power_up_handler.up_difficult()

    def reset(self):
        self.player.reset()
        self.bullet_handler.reset()
        self.enemy_handler.reset()
        self.explosion_handler.reset()
        self.player_life.reset()
        self.asteroids_handler.reset()
        self.power_up_handler.reset()
        self.game_speed = 10
        self.finish_count = 0
        self.score = 0
        self.scores_buff = []
        self.counter_score_buffs = 1
        self.scores_difficult = []
        self.counter_score_difficult = 1
        self.player_buffs = 0
        self.level = 1