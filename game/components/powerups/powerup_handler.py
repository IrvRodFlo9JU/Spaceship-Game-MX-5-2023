
from game.components.powerups.shield import Shield
from game.utils.constants import SHIELD_TYPE

class PowerUpHandler:
    INTERVAL_TIME_SHIELD = 300

    def __init__(self):
        self.power_ups = []
        self.counter_shield_add = 0
        self.interval_time_shield = self.INTERVAL_TIME_SHIELD

    def update(self, player, explosion_handler):
        self.counter_shield_add += 1
        if self.counter_shield_add % self.INTERVAL_TIME_SHIELD == 0:
            self.add_power_up(SHIELD_TYPE)
            self.counter_shield_add = 0

        for power_up in self.power_ups:
            power_up.update(player, explosion_handler)
            if not power_up.is_alive:
                self.remove(power_up)
            
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def add_power_up(self, type_power):
        if type_power == SHIELD_TYPE:
            self.power_ups.append(Shield())
    
    def remove(self, power_up):
        self.power_ups.remove(power_up)

    def up_difficult(self):
        if self.interval_time_shield >= 10:
            self.interval_time_shield -= 20

    def reset(self):
        self.power_ups.clear()
        self.counter_shield_add = 0 
        self.interval_time_shield = self.INTERVAL_TIME_SHIELD       