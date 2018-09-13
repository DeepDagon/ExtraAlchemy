#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import time
import random
import pygame
from pygame.locals import *
from Player import *
from plants import *
from gadgets import *
from Buttons import *

pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()

# Настройка игрового окна
SIZE = (1280, 720)  # Группируем ширину и высоту в одну переменную (можно указать любые)

x = SIZE[0]/100
y = SIZE[1]/100

background_one = 'images/backgrounds/background_one.png'  # Фон первого уровня
background_night_path = 'images/backgrounds/Night.png'  # Путь до ночной маски
win_title = 'ЭкстраАлхимия'
screen = pygame.display.set_mode((SIZE))  # Размеры окна
pygame.display.set_caption(win_title)  # Надпись вверху окна
background_image = pygame.image.load(background_one)  # Фон поля
night_mask = pygame.image.load(background_night_path)  # Ночь

# Второй уровень
cook_level_background = 'images/backgrounds/background_cook.png'
cook_level = pygame.image.load(cook_level_background)

# Frame per seconds
FPS = pygame.time.Clock()

# Настройка саундтрека
soundtrack_day = pygame.mixer.Sound('sound/Soundtrack/day.ogg')
soundtrack_night = pygame.mixer.Sound('sound/Soundtrack/night.ogg')
soundtrack_cook = pygame.mixer.Sound('sound/Soundtrack/cook.ogg')

# звуки
night_start = pygame.mixer.Sound('sound/Night_start/1.ogg')
night_end = pygame.mixer.Sound('sound/Night_end/1.ogg')
sound_end = pygame.mixer.Sound('sound/Start_round/1.ogg')
sound_taking = pygame.mixer.Sound('sound/Green/1.ogg')
sound_lamp = pygame.mixer.Sound('sound/Lights/1.ogg')
sound_bucket = pygame.mixer.Sound('sound/Water/1.ogg')
sound_umbrella = pygame.mixer.Sound('sound/Umbrella/1.ogg')
sound_click = pygame.mixer.Sound('sound/Click/1.ogg')

# Настройка шрифтов
my_font = pygame.font.Font(None, 70)
irina_font = pygame.font.SysFont('IrinaCCT', 64)
gadget_font = pygame.font.SysFont('IrinaCCT', 52)
small_font = pygame.font.SysFont('IrinaCCT', 40)

# Создание героя
hero_x = SIZE[0]/3
hero_y = SIZE[1]/3
hero = Player(hero_x, hero_y)
left = right = up = down = False

# Группируем спрайты
sprite_group = pygame.sprite.Group()
plantslist = []  # Список со всеми сгенерированными растениями


def genworld():
    XPos = SIZE[0]/6
    YPos = SIZE[1]/6

    PlantsRender = []

    for i in range(1,6):
        PlantsRender.append(sunPlants(XPos, YPos*i))
        PlantsRender.append(shadowPlants(XPos*3, YPos*i))
        PlantsRender.append(waterPlants(XPos*5, YPos*i))

    for plant in PlantsRender:
        sprite_group.add(plant)
        plantslist.append(plant)



genworld()
sprite_group.add(hero)

#Количество "гаджетов"
umbrellaNumber = 5
lampNumber = 5
bucketNumber = 5

#Рендер всего
def baserender():
    color = (253, 234, 168)
    # Установка фонового изображения (поле)
    screen.blit(background_image, (0, 0))
    screen.blit(my_font.render(time_info, 10, color), (x*30, y*2))

    screen.blit(gadget_font.render(umbrellaInfo, 1, color), (x, y))
    screen.blit(gadget_font.render(lampInfo, 1, color), (x, y*5))
    screen.blit(gadget_font.render(bucketInfo, 1, color), (x, y*10))

    hero.update(left, right, up, down, plantslist)
    sprite_group.draw(screen)



seconds = -1

sunTime = sunPlants(0, 0).time
shadowTime = shadowPlants(0, 0).time
waterTime = waterPlants(0, 0).time

#Третий этап
ThirdStage = False
NumberSunPlants = 0
NumberShadowPlants = 0
NumberWaterPlants = 0


def seconds_counter():
    global seconds, sunTime, shadowTime, waterTime
    while True:
        seconds += 1
        sunTime += 1
        shadowTime += 1
        waterTime += 1
        time.sleep(1)


thread = Thread(target=seconds_counter)
thread.start()

soundValue = 1
isRunning = True

#Список зелий
potionlist = ['desert', 'sunset', 'fog', 'invisible', 'swamp', 'underwater']

#Количество зелий
desertNumber = 0
sunsetNumber = 0
fogNumber = 0
invisibleNumber = 0
swampNumber = 0
underwaterNumber = 0

#Кнопки
desertButton = desertButton()
sunsetButton = sunsetButton()
fogButton = fogButton()
invisibleButton = invisibleButton()
swampButton = swampButton()
underwaterButton = underwaterButton()
stopCookButton = stopCookButton()

#Деньги за зелья
money = 0
moneyInfo = ' '

while isRunning:

    #Информация о зельях
    DSFnumber = u'Пустынных: ' + str(desertNumber) + ' Закатных: ' + str(sunsetNumber) + ' Туманных: ' + str(fogNumber)
    ISUnumber = u'Невидимости: ' + str(invisibleNumber) + ' Болотных: ' + str(swampNumber) + ' Водных: ' + str(underwaterNumber)


    playerPositionX, playerPositionY = hero.playerPosition()  # Позиция игрока

    time_info = u'Прошло: ' + str(seconds) + ' сек из 200'
    sunNumberInfo = u'Время истекло, вы собрали ' + str(NumberSunPlants) + ' солнечных растений'
    shadowNumberInfo = str(NumberShadowPlants) + u' сумеречных растений'
    waterNumberInfo = str(NumberWaterPlants) + u' водных растений'

    #Информация о количестве гаджетов
    umbrellaInfo = u'Зонтиков: ' + str(umbrellaNumber)
    lampInfo = u'Ламп: ' + str(lampNumber)
    bucketInfo = u'Вёдер: ' + str(bucketNumber)

    for event in pygame.event.get():
        if (event.type == pygame.locals.QUIT) or ((event.type == pygame.locals.KEYDOWN) and (event.key == pygame.locals.K_ESCAPE)):
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False

            if (event.key == pygame.K_l) and (lampNumber > 0) and (seconds in range(100, 201)):
                PlantsRender = lamp(playerPositionX, playerPositionY)
                sprite_group.add(PlantsRender)
                sound_lamp.play()
                lampNumber -= 1
                sunTime +=5

            if (event.key == pygame.K_b) and (bucketNumber > 0):
                PlantsRender = bucket(playerPositionX, playerPositionY)
                sprite_group.add(PlantsRender)
                sound_bucket.play()
                bucketNumber -= 1
                waterTime += 5

            if (event.key == pygame.K_u) and ((umbrellaNumber > 0) and (seconds in range(0, 101))):
                PlantsRender = umbrella(playerPositionX, playerPositionY)
                sprite_group.add(PlantsRender)
                sound_umbrella.play()
                umbrellaNumber -= 1
                shadowTime +=5

            if event.key == pygame.K_e:
                if waterTime in range(80, 101):
                    waterTime = 201
                    NumberWaterPlants += 5
                    sound_taking.play()

                if shadowTime in range(140, 180):
                    shadowTime = 201
                    NumberShadowPlants += 5
                    sound_taking.play()

                if sunTime in range(180, 200):
                    sunTime = 201
                    NumberSunPlants += 5
                    sound_taking.play()

    color = (253, 234, 168)

    if seconds in range(0, 100):
        baserender()
        if soundValue == 1:
            soundtrack_day.play()
            soundValue = 2

        if waterTime in range(80, 100):
            screen.blit(my_font.render(
                'Скорее собирай водные растения!', 1, color), (x*20, y*10))

    elif seconds in range(100, 201):
        baserender()
        if soundValue == 2:
            night_start.play()
            soundtrack_night.play()
            soundValue = 3

        if shadowTime in range(140, 180):
            screen.blit(my_font.render(
                'Скорее собирай сумеречные растения!', 1, color), (x*20, y*10))

        if sunTime in range(180, 200):
            screen.blit(my_font.render(
                'Скорее собирай солнечные растения!', 1, color), (x*20, y*10))

        screen.blit(night_mask, (0, 0)) #Ночь

    elif seconds == 200:
        baserender()
        sound_end.play()

    elif seconds > 200:
        if soundValue == 3:
            soundtrack_cook.play(-1)
            soundValue = 0

        screen.blit(cook_level, (0, 0))
        screen.blit(small_font.render(sunNumberInfo,
                                      1, color), (x*15, y*3))
        screen.blit(small_font.render(shadowNumberInfo,
                                      1, color), (x*44, y*7))
        screen.blit(small_font.render(waterNumberInfo,
                                      1, color), (x*48, y*12))

        color = (107, 142, 35)
        white_color = (255, 255, 255)
        desertButton.create_button(screen, color, x*10, y*25, 250, 100, 0,
                              "Пустынное зелье", white_color)
        sunsetButton.create_button(screen, color, x*30, y*25, 250, 100, 0,
                              "Закатное зелье", white_color)
        fogButton.create_button(screen, color, x*50, y*25, 250, 100, 0,
                              "Туманное зелье", white_color)
        invisibleButton.create_button(screen, color, x*10, y*45, 250, 100, 0,
                              "Зелье невидимости", white_color)
        swampButton.create_button(screen, color, x*30, y*45, 250, 100, 0,
                              "Болотное зелье", white_color)
        underwaterButton.create_button(screen, color, x*50, y*45, 250, 100, 0,
                              "Подводное зелье", white_color)
        stopCookButton.create_button(screen, color, x*30, y*65, 250, 100, 0,
                              "Закончить варку", white_color)

        color = (253, 234, 168)

        screen.blit(small_font.render(DSFnumber, 1, color), (x*30, y*80))
        screen.blit(small_font.render(ISUnumber, 1, color), (x*30, y*90))

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT or (event.type == pygame.locals.KEYDOWN
                                                    and (event.key == pygame.locals.K_ESCAPE)):
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if desertButton.pressed(pygame.mouse.get_pos()) and NumberSunPlants >= 2:
                    NumberSunPlants -= 2
                    desertNumber += 1
                    sound_click.play()
                    money += 4

                if sunsetButton.pressed(pygame.mouse.get_pos()) and NumberSunPlants >= 1 and NumberShadowPlants >= 2:
                    NumberSunPlants -= 1
                    NumberShadowPlants -= 2
                    sunsetNumber += 1
                    sound_click.play()
                    money += 4

                if fogButton.pressed(pygame.mouse.get_pos()) and NumberSunPlants >= 2 and NumberWaterPlants >= 1:
                    NumberSunPlants -= 2
                    NumberWaterPlants -= 1
                    fogNumber += 1
                    sound_click.play()
                    money += 4

                if invisibleButton.pressed(pygame.mouse.get_pos()) and NumberShadowPlants >= 2:
                    NumberShadowPlants -= 2
                    invisibleNumber += 1
                    sound_click.play()
                    money += 5

                if swampButton.pressed(pygame.mouse.get_pos()) and NumberShadowPlants >= 2 and NumberWaterPlants >= 2:
                    NumberShadowPlants -= 2
                    NumberWaterPlants -= 2
                    swampNumber += 1
                    sound_click.play()
                    money += 4

                if underwaterButton.pressed(pygame.mouse.get_pos()) and NumberSunPlants >= 1 and NumberShadowPlants >= 1 and NumberWaterPlants >= 1:
                    NumberSunPlants -= 1
                    NumberShadowPlants -= 1
                    NumberWaterPlants -= 1
                    underwaterNumber += 1
                    sound_click.play()
                    money += 5

                if stopCookButton.pressed(pygame.mouse.get_pos()):
                    seconds = 201
                    ThirdStage = True
                    sound_end.play()

        if ThirdStage:
            color = (253, 234, 168)
            screen.blit(cook_level, (0,0))
            screen.blit(irina_font.render('Спасибо за прохождение игры!', 1, color), (x*15, y*5))
            screen.blit(irina_font.render('Разработчик: vk.com/val_kd', 1, color), (x*15, y*10))
            screen.blit(irina_font.render('Композитор: vk.com/pointerwar', 1, color), (x*15, y*15))
            screen.blit(irina_font.render('Графика: vk.com/20usa22', 1, color), (x*15, y*20))
            screen.blit(irina_font.render('Группа игры: vk.com/fastprogram', 1, color), (x*15, y*25))

            if seconds > 200:
                if money == 0:
                    moneyInfo = 'Вы ничего не продали'
                    screen.blit(irina_font.render(moneyInfo, 1, color), (x*25, y*36))

                elif money == 1 or money == 21:
                    moneyInfo = 'Вы получили за зелья: ' + str(money) + ' золотую монету'
                    screen.blit(irina_font.render(moneyInfo, 1, color), (x*15, y*36))

                elif money in range(2, 5) or money in range(22, 25):
                    moneyInfo = 'Вы получили за зелья: ' + str(money) + ' золотые монеты'
                    screen.blit(irina_font.render(moneyInfo, 1, color), (x*15, y*36))

                elif money in range(5, 21) or money == 25:
                    moneyInfo = 'Вы получили за зелья: ' + str(money) + ' золотых монет'
                    screen.blit(irina_font.render(moneyInfo, 1, color), (x*15, y*36))

                else:
                    moneyInfo = 'Что-то пошло не так :('
                    screen.blit(irina_font.render(moneyInfo, 1, color), (x*22, y*36))

    else:
        print("Ошибка времени")
        exit()

    pygame.display.update()
    FPS.tick(60)
