import sys
import os
import pygame as pg

from config import SCREEN_W, SCREEN_H, SCREEN_CAPTION, SKY_COLOUR
from util import initialise_display
from view import View
from car import Car

# def initialise_display():
#     display = pg.display.set_mode((SCREEN_W, SCREEN_H))
#     pg.display.set_caption(SCREEN_CAPTION)
#     return display

# def load_anim_frames(dir):
#     temp = []
#     for i in range(1, len(os.listdir(dir))):
#         fname = str(i) + '.png'
#         img = pg.image.load(os.path.join(dir, fname)).convert_alpha()
#         temp.append(img)
#     return temp

class MainGame:
    def __init__(self):
        pg.init()

        self._clock = pg.time.Clock()
        self._display = initialise_display()
        self._view = View(1)
        self._car = Car()

        self.look_out = False
        self.car = True

    def game_loop(self):
        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            if self.car:
                self._car.update(self._display)
            if self.look_out:
                self._display.fill(SKY_COLOUR)
                self._view.render_view(self._display)
            pg.display.update()
            self._clock.tick(60)

        pg.quit()
        sys.exit()


if __name__ == '__main__':
    g = MainGame()
    g.game_loop()