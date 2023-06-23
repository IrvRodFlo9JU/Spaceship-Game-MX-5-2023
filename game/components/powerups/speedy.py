
import pygame
from game.components.powerups.power_up import PowerUp
from game.utils.constants import SPEEDY, SPEEDY_TYPE

class Speedy(PowerUp):
    SPEED = 6

    def __init__(self):
        self.image = SPEEDY
        super().__init__(self.image, self.SPEED, SPEEDY_TYPE)