# ship.py
import pygame

class Ship:
    '''우주선을 관리하는 클래스'''

    def __init__(self, ag_game):
        '''우주선을 초기화하고 시작 위치를 설정합니다'''
        self.screen = ag_game.screen
        self.settings = ag_game.settings
        self.screen_rect = ag_game.screen.get_rect()

        # 우주선 이미지를 불러오고 사각형을 가져옵니다
        image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(image, (100,100))
        self.rect = self.image.get_rect()

        # 우주선의 초기 위치는 화면 하단 중앙입니다
        self.rect.midbottom = self.screen_rect.midbottom

        # Floating pt num for ship's exact 위치
        self.x = float(self.rect.x)

        # 이동 플래그; 움직이지 않은 우주선 시작
        self.moving_right = False
        self.moving_left = False 

    def update(self):
        '''우주선의 위치를 업데이트'''
        # x값만 업데이트 합니다
        if (self.moving_right and 
            self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        if (self.moving_left and self.rect.left > 0):
            self.x -= self.settings.ship_speed

        # rect객체 업데이트
        self.rect.x = self.x

    def blit_me(self):
        '''우주선을 현재 위치에 그립니다'''
        self.screen.blit(self.image, self.rect)