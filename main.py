import pygame
from pygame.locals import *
from Constant import *
#from Player import *

pygame.init()

screen = pygame.display.set_mode((display_width, display_height)) #Размеры окна
pygame.display.set_caption(display_title) #Надпись вверху окна
background_image = pygame.image.load(background_one) #Фон поля
clock = pygame.time.Clock() #Для FPS

walkRight = [pygame.image.load('images/character/right_0.png'),
pygame.image.load('images/character/right_1.png'), pygame.image.load('images/character/right_2.png'),
pygame.image.load('images/character/right_3.png'), pygame.image.load('images/character/right_4.png'),
pygame.image.load('images/character/right_5.png'), pygame.image.load('images/character/right_6.png'),
pygame.image.load('images/character/right_7.png'), pygame.image.load('images/character/right_8.png'),
pygame.image.load('images/character/right_9.png')]

walkLeft = [pygame.image.load('images/character/left_0.png'),
pygame.image.load('images/character/left_1.png'), pygame.image.load('images/character/left_2.png'),
pygame.image.load('images/character/left_3.png'), pygame.image.load('images/character/left_4.png'),
pygame.image.load('images/character/left_5.png'), pygame.image.load('images/character/left_5.png'),
pygame.image.load('images/character/left_7.png'), pygame.image.load('images/character/left_8.png'),
pygame.image.load('images/character/left_9.png')]
"""
walkUp = [pygame.image.load('images/character/up_1.png'),
pygame.image.load('images/character/up_2.png'), pygame.image.load('images/character/up_3.png'),
pygame.image.load('images/character/up_4.png'), pygame.image.load('images/character/up_5.png'),
pygame.image.load('images/character/up_6.png'), pygame.image.load('images/character/up_7.png'),
pygame.image.load('images/character/up_8.png'), pygame.image.load('images/character/up_9.png'),
pygame.image.load('images/character/up_10.png')]

walkDown = [pygame.image.load('images/character/down_1.png'),
pygame.image.load('images/character/down_2.png'), pygame.image.load('images/character/down_3.png'),
pygame.image.load('images/character/down_4.png'), pygame.image.load('images/character/down_5.png'),
pygame.image.load('images/character/down_6.png'), pygame.image.load('images/character/down_7.png'),
pygame.image.load('images/character/down_8.png'), pygame.image.load('images/character/down_9.png'),
pygame.image.load('images/character/down_10.png')]
"""


playerStand = pygame.image.load('images/character/stand.png') #Персонаж


def render():
	screen.blit(background_image, (0, 0)) #Установка фонового изображения (поле)

	global animCount

	if animCount + 1 >= 30:
		animCount = 0

	if left:
		screen.blit(walkLeft[animCount // 3], (x,y))
		animCount += 1
		print(animCount, left, "Анимация влево")
	elif right:
		screen.blit(walkRight[animCount // 3], (x,y))
		animCount += 1
		print(animCount, right, "Анимация вправо", animCount // 3)
	elif up:
		#screen.blit(walkUp[animCount // 5], (x,y))
		animCount += 1
		print(animCount, up, "Анимация вверх")
	elif down:
		#screen.blit(walkDown[animCount // 5], (x,y))
		animCount += 1
		print(animCount, down, "Анимаци вниз")
	else:
		screen.blit(playerStand, (x,y))
		print("Стою")

	pygame.display.update()

def event_handler(): #Идентефикация нажатия на клавиши
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE)):
			pygame.quit()
			isRunning = False

def walk():
	pygame.init()

	global x, y, width, height, speed
	global display_width, display_height
	global left, right, up, down

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > 1:
		x -= speed
		left = True
		right = False
	if keys[pygame.K_RIGHT] and x < display_width - width - 1:
		x += speed
		left = False
		right = True
	elif keys[pygame.K_UP] and y > 1:
		y -= speed
		up = True
		down = False
	else:
		left = False
		right = False
		up = False
		down = False
		animCount = 0

	if keys[pygame.K_DOWN] and y < display_height - height + 1:
		y += speed
		up = False
		down = True

isRunning = True

while isRunning:
	clock.tick(30)  #Кадров в секунду
	event_handler()
	walk()
	render()

pygame.quit()


