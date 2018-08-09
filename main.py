import pygame
from pygame.locals import *
from player import *
from pyganim import *
from plants import Plants
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
sprite_group.add(hero)
plantslist = []

XRandPos = random.randint(260, 1105) #Для рандомной генерации растений на поле
YRandPos = random.randint(256, 512)

PlantsRender = Plants(XRandPos, YRandPos)
sprite_group.add(PlantsRender)
plantslist.append(PlantsRender)

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
