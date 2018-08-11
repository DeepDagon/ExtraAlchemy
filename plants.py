from pygame.sprite import Sprite
from pygame.image import load
import pygame

pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.mixer.init()

class Plants:
	def __init__(self):
		self.touched = False

	def is_touched(self):
		if not self.touched:
			self.touched = True

	def is_untouched(self):
		if  self.touched:
			self.touched = False

class sunPlants(Sprite, Plants):
	def __init__(self, x, y):
		Sprite.__init__(self)
		Plants.__init__(self)
		self.image = load('images/plants/sunPlants.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.word = 'sun'
		self.sunTime = 0

class shadowPlants(Sprite, Plants):
	def __init__(self, x, y):
		Sprite.__init__(self)
		Plants.__init__(self)
		self.image = load('images/plants/shadowPlants.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.word = 'shadow'
		self.shadowTime = 0

class waterPlants(Sprite, Plants):
	def __init__(self, x, y):
		Sprite.__init__(self)
		Plants.__init__(self)
		self.image = load('images/plants/waterPlants.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.word = 'water'
		self.waterTime = 0