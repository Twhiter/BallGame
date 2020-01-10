import pygame
import sys

def check_events(settings,line):
    '''响应按键和鼠标事件'''

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,line)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,line)

def check_keydown_events(event,line):
    '''按键按下'''

    if  event.key == pygame.K_RIGHT:
        line.moving_right = True
    elif    event.key == pygame.K_LEFT:
        line.moving_left = True

def check_keyup_events(event,line):
    '''按键松开'''

    if  event.key == pygame.K_RIGHT:
        line.moving_right = False
    elif    event.key == pygame.K_LEFT:
        line.moving_left = False


def check_collisions(ball,line):
    '''检测球与木板，或球与边界是否发生碰撞，如果发生碰撞，就改变方向'''

    if  pygame.sprite.collide_rect(ball,line) or ball.rect.top <= 0:
        ball.y_speed_factor *= -1

    elif    ball.rect.left <=0 or ball.rect.right >= ball.screen_rect.right:
        ball.x_speed_factor *= -1


def update_screen(settings,screen,line,ball):
    '''更新屏幕上的图像，并更新到新屏幕'''
    screen.fill(settings.screen_bg_color)
    ball.update()
    ball.blite()
    line.update()
    line.blitme()
    check_collisions(ball,line)
    pygame.display.flip()

