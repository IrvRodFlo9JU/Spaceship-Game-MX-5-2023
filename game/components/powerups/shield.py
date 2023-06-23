
import pygame
from game.components.powerups.power_up import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE

class Shield(PowerUp):
    SPEED = 5

    def __init__(self):
        self.image = SHIELD
        super().__init__(self.image, self.SPEED, SHIELD_TYPE)