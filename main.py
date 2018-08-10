import pygame
from pygame.locals import *
from player import *
from pyganim import *
from plants import *
from pygame import mixer
import random

pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.mixer.init()

#Настройка игрового окна 
SIZE = (1366, 768) # Группируем ширину и высоту в одну переменную
background_one = 'images/backgrounds/background_one.png'
win_title = 'ЭкстраАлхимия'
screen = pygame.display.set_mode((SIZE)) #Размеры окна
pygame.display.set_caption(win_title) #Надпись вверху окна
background_image = pygame.image.load(background_one) #Фон поля

clock = pygame.time.Clock() #Для FPS

#Настройка саундтрека
soundtrack = pygame.mixer.Sound('sound/Soundtrack/01.wav')
#soundtrack.play(-1)

#Настройка шрифтов
time_font = pygame.font.Font(None, 72)
#Создание героя
hero = Player(550, 550)
left = right = up = down = False

#Группируем спрайты
sprite_group = pygame.sprite.Group()
plantslist = [] #Список со всеми сгенерированными растениями

i = 0

while i < 5:

	XRandPos = random.randint(100, 1266) #Для рандомной генерации растений на поле
	YRandPos = random.randint(98, 670)
	PlantsRender = sunPlants(XRandPos, YRandPos)
	sprite_group.add(PlantsRender)
	plantslist.append(PlantsRender)

	XRandPos = random.randint(100, 1266) #Для рандомной генерации растений на поле
	YRandPos = random.randint(98, 670)
	PlantsRender = shadowPlants(XRandPos, YRandPos)
	sprite_group.add(PlantsRender)
	plantslist.append(PlantsRender)

	XRandPos = random.randint(100, 1266) #Для рандомной генерации растений на поле
	YRandPos = random.randint(98, 670)
	PlantsRender = waterPlants(XRandPos, YRandPos)
	sprite_group.add(PlantsRender)
	plantslist.append(PlantsRender)

	i += 1

sprite_group.add(hero)

def baserender(): #Рендер всего
	screen.blit(background_image, (0, 0)) #Установка фонового изображения (поле)
	
	hero.update(left, right, up, down, plantslist)
	sprite_group.draw(screen)

start_ticks = pygame.time.get_ticks() #Запуск таймера
roundValue = 0

isRunning = True

while isRunning:

	seconds	= int((pygame.time.get_ticks()-start_ticks)/1000) #Секунды

	if seconds == 10:
		exit()

	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE)):
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

	baserender()

	time_info = u'Прошло: ' + str(seconds) + ' сек из 300'
	screen.blit(time_font.render(time_info, 1, (253,234,168)), (400, 20))

	clock.tick(60)  #Кадров в секунду
	pygame.display.update()