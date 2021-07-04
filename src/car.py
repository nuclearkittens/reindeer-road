import os
import math
import pygame as pg

from util import load_anim_frames, Button
from config import CAR_DIR, SCREEN_W, SCREEN_H

class Car:
    def __init__(self):
        self._bg = pg.image.load(os.path.join(CAR_DIR, 'bg_back.png')).convert_alpha()
        self._bg_mid = pg.image.load(os.path.join(CAR_DIR, 'bg_mid.png')).convert_alpha()
        self._bg_front = pg.image.load(os.path.join(CAR_DIR, 'bg_front.png')).convert_alpha()
        self._road = AnimatedEntity(os.path.join(CAR_DIR, 'road'))
        self._mum = AnimatedEntity(os.path.join(CAR_DIR, 'mum'))
        # self._dad_static = StaticEntity(os.path.join(CAR_DIR, 'dad.png'))
        self._dad_anim = AnimatedEntity(os.path.join(CAR_DIR, 'dad'))
        self._hand = PlayerHand()

        self._group = pg.sprite.Group(
            self._mum, self._dad_anim)

        self._buttons = pg.sprite.Group()
        self.create_buttons()


    def update(self, display, clicked):
        display.blit(self._bg, (0, 0))
        self._road.update()
        self._road.draw(display)
        display.blit(self._bg_mid, (0, 0))
        self._group.update()
        self._group.draw(display)
        display.blit(self._bg_front, (0, 0))
        self._hand.update()
        self._hand.draw(display)

        for button in self._buttons:
            action = button.update()
            button.draw(display)
            if clicked and action:
                return action

        return False

    def create_buttons(self):
        self._buttons.add(Button('window', (1800, 500)))


class AnimatedEntity(pg.sprite.Sprite):
    def __init__(self, img_dir):
        pg.sprite.Sprite.__init__(self)
        self._update_time = pg.time.get_ticks()
        self._frames = load_anim_frames(img_dir)
        self._frame_idx = 0
        self.image = self._frames[0]
        self.rect = self.image.get_rect()

    def update(self):
        anim_cooldown = 200
        try:
            self.image = self._frames[self._frame_idx]
        except IndexError:
            self.image = self._frames[-1]

        if pg.time.get_ticks() - self._update_time > anim_cooldown:
            self._update_time = pg.time.get_ticks()
            self._frame_idx += 1
        if self._frame_idx >= len(self._frames):
            self._frame_idx = 0
            # self._update_time = pg.time.get_ticks()

    def draw(self, display):
        display.blit(self.image, self.rect)

class StaticEntity(pg.sprite.Sprite):
    def __init__(self, img_path):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self, display):
        display.blit(self.image, self.rect)

class PlayerHand(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self._og_image = pg.image.load(os.path.join(CAR_DIR, 'hand.png'))
        self.pos = (SCREEN_W // 2, SCREEN_H + 500)
        self.image = self._og_image
        self.rect = self.image.get_rect(midbottom=self.pos)

    def _rotate(self):
        correction_angle = 90
        mouse_x, mouse_y = pg.mouse.get_pos()
        dx, dy = mouse_x - (self.rect.x + self.rect.width), mouse_y - self.rect.centery
        # angle = int((180 / math.pi) * -math.atan2(y, x))
        angle = math.degrees(math.atan2(-dy, dx)) - correction_angle
        self.image = pg.transform.rotate(self._og_image, angle)
        self.rect = self.image.get_rect(midbottom=self.pos)

    def update(self):
        self._rotate()

    def draw(self, display):
        display.blit(self.image, self.rect)
