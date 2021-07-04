import sys
import os
import pygame as pg

from config import SCREEN_W, SCREEN_H, SCREEN_CAPTION, SKY_COLOUR, MUSIC
from util import initialise_display, check_events
from view import View
from car import Car

class MainGame:
    def __init__(self):
        pg.init()

        self._clock = pg.time.Clock()
        self._display = initialise_display()
        self._view = View(2)
        self._car = Car()
        self._audio = pg.mixer.music.load(MUSIC)

        self.look_out = False
        self.car = True

    def game_loop(self):
        running = True
        pg.mixer.music.play(loops=-1)

        while running:
            running, clicked = check_events()
            if self.car:
                action = self._car.update(self._display, clicked)
                if action:
                    self.car = False
                    if action == 'window':
                        self.look_out = True
            if self.look_out:
                self._display.fill(SKY_COLOUR)
                self._view.render_view(self._display)
                back = self._view.go_back(self._display)
                if back and clicked:
                    self.look_out = False
                    self.car = True
            pg.display.update()
            self._clock.tick(60)

        self.car = False
        self.view = False
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    g = MainGame()
    g.game_loop()