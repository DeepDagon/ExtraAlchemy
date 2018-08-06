import pygame
from pygame.locals import *
from Constant import *
from Player import *

pygame.init()

screen = pygame.display.set_mode((display_width, display_height)) #Размеры окна
pygame.display.set_caption(display_title) #Надпись вверху окна
background_image = pygame.image.load('images/background.jpg') #Фон
clock = pygame.time.Clock() #Для FPS

walkRight = [pygame.image.load('images/character/right_1.png'),
pygame.image.load('images/character/right_2.png'), pygame.image.load('images/character/right_3.png'),
pygame.image.load('images/character/right_4.png'), pygame.image.load('images/character/right_5.png'),
pygame.image.load('images/character/right_6.png')]

walkLeft = [pygame.image.load('images/character/left_1.png'),
pygame.image.load('images/character/left_2.png'), pygame.image.load('images/character/left_3.png'),
pygame.image.load('images/character/left_4.png'), pygame.image.load('images/character/left_5.png'),
pygame.image.load('images/character/left_6.png')]

playerStand = pygame.image.load('images/character/stand.png') #Персонаж


def render():
	screen.blit(background_image, (0, 0)) #Установка фонового изображения (поле)

	global animCount

	if animCount + 1 >= 30:
		animCount = 0

	if left:
		screen.blit(walkLeft[animCount // 5], (x,y))
		animCount += 1
	if right:
		screen.blit(walkRight[animCount // 5], (x,y))
		animCount += 1
	else:
		screen.blit(playerStand, (x,y))

	pygame.display.update()

def event_handler(): #Идентефикация нажатия на клавиши
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE)):
			pygame.quit()
			isRunning = False

isRunning = True

while isRunning:
	clock.tick(30)  #Кадров в секунду
	event_handler()
	walk()
	render()

pygame.quit()


