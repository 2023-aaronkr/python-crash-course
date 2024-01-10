# settings.py
class Settings:
    '''외계인 침공의 설정을 저장하는 클래스'''
    
    def __init__(self):
        '''게임 설정 초기화'''
        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 30, 30) # 0-255까지 RGB 색갈

        # 우주선 설정
        self.ship_speed = 1.5

        # 레이저 설정
        self.laser_speed = 2.0
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = (255, 0, 0) # red
        self.laser_allowed = 5