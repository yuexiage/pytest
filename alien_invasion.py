import sys
import pygame
from ship import Ship
import game_functions as gf
from settings import Settings
from pygame.sprite import Group
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.window_title)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 更新飞船位置
        ship.update()
        bullets.update()
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)
run_game()

