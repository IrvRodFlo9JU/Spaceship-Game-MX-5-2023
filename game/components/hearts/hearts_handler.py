
from game.components.hearts.heart import Heart


class HeartsHandler:
    POS_X = 50
    POS_Y = 40
    SPACE = 5
    HEART_WIDTH = 20

    def __init__(self):
        self.lifes = []
        self.pos_x = self.POS_X
        self.player_life = 5

    def update(self, player):
        self.player_life = player.life
        self.add_heart()
        if len(self.lifes) > self.player_life:
            self.remove_heart()

    def draw(self, screen):
        for heart in self.lifes:
            heart.draw(screen)

    def add_heart(self):
        if len(self.lifes) <  self.player_life + 1:
            if len(self.lifes) > 0:
                self.pos_x += self.HEART_WIDTH
            self.lifes.append(Heart(self.pos_x, self.POS_Y))
            self.pos_x += self.SPACE

    def remove_heart(self):
        self.lifes.pop()
        self.pos_x -= (self.SPACE + self.HEART_WIDTH)

    def reset(self):
        self.pos_x = self.POS_X


