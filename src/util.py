import os
import pygame as pg

from config import SCREEN_W, SCREEN_H, SCREEN_CAPTION

def initialise_display():
    display = pg.display.set_mode((SCREEN_W, SCREEN_H))
    pg.display.set_caption(SCREEN_CAPTION)
    return display

def load_anim_frames(dir):
    temp = []
    for i in range(1, len(os.listdir(dir))):
        fname = str(i) + '.png'
        img = pg.image.load(os.path.join(dir, fname)).convert_alpha()
        temp.append(img)
    return temp