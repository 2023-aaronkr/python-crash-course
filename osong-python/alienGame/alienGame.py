# alienGame.py
# python -m pip install --user pygame (pygame 설치)

import sys
import pygame # 설치해야 됩니다

from settings import Settings
from ship import Ship
from laser import Laser

class AlienGame:
    '''게임 자원과 동작을 전체적으로 관리하는 클래스'''

    def __init__(self): # constructor 함수 (초기화)
        '''게임을 초기화하고 게임 자원을 만듭니다'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        ))
        pygame.display.set_caption("Alien Game!")

        self.ship = Ship(self)
        self.lasers = pygame.sprite.Group()

    def run_game(self):
        '''게임의 메인 루프를 시작합니다'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_lasers()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # 키보드와 마우스 이벤트에 응답합니다
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # 키 다운 이벤트에 응답합니다
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_laser()

    def _check_keyup_events(self, event):
        # 키 업 이벤트에 응답합니다
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_laser(self):
        '''새로운 레이저를 만들고 레이저의 그룹에 추가합니다'''
        if len(self.lasers) < self.settings.laser_allowed:
            new_laser = Laser(self)
            self.lasers.add(new_laser)

    def _update_lasers(self):
        '''모든 레이저의 위치를 업데이트하고 사용한 레이저를 제거합니다'''
        self.lasers.update()

        # 사용한 레이저를 제거합니다
        for lz in self.lasers.copy():
            if lz.rect.bottom <= 0:
                self.lasers.remove(lz)

    def _update_screen(self):
        # 루프를 반복할 때마다 화면을 다시 그립니다
        self.screen.fill(self.settings.bg_color)
        for lz in self.lasers.sprites():
            lz.draw_laser()
        
        self.ship.blit_me()

        # 가장 최근 그린 화면을 표시합니다
        pygame.display.flip()
        

if __name__ == '__main__':
    # 게임 인스턴스를 만들고 게임을 실행합니다
    ag = AlienGame()
    ag.run_game()