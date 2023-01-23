import sys
from os import kill
import pygame as pg
from tkinter import *
import pygame.font
import settings
from classes.ball import Ball
from classes.pit import Pit
from classes.obstacle import Obstacle
from classes.playground import Playground
from settings import *
from random import randrange
import pymunk
import pymunk.pygame_util

class Game:
    points = 0
    level = 1
    strokes = 0
    maxstrokes = 15
    strokesleft = 15
    maxlevel = 3

    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        pg.display.set_caption('Minigolf')
        self.font = pg.font.Font('freesansbold.ttf', 200)
        self.fonttries = pg.font.Font('freesansbold.ttf', 50)
        self.text = self.font.render('U WON', False, 'GREY')
        self.textlost = self.font.render('U LOST', False, 'RED')

        self.textRect = self.text.get_rect()
        self.textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.uroven = True
        self.running = True
        self.events_list = None
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.space = pymunk.Space()

        self.dt = 1 / FPS
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)

    def enviroment(self):
        if self.level == 1:
            self.obstacle1 = Obstacle(self, (400, 200), (500, 500), points=[(100, 0), (0, 0), (100,500), (0, 500)])
            self.obstacle2 = Obstacle(self, (600, 400), (300, 300), points=[(500, 0), (0, 0), (500,100), (0, 100),(550,50)])
            self.obstacle3 = Obstacle(self, (750, 100), (300, 300), points=[(940, -50), (0, -50), (940, 50), (0, 50)])
            self.obstacle4 = Obstacle(self, (1400, 650), (0, 0), points=[(289, 0), (0, 200), (289, 200) ])
            self.obstacle5 = Obstacle(self, (1589, 50), (0, 0), points=[(100, 0), (0, 0), (100,800), (0, 800)])
            self.obstacle6 = Obstacle(self, (1200, 100), (0, 0), points=[(0, 0), (400, 0), (400, 400)])
            self.obstaclex = Obstacle(self, (150, 100), (0, 0), points=[(0, 0), (0, 100), (10, 0), (10, 100)])
            self.obstacley = Obstacle(self, (150, 100), (0, 0), points=[(-45, 45), (-45, 55), (55, 45), (55, 55)])
            self.obstaclex2 = Obstacle(self, (750, 700), (0, 0), points=[(0, 0), (0, 100), (10, 0), (10, 100)])
            self.obstacley2 = Obstacle(self, (750, 700), (0, 0), points=[(-45, 45), (-45, 55), (55, 45), (55, 55)])

        elif self.level == 2:
            self.obstacle7 = Obstacle(self, (200, 300), (400, 400), points=[(300, 0), (0,20), (0,100), (330, 200), (200, -100)])
            self.obstacle8 = Obstacle(self, (700, 51), (0, 0), points=[(0, 0), (75, 0), (50, 99), (99, 50), (100, 99)])
            self.obstacle9 = Obstacle(self, (500, 400), (300, 300), points=[(200, 0), (0, -200), (200,100), (0, 100)])
            self.obstacle10 = Obstacle(self, (1400, 650), (0, 0), points=[(289, 0), (0, 200), (289, 200) ])
            self.obstaclex4 = Obstacle(self, (1050, 500), (0, 0), points=[(0, 0), (0, 100), (10, 0), (10, 100)])
            self.obstacley4 = Obstacle(self, (1050, 500), (0, 0), points=[(-45, 45), (-45, 55), (55, 45), (55, 55)])
            self.obstaclex6 = Obstacle(self, (1000, 200), (0, 0), points=[(0, 0), (0, 100), (10, 0), (10, 100)])
            self.obstacley6 = Obstacle(self, (1000, 200), (0, 0), points=[(-45, 45), (-45, 55), (55, 45), (55, 55)])
            self.obstaclex7 = Obstacle(self, (650, 100), (0, 0), points=[(0, 0), (0, 100), (10, 0), (10, 100)])
            self.obstacley7 = Obstacle(self, (650, 100), (0, 0), points=[(-45, 45), (-45, 55), (55, 45), (55, 55)])

        elif self.level == 3:
            self.obstacle11 = Obstacle(self, (500, 300), (400, 400), points=[(0, 0), (0, 400), (300, 50), (500, 200)])
            self.obstacle12 = Obstacle(self, (11, 700), (300, 300), points=[(50,0), (50,149), (300,149)])
            self.obstaclex1 = Obstacle(self, (250, 500), (0, 0), points=[(0, 0), (0, 100), (10, 0), (10, 100)])
            self.obstacley1 = Obstacle(self, (250, 500), (0, 0), points=[(-45, 45), (-45, 55), (55, 45), (55, 55)])

            self.obstaclex3 = Obstacle(self, (950, 600), (0, 0), points=[(0, 0), (0, 100), (10, 0), (10, 100)])
            self.obstacley3 = Obstacle(self, (950, 600), (0, 0), points=[(-45, 45), (-45, 55), (55, 45), (55, 55)])
            self.obstaclex5 = Obstacle(self, (1400, 680), (0, 0), points=[(0, 0), (0, 100), (10, 0), (10, 100)])
            self.obstacley5 = Obstacle(self, (1400, 680), (0, 0), points=[(-45, 45), (-45, 55), (55, 45), (55, 55)])

    def doplnek(self):
        #funkce nakreslí jamky a míčky každý level
        if self.level == 1:
            self.playground = Playground(self)
            self.ball = Ball(self, (1500, 700))
            self.all_sprites.add(self.ball)
            self.pit = Pit(self, (300, 80))

        elif self.level == 2:

            self.ball = Ball(self, (300, 80))
            self.all_sprites.add(self.ball)
            self.pit = Pit(self, (1200, 500))

        elif self.level == 3:

            self.ball = Ball(self,(1200, 500))
            self.all_sprites.add(self.ball)
            self.pit = Pit(self, (100, 360))

    def events(self):
        self.events_list = pg.event.get()
        #funkce zajistí ať hra jde vypnout
        for event in self.events_list:
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        if self.level <= self.maxlevel and self.strokes <= self.maxstrokes:
            #vykreslení hřiště
            self.screen.fill(GREEN)
            self.clock.tick(FPS)
            self.ball.update(self.events_list)
            self.pit.update(self.events_list)
            self.space.debug_draw(self.draw_options)
            # přidání informace o počtu zbyvajích pokusů
            self.textstrokes = self.fonttries.render("Strokes:{}/15".format(self.strokes), False, 'RED')
            self.rectStrokes = self.textstrokes.get_rect()
            self.rectStrokes.bottomright = (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 850)
            self.screen.blit(self.textstrokes, self.rectStrokes)
            #přidání informace o levelu
            self.textlevel = self.fonttries.render("Level: {}/3".format(self.level), False, 'RED')
            self.rectLevel = self.textlevel.get_rect()
            self.rectLevel.bottomright = (SCREEN_WIDTH - 1400, SCREEN_HEIGHT - 850)
            self.screen.blit(self.textlevel, self.rectLevel)
            pg.display.update()
        #funkce když prohrajeme nám to oznámí
        elif self.level <= self.maxlevel and self.strokes >= self.maxstrokes:
            self.screen.fill(GREEN)
            self.clock.tick(FPS)
            self.screen.blit(self.textlost, self.textRect)
            pg.display.update()
        #funkce když vyhrajeme nám to oznámí
        else:
            self.screen.fill(GREEN)
            self.clock.tick(FPS)
            self.screen.blit(self.text, self.textRect)
            pg.display.update()

    def run(self):
        # funkce nakreslí první level
        self.doplnek()
        self.enviroment()

        while self.running:
            for _ in range(10):
                self.space.step(self.dt / 10)
                #funkce zajistí ať se proces nezastaví
                if self.running == True:
                    self.events()
                    self.update()

            if self.uroven == False:
                if self.pit.levelchange() == 2:
                    # funkce přidá překážky do prvního levelu a tím vznikne level 2
                    self.enviroment()
                    self.doplnek()
                    self.pit.levelchange()
                    self.uroven = True

                elif self.pit.levelchange() == 3:
                    # funkce přidá překážky do prvního a druhého levelu a tím vznikne level 3
                    self.enviroment()
                    self.doplnek()
                    self.pit.levelchange()
                    self.uroven = True

def main():
    #vyvolání funkcí pro nakreslení všeho
    g = Game()
    g.run()

if __name__ == '__main__': main()
