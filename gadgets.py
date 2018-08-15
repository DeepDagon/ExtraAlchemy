import pygame
from pygame.sprite import Sprite
from pygame.image import load

class lamp(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = load('images/lamp/lampOn.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class bucket(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = load('images/bucket/bucketFull.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class tent(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = load('images/tent/tent.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
