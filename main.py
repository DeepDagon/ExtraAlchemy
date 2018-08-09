import pygame
from pygame.locals import *
from player import *
from pyganim import *
from plants import *
import random

pygame.init()

#Объявляем переменные
SIZE = (1366, 768) # Группируем ширину и высоту в одну переменную
background_one = 'images/backgrounds/background_one.png'
win_title = 'ЭкстраАлхимия'

screen = pygame.display.set_mode((SIZE)) #Размеры окна
pygame.display.set_caption(win_title) #Надпись вверху окна
background_image = pygame.image.load(background_one) #Фон поля
clock = pygame.time.Clock() #Для FPS

#Создание героя
hero = Player(550, 550)
left = right = up = down = False

#Группируем спрайты
sprite_group = pygame.sprite.Group()
#ungenplant = [sunPlants, shadowPlants, waterPlants] #Список растений
plantslist = [] #Список со всеми сгенерированными растениями

sunlist = []
shadowlist = []
waterlist = []
i = 0

while i < 5:

	XRandPos = random.randint(100, 1266) #Для рандомной генерации растений на поле
	YRandPos = random.randint(98, 670)
	PlantsRender = sunPlants(XRandPos, YRandPos)
#	sunlist.append(PlantsRender)
	sprite_group.add(PlantsRender)
	plantslist.append(PlantsRender)

	XRandPos = random.randint(100, 1266) #Для рандомной генерации растений на поле
	YRandPos = random.randint(98, 670)
	PlantsRender = shadowPlants(XRandPos, YRandPos)
#	shadowlist.append(PlantsRender)
	sprite_group.add(PlantsRender)
	plantslist.append(PlantsRender)

	XRandPos = random.randint(100, 1266) #Для рандомной генерации растений на поле
	YRandPos = random.randint(98, 670)
	PlantsRender = waterPlants(XRandPos, YRandPos)
	sprite_group.add(PlantsRender)
	plantslist.append(PlantsRender)
#	waterlist.append(PlantsRender)

	i += 1

#sprite_group.add(sunlist, shadowlist, waterlist)
sprite_group.add(hero)

def baserender(): #Рендер всего
	screen.blit(background_image, (0, 0)) #Установка фонового изображения (поле)
	
	hero.update(left, right, up, down, plantslist)
	sprite_group.draw(screen)

	pygame.display.update()

isRunning = True

while isRunning:
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

	clock.tick(60)  #Кадров в секунду
