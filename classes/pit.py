import os
import pygame as pg
import pymunk as pm
from pymunk.pygame_util import *
from settings import *
from random import randrange
from classes.obstacle import Obstacle
from os import kill

class Pit:
    def __init__(self, game, pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), radius=30):
        self.game = game
        self.radius = radius
        self.pos = pos
        self.image = pg.Surface((radius * 2, radius * 2))
        self.image.fill(GREEN)
        self.rect = pg.Rect(pos[0] - radius, pos[1] - radius, 2 * radius, 2 * radius)

    def levelchange(self):
        ball = self.game.ball
        distance = (((self.rect.centerx - ball.body.position.x) ** 2) + ((self.rect.centery - ball.body.position.y) ** 2)) ** (1 / 2)

        if distance < self.radius - ball.radius:
            self.game.points += 1
            self.game.level += 1
            print(self.game.level,  "level")
            print(self.game.points,  "pocet bodu")
        return self.game.level

    def update(self, events_list):
        ball = self.game.ball
        distance = (((self.rect.centerx - ball.body.position.x) ** 2) + ((self.rect.centery - ball.body.position.y) ** 2)) ** (1/2)

        if distance < self.radius - ball.radius:
            pg.draw.circle(self.image, (200, 200, 20), (self.radius, self.radius), self.radius, 0)
            self.game.ball.body.velocity = (0.0, 0.0)
            self.game.ball.body.position = (1500, 1500)
            self.game.screen.fill(GREEN)
            self.game.points += 1
            self.game.level += 1
            print(self.game.level, "level")
            print(self.game.points, "pocet bodu")
            self.game.uroven = False

        else:
            pg.draw.circle(self.image, (20, 20, 20), (self.radius, self.radius), self.radius, 0)
        self.game.screen.blit(self.image, self.rect.topleft)