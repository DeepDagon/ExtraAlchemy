from pygame.sprite import Sprite
from pygame.image import load

class sunPlants(Sprite):
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = load('images/plants/sunPlants.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class shadowPlants(Sprite):
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = load('images/plants/shadowPlants.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class waterPlants(Sprite):
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.image = load('images/plants/waterPlants.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y