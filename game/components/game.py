import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, TITLE_IMG
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.explosions.explosions_handler import ExplosionHandler
from game.utils import text_utils


class Game:
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
        self.number_dead = 0
        self.score = 0
        self.scores = []
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
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler, self.player, self.explosion_handler)
            self.bullet_handler.update(self.player, self.enemy_handler, self.explosion_handler)
            self.explosion_handler.update()
            self.score = self.enemy_handler.enemies_destroyed
            if not self.player.is_alive:
                self.finish_count += 1
                pygame.time.delay(300)
                self.scores.append(self.score)
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
            self.draw_score()
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
            self.screen.blit(self.title, self.title_rect)
            text, text_rect = text_utils.get_message("Press any key to Start", 30, WHITE_COLOR, height=500)
        else:
            self.max_score = max(self.scores)
            text, text_rect = text_utils.get_message("Press any key to restart", 30, WHITE_COLOR)
            score, score_rect = text_utils.get_message("Your score was: " + str(self.score), 18, WHITE_COLOR, height=SCREEN_HEIGHT//2 + 50)
            max_score, max_score_rect = text_utils.get_message("Max score: " + str(self.max_score), 15, WHITE_COLOR, 1000, 560)
            self.screen.blit(max_score, max_score_rect)
            self.screen.blit(score, score_rect)
        self.screen.blit(text, text_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message("Score: " + str(self.score), 18, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)

    def reset(self):
        self.player.reset()
        self.bullet_handler.reset()
        self.enemy_handler.reset()
        self.explosion_handler.reset()
        self.game_speed = 10
        self.finish_count = 0
        self.score = 0
