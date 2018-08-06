import pygame
from Constant import *

def walk():
	pygame.init()

	global x, y, width, height, speed
	global display_width, display_height
	global left, right

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > 1:
		x -= speed
		left = True
		right = False
	if keys[pygame.K_RIGHT] and x < display_width - width - 1:
		x += speed
		right = True
		left = False
	elif keys[pygame.K_UP] and y > 1:
		y -= speed
	else:
		left = False
		right = False
		animCount = 0

	if keys[pygame.K_DOWN] and y < display_height - height + 1:
		y += speed	

