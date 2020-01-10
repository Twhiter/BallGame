import pygame
from pygame.sprite import Sprite

class   Line(Sprite):
    '''表示木板的类'''

    def __init__(self,screen,settings):
        '''初始化并对木板位置进行设定'''
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        #加载木板图片,并缩小为合适的尺寸
        self.image = pygame.transform.scale(pygame.image.load('images/line.png'),
                                                (self.settings.line_width,self.settings.line_height))
        self.rect = self.image.get_rect()

        #将木板位置设定在最下方的中间
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

        #存储木板的准确位置
        self.x = float(self.rect.x)

        #木板移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        '''在指定位置绘制木板'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''根据移动标志调整飞船位置'''

        if  self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.line_speed_factor
        if  self.moving_left and self.rect.left > 0:
            self.x -= self.settings.line_speed_factor

        #根据self.x更新self.rect.x
        self.rect.x = self.x
