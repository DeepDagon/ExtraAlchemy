import pygame
from pygame.locals import *
from var import *

pygame.init()

screen = pygame.display.set_mode((display_width, display_height)) #Размеры окна
pygame.display.set_caption(display_title) #Надпись вверху окна
background_image = pygame.image.load('images/background.jpg')


def event_handler(): #Идентефикация нажатия на клавиши
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE)):
			pygame.quit()
			quit()

while True:
	pygame.time.delay(60)
	screen.blit(background_image, (0, 0)) #Установка фонового изображения (поле)
	event_handler()
	pygame.draw.rect(screen, (0,0,255), (x,y, width, height)) #Персонаж
	pygame.display.update()
