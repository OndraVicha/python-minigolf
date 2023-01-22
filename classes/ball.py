import os
import pygame as pg
import pymunk as pm
from pymunk.pygame_util import *
from settings import *
from random import randrange

class Ball(pg.sprite.Sprite):
    def __init__(self, game, pos=(SCREEN_WIDTH / 1.2, SCREEN_HEIGHT / 1.2), radius=20):
        super(Ball, self).__init__()
        self.game = game
        self.body = pm.Body(body_type=pm.Body.DYNAMIC)
        self.body.position = pos
        self.radius = radius
        self.image = pg.Surface((radius, radius ))

        self.shape = pm.Circle(self.body, self.radius)
        self.shape.mass = 0.6
        self.shape.elasticity = 1
        self.shape.friction = 0
        self.speed = 10
        self.shape.color = (255, 255, 255, 0)
        self.game.space.add(self.body, self.shape)
        self.pre_pos = None

    def update(self, events_list):

        for event in events_list:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.shape.point_query(event.pos).distance.real < 0:
                    self.pre_pos = from_pygame(event.pos, self.game.screen)

            elif event.type == pg.MOUSEMOTION:
                if self.pre_pos:
                    p = to_pygame(self.body.position, self.game.screen)
                    pg.draw.line(self.game.screen, RED, p, event.pos, 10)

            elif event.type == pg.MOUSEBUTTONUP:

                if self.pre_pos:
                    p0 = pm.Vec2d(self.body.position.x, self.body.position.y)
                    p1 = from_pygame(event.pos, self.game.screen)
                    force = 1000 * pm.Vec2d(p0.x - p1[0], p0.y - p1[1]).rotated(-self.body.angle)
                    self.speed * 0.4
                    self.body.apply_force_at_local_point(force * self.speed)
                    self.pre_pos = None
                    self.game.strokes += 1
                    a = "Pokus "
                    b = self.game.strokes
                    print(a,b)







