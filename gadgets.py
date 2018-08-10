from pygame.sprite import Sprite
from pygame.image import load

class lamp(Sprite):
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = load('images/lamp/lampOn.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class bucket(Sprite):
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = load('images/bucket/bucketFull.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
