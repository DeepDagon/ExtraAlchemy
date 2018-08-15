import pygame
from pygame.locals import *
from player import *
from plants import *
from gadgets import *
from threading import Thread
import time

pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.mixer.init()
start_ticks = pygame.time.get_ticks()

#Настройка игрового окна 
SIZE = (1366, 768) # Группируем ширину и высоту в одну переменную
background_one = 'images/backgrounds/background_one.png'
background_night_path = 'images/backgrounds/night.png'
win_title = 'ЭкстраАлхимия'
screen = pygame.display.set_mode((SIZE)) #Размеры окна
pygame.display.set_caption(win_title) #Надпись вверху окна
background_image = pygame.image.load(background_one) #Фон поля
night_mask = pygame.image.load(background_night_path)

clock = pygame.time.Clock() #Для FPS

#Настройка саундтрека
soundtrack_day = pygame.mixer.Sound('sound/Soundtrack/day.wav')
soundtrack_night = pygame.mixer.Sound('sound/Soundtrack/night.wav')

#звуки
night_start = pygame.mixer.Sound('sound/night start/1.wav')
night_end = pygame.mixer.Sound('sound/night end/1.wav')
sound_end = pygame.mixer.Sound('sound/start round/1.wav')
sound_taking = pygame.mixer.Sound('sound/green/1.wav')
sound_lamp = pygame.mixer.Sound('sound/lights/1.wav')
sound_bucket = pygame.mixer.Sound('sound/water/1.wav')
sound_tent = pygame.mixer.Sound('sound/tent build/1.wav')

#Настройка шрифтов
my_font = pygame.font.Font(None, 72)

#Создание героя
hero = Player(550, 550)
left = right = up = down = False

#Группируем спрайты
sprite_group = pygame.sprite.Group()
plantslist = [] #Список со всеми сгенерированными растениями

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
	XPos = 600
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

def baserender(): #Рендер всего
	screen.blit(background_image, (0, 0)) #Установка фонового изображения (поле)
	
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

soundValue = 0
isRunning = True

while isRunning:
	playerPositionX, playerPositionY = hero.playerPosition() #Позиция игрока

	time_info = u'Прошло: ' + str(seconds) + ' сек из 200' 
	sunNumberInfo = u'Время истекло, вы собрали ' + str(NumberSunPlants) + ' солнечных растений'
	shadowNumberInfo = str(NumberShadowPlants) + u' сумеречных растений'
	waterNumberInfo = str(NumberWaterPlants) + u' водных растений'
	baserender()

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
			if event.key == pygame.K_l:
				PlantsRender = lamp(playerPositionX, playerPositionY)
				sprite_group.add(PlantsRender)
				sound_lamp.play()			
			if  event.key == pygame.K_b:
				PlantsRender = bucket(playerPositionX, playerPositionY)
				sprite_group.add(PlantsRender)
				sound_bucket.play()
			if  event.key == pygame.K_t:
				PlantsRender = tent(playerPositionX, playerPositionY)
				sprite_group.add(PlantsRender)
				sound_tent.play()
			if  event.key == pygame.K_s:
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

	if seconds >= 0 and seconds <= 100:		
		screen.blit(my_font.render(time_info, 1, (253,234,168)), (400, 20))
		if soundValue == 0:
			soundtrack_day.play()
			soundValue = 1

		if seconds >= 80 and seconds < 100:
			screen.blit(my_font.render('Скорее собирай солнечные растения!', 1, (253,234,168)), (200, 70))

	elif seconds > 100 and seconds <= 200: #Затухание звуков и музыки перед остановкой
		screen.blit(my_font.render(time_info, 1, (253,234,168)), (400, 20))
		if soundValue == 1:
			night_start.play()		
			soundtrack_night.play()
			soundValue = 2

		screen.blit(night_mask, (0, 0))

		if seconds >= 140 and seconds < 160:
			screen.blit(my_font.render('Скорее собирай сумеречные растения!', 1, (253,234,168)), (200, 70))

		if seconds >= 180 and seconds < 200:
			screen.blit(my_font.render('Скорее собирай водные растения!', 1, (253,234,168)), (200, 70))

	elif seconds == 200:
		sound_end.play()

	elif seconds > 200:
		screen.blit(my_font.render(sunNumberInfo, 1, (253,234,168)), (70, 70))
		screen.blit(my_font.render(shadowNumberInfo, 1, (253,234,168)), (400, 120))
		screen.blit(my_font.render(waterNumberInfo, 1, (253,234,168)), (450, 170))

	else:
		print("Ошибка времени")
		exit()

#	print(sunTime, shadowTime, waterTime, sunReadyStatus, NumberSunPlants, NumberShadowPlants, NumberWaterPlants)
	pygame.display.update()
	clock.tick(60)  #Кадров в секунду