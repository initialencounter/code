import pygame
import os

pygame.init()
screen = pygame.display.set_mode((220, 100))
pygame.display.set_caption("键盘事件")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

def drawt(content):
    pygame.font.init()
    font = pygame.font.Font("sans.ttf", 100)
    text_sf = font.render(content, True, pygame.Color(0, 0, 0), pygame.Color(255,255,255))
    return text_sf
def anjian():
    keys = pygame.key.get_pressed()  # 检查按键是按下
    if keys[pygame.K_f]:
        screen.blit(background, (0, 0))  # 清除绘图窗口
        screen.blit(drawt("f"), (0, 0))
        os.system('./adb shell input tap 270 960')
    if keys[pygame.K_d]:
        screen.blit(background, (0, 0))  # 清除绘图窗口
        screen.blit(drawt("d"), (0, 0))
        os.system('./adb shell input tap 2200 730')
    if keys[pygame.K_1]:
        screen.blit(background, (0, 0))  # 清除绘图窗口
        screen.blit(drawt("1"), (0, 0))
        os.system('./adb shell input tap 600 300')
    if keys[pygame.K_2]:
        screen.blit(background, (0, 0))  # 清除绘图窗口
        screen.blit(drawt("2"), (0, 0))
        os.system('./adb shell input tap 970 300')
    if keys[pygame.K_3]:
        screen.blit(background, (0, 0))  # 清除绘图窗口
        screen.blit(drawt("3"), (0, 0))
        os.system('./adb shell input tap 1330 300')
    if keys[pygame.K_4]:
        screen.blit(background, (0, 0))  # 清除绘图窗口
        screen.blit(drawt("4"), (0, 0))
        os.system('./adb shell input tap 1730 300')
    if keys[pygame.K_5]:
        screen.blit(background, (0, 0))  # 清除绘图窗口
        screen.blit(drawt("5"), (0, 0))
        os.system('./adb shell input tap 2100 300')
    if keys[pygame.K_l]:
        screen.blit(background, (0, 0))  # 清除绘图窗口
        screen.blit(drawt("lock"), (0, 0))
        os.system('./adb shell input tap 2222 555')

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)  # 每秒执行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    anjian()
    pygame.display.update()
pygame.quit()
