import os
import pygame as pg

from config import SCREEN_W, SCREEN_H, SCREEN_CAPTION, CLICK_DIR

def initialise_display():
    display = pg.display.set_mode((SCREEN_W, SCREEN_H))
    pg.display.set_caption(SCREEN_CAPTION)
    return display

def load_anim_frames(dir):
    temp = []
    fnames = [str(i+1) + '.png' for i in range(len(os.listdir(dir)))]
    print(fnames)
    # for i in range(len(os.listdir(dir))):
    #     fname = str(i+1) + '.png'
    #     img = pg.image.load(os.path.join(dir, fname)).convert_alpha()
    #     temp.append(img)
    for fname in fnames:
        try:
            temp.append(pg.image.load(os.path.join(dir, fname)).convert_alpha())
        except FileNotFoundError:
            temp.append(pg.Surface((30, 30)).convert())

    return temp

def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False, False
        if event.type == pg.MOUSEBUTTONDOWN:
            return True, True
    return True, False

class Button(pg.sprite.Sprite):
    def __init__(self, name, pos):
        pg.sprite.Sprite.__init__(self)
        self._name = name
        self._pos = pos
        self._frames = load_anim_frames(CLICK_DIR)
        self._frame_idx = 0
        self.image = self._frames[0]
        self.rect = self.image.get_rect(topleft=self._pos)

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        hit = self.rect.collidepoint(mouse_pos)
        self.image = self._frames[1] if hit else self._frames[0]
        return self._name if hit else False

    def draw(self, display):
        display.blit(self.image, self.rect)