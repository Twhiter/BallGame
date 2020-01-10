class   Settings():
    '''存储游戏设置信息'''
    def __init__(self):
        '''设置屏幕宽度，高度以及背景色'''
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = 255,255,255

        #存储木板速度
        self.line_speed_factor = 2

        #存储木板宽度，高度
        self.line_width = 250
        self.line_height = 5

        #存储小球各方向速度信息
        self.ball_x_speed_factor = 1
        self.ball_y_speed_factor = 1

        #小球的半径
        self.ball_radius = 50