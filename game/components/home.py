
import pygame
from game.utils.constants import HOME, SCREEN_WIDTH, SCREEN_HEIGHT

class Home:
    WIDHT = 300
    HEIGHT = 300
    SPEED = 2

    def __init__(self):
        self.image = HOME
        self.image = pygame.transform.scale(self.image, (self.WIDHT, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.is_alive = False
        self.rect.centery = 0
        self.rect.centerx = SCREEN_WIDTH//2
        self.passed = False
    
    def update(self, player):
        if self.is_alive:
            self.move()
            if self.rect.colliderect(player.rect):
                self.passed = True
            elif self.rect.top == SCREEN_HEIGHT:
                self.passed = True

    def draw(self, screen):
        if self.is_alive:
            screen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.centery += self.SPEED
        self.rect.centerx = SCREEN_WIDTH//2
    
    def reset(self):
        self.rect.centery = 0
        self.passed = False
        self.is_alive = False

        