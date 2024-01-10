# laser.py
import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    '''레이저를 관리하는 클래스'''

    def __init__(self, ag_game):
        '''우주선의 위치에 레이저를 만듭니다'''
        super().__init__()
        self.screen = ag_game.screen
        self.settings = ag_game.settings
        self.color = self.settings.laser_color

        # (0,0)에서 레이저 rect을 만들고 크기를 정합니다
        self.rect = pygame.Rect(0, 0, 
            self.settings.laser_width,
            self.settings.laser_height
        )
        self.rect.midtop = ag_game.ship.rect.midtop

        # Floating pt num = 레이저의 위치
        self.y = float(self.rect.y)

    def update(self):
        '''레이저를 스크린에서 이동합니다'''
        # 정확한 위치를 업데이트합니다
        self.y -= self.settings.laser_speed
        # rect 업데이트합니다
        self.rect.y = self.y

    def draw_laser(self):
        '''스크린에서 레이저를 그립니다'''
        pygame.draw.rect(self.screen, self.color, self.rect)