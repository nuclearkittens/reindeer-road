import os
import pygame as pg

from random import uniform

from config import DIRNAME, FRAME_DIR, SCREEN_W, SCREEN_H
from util import load_anim_frames, Button

class View:
    def __init__(self, idx):
        self._scenery = self._load_view_imgs(idx)
        self._frame = pg.image.load(FRAME_DIR)
        self._button = Button('back', (0, SCREEN_H - 200))

    def _load_view_imgs(self, idx):
        temp = {}
        view_dir = os.path.join(DIRNAME, 'img/views', str(idx))
        frames = load_anim_frames(view_dir)
        # for i in range(1, len(os.listdir(view_dir))):
        #     fname = str(i) + '.png'
        #     img = pg.image.load(os.path.join(view_dir, fname)).convert_alpha()
        #     rect = img.get_rect()
        #     speed = uniform(3.0, 6.0)
        #     temp[img] = [speed, rect]
        for frame in frames:
            rect = frame.get_rect()
            speed = uniform(3.0, 9.0)
            temp[frame] = [speed, rect]
        return temp

    def render_view(self, display):
        for img, attr in self._scenery.items():
            display.blit(img, attr[1])
            display.blit(img, attr[1].move(attr[1].width, 0))
            attr[1].move_ip(-attr[0], 0)
            if attr[1].right <= 0:
                attr[1].x = 0
        display.blit(self._frame, (0,0))

    def go_back(self, display):
        back = self._button.update()
        self._button.draw(display)
        return True if back else False
