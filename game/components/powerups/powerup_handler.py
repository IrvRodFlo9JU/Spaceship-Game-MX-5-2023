
import random
from game.components.powerups.shield import Shield
from game.components.powerups.speedy import Speedy
from game.components.powerups.heart import Heart
from game.utils.constants import SHIELD_TYPE, SPEEDY_TYPE, HEART_TYPE

class PowerUpHandler:
    INTERVAL_TIME = 300
    OPTIONS = [HEART_TYPE, SHIELD_TYPE, SPEEDY_TYPE]

    def __init__(self):
        self.power_ups = []
        self.counter_add = 0
        self.options = self.OPTIONS
        self.interval_add = self.INTERVAL_TIME

    def update(self, player, explosion_handler):
        self.counter_add += 1
        if self.counter_add % self.interval_add == 0:
            self.add_power_up()
            self.counter_add = 0

        for power_up in self.power_ups:
            power_up.update(player, explosion_handler)
            if not power_up.is_alive:
                self.remove(power_up)
            
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def add_power_up(self):
        new_power = random.choice(self.options)
        if new_power == SHIELD_TYPE:
            self.power_ups.append(Shield())
        elif new_power == SPEEDY_TYPE:
            self.power_ups.append(Speedy())
        elif new_power == HEART_TYPE:
            self.power_ups.append(Heart())

    def remove(self, power_up):
        self.power_ups.remove(power_up)

    def up_difficult(self):
        if self.interval_time >= 60:
            self.interval_time -= 20
        if self.interval_time == self.INTERVAL_TIME - 60:
            self.options.append(SHIELD_TYPE, HEART_TYPE)

    def reset(self):
        self.power_ups.clear()
        self.counter_add = 0 
        self.interval_add = self.INTERVAL_TIME    