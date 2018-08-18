from threading import Thread
import time
import random
import pygame
from pygame.locals import *
from player import *
from plants import *
from gadgets import *
from Buttons import *

pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()

# Настройка игрового окна
SIZE = (1366, 768)  # Группируем ширину и высоту в одну переменную
background_one = 'images/backgrounds/background_one.png'  # Фон первого уровня
background_night_path = 'images/backgrounds/night.png'  # Путь до ночной маски
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
night_start = pygame.mixer.Sound('sound/night start/1.ogg')
night_end = pygame.mixer.Sound('sound/night end/1.ogg')
sound_end = pygame.mixer.Sound('sound/start round/1.ogg')
sound_taking = pygame.mixer.Sound('sound/green/1.ogg')
sound_lamp = pygame.mixer.Sound('sound/lights/1.ogg')
sound_bucket = pygame.mixer.Sound('sound/water/1.ogg')
sound_umbrella = pygame.mixer.Sound('sound/umbrella/1.ogg')
sound_click = pygame.mixer.Sound('sound/click/1.ogg')

# Настройка шрифтов
my_font = pygame.font.Font(None, 72)
irina_font = pygame.font.SysFont('IrinaCCT', 64)
gadget_font = pygame.font.SysFont('IrinaCCT', 52)

# Создание героя
hero = Player(550, 550)
left = right = up = down = False

# Группируем спрайты
sprite_group = pygame.sprite.Group()
plantslist = []  # Список со всеми сгенерированными растениями


def genworld():
    i = 0
    XPos = 200
    YPos = 140

    while i < 5:
        PlantsRender = sunPlants(XPos, YPos)
        sprite_group.add(PlantsRender)
        plantslist.append(PlantsRender)

        YPos += 110
        i += 1

    i = 0
    XPos = 650
    YPos = 140

    while i < 5:
        PlantsRender = shadowPlants(XPos, YPos)
        sprite_group.add(PlantsRender)
        plantslist.append(PlantsRender)

        YPos += 110
        i += 1

    i = 0
    XPos = 1100
    YPos = 140

    while i < 5:
        PlantsRender = waterPlants(XPos, YPos)
        sprite_group.add(PlantsRender)
        plantslist.append(PlantsRender)

        YPos += 110
        i += 1


genworld()
sprite_group.add(hero)

#Количество "гаджетов"
umbrellaNumber = 5
lampNumber = 5
bucketNumber = 5

#Рендер всего
def baserender():
    # Установка фонового изображения (поле)
    screen.blit(background_image, (0, 0))
    screen.blit(my_font.render(time_info, 1, (253, 234, 168)), (400, 20))

    screen.blit(gadget_font.render(umbrellaInfo, 1, (253, 234, 168)), (10, 10))   
    screen.blit(gadget_font.render(lampInfo, 1, (253, 234, 168)), (10, 50))   
    screen.blit(gadget_font.render(bucketInfo, 1, (253, 234, 168)), (10, 90)) 

    hero.update(left, right, up, down, plantslist)
    sprite_group.draw(screen)


seconds = 0

sunTime = sunPlants(0, 0).time
shadowTime = shadowPlants(0, 0).time
waterTime = waterPlants(0, 0).time

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

#Третий этап
ThirdStage = False

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
        if event.type == pygame.locals.QUIT or (event.type == pygame.locals.KEYDOWN and (event.key == pygame.locals.K_ESCAPE)):
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

            if event.key == pygame.K_l and lampNumber > 0:
                PlantsRender = lamp(playerPositionX, playerPositionY)
                sprite_group.add(PlantsRender)
                sound_lamp.play()
                lampNumber -= 1

            if event.key == pygame.K_b and bucketNumber > 0:
                PlantsRender = bucket(playerPositionX, playerPositionY)
                sprite_group.add(PlantsRender)
                sound_bucket.play()
                bucketNumber -= 1

            if event.key == pygame.K_u and umbrellaNumber > 0:
                PlantsRender = umbrella(playerPositionX, playerPositionY)
                sprite_group.add(PlantsRender)
                sound_umbrella.play()
                umbrellaNumber -= 1

            if event.key == pygame.K_s:
                if seconds >= 80 and seconds < 100 and sunTime > 80:
                    sunTime = 0
                    NumberSunPlants += 5
                    sound_taking.play()

                if seconds >= 140 and seconds < 160 and shadowTime > 140:
                    shadowTime = 0
                    NumberShadowPlants += 5
                    sound_taking.play()

                if seconds >= 180 and seconds < 200 and waterTime > 180:
                    waterTime = 0
                    NumberWaterPlants += 5
                    sound_taking.play()

    if seconds in range (0, 101):
        baserender()
        if soundValue == 1:
            soundtrack_day.play()
            soundValue = 2

        if seconds in range (80, 101):
            screen.blit(my_font.render(
                'Скорее собирай солнечные растения!', 1, (253, 234, 168)), (200, 70))

    elif seconds in range (101, 201):
        baserender()
        if soundValue == 2:
            night_start.play()
            soundtrack_night.play()
            soundValue = 3

        if seconds in range (140, 160):
            screen.blit(my_font.render(
                'Скорее собирай сумеречные растения!', 1, (253, 234, 168)), (200, 70))

        if seconds in range(180, 200):
            screen.blit(my_font.render(
                'Скорее собирай водные растения!', 1, (253, 234, 168)), (210, 70))

        screen.blit(night_mask, (0, 0)) #Ночь

    elif seconds == 200:
        baserender()
        sound_end.play()

    elif seconds > 200:
        if soundValue == 3:
            soundtrack_cook.play(-1)
            soundValue = 0

        screen.blit(cook_level, (0, 0))
        screen.blit(irina_font.render(sunNumberInfo,
                                      1, (253, 234, 168)), (150, 30))
        screen.blit(irina_font.render(shadowNumberInfo,
                                      1, (253, 234, 168)), (450, 80))
        screen.blit(irina_font.render(waterNumberInfo,
                                      1, (253, 234, 168)), (500, 130))

        desertButton.create_button(screen, (107, 142, 35), 300, 200, 250, 100, 0,
                              "Пустынное зелье", (255, 255, 255))
        sunsetButton.create_button(screen, (107, 142, 35), 600, 200, 250, 100, 0,
                              "Закатное зелье", (255, 255, 255))
        fogButton.create_button(screen, (107, 142, 35), 900, 200, 250, 100, 0,
                              "Туманное зелье", (255, 255, 255))
        invisibleButton.create_button(screen, (107, 142, 35), 300, 350, 250, 100, 0,
                              "Зелье невидимости", (255, 255, 255))
        swampButton.create_button(screen, (107, 142, 35), 600, 350, 250, 100, 0,
                              "Болотное зелье", (255, 255, 255))
        underwaterButton.create_button(screen, (107, 142, 35), 900, 350, 250, 100, 0,
                              "Подводное зелье", (255, 255, 255))
        stopCookButton.create_button(screen, (107, 142, 35), 600, 500, 250, 100, 0,
                              "Закончить варку", (255, 255, 255))

        screen.blit(irina_font.render(DSFnumber, 1, (253, 234, 168)), (300, 620))   
        screen.blit(irina_font.render(ISUnumber, 1, (253, 234, 168)), (290, 680))

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
                    ThirdStage = True
                    sound_end.play()

        if ThirdStage:
            screen.blit(cook_level, (0,0))

            if money == 0:
                moneyInfo = 'Вы ничего не продали'

            elif money == 1 or money == 21:
                moneyInfo = 'Вы получили за зелья: ' + str(money) + ' золотую монету'

            elif money in range(2, 4) or money in range(22, 24): 
                moneyInfo = 'Вы получили за зелья: ' + str(money) + ' золотые монеты'

            elif money in range(5, 20) or money == 25:
                moneyInfo = 'Вы получили за зелья: ' + str(money) + ' золотых монет'

            else:
                moneyInfo = 'Что-то пошло не так :('

            screen.blit(irina_font.render(moneyInfo, 1, (253, 234, 168)), (280, 360))

    else:
        print("Ошибка времени")
        exit()

    pygame.display.update()
    FPS.tick(60)
