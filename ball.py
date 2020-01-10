import pygame
from pygame.sprite import Sprite


class   Ball(Sprite):
    '''一个球的类'''

    def __init__(self,settings,screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        '''加载球的图片,并缩小,并获取其矩形'''

        self.image  = pygame.transform.scale(pygame.image.load('images/ball.png'),
                                                (2 * self.settings.ball_radius, 2 * self.settings.ball_radius))
        self.rect = self.image.get_rect()

        '''初始化位置'''
        self.rect.x = 0
        self.rect.y = 0

        '''准确存储位置'''
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        '''小球速度'''
        self.x_speed_factor = self.settings.ball_x_speed_factor
        self.y_speed_factor = self.settings.ball_y_speed_factor

    def blite(self):
        '''在指定位置绘制球'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''小球运动'''
        self.x += self.x_speed_factor
        self.y += self.y_speed_factor

        '''更新小球坐标'''
        self.rect.x = self.x
        self.rect.y = self.y



