import pygame
import sys

from settings import Settings
from line   import Line
from ball   import Ball
import game_functions as gf

def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()
    settings = Settings()

    #设置屏幕
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption('弹弹球')

    #创建一个木板
    line = Line(screen,settings)
    ball = Ball(settings,screen)

    while   True:
        gf.check_events(settings,line)
        gf.update_screen(settings,screen,line,ball)

run_game()
