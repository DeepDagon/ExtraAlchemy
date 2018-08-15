import pyganim
from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from plants import *

move_speed = 10
animationDelay = 0.1

walkRight = ['images/character/walk/right/right_0.png',
'images/character/walk/right/right_1.png', 'images/character/walk/right/right_2.png',
'images/character/walk/right/right_3.png', 'images/character/walk/right/right_4.png',
'images/character/walk/right/right_5.png', 'images/character/walk/right/right_6.png',
'images/character/walk/right/right_7.png', 'images/character/walk/right/right_8.png',
'images/character/walk/right/right_9.png']

walkLeft = ['images/character/walk/left/left_0.png',
'images/character/walk/left/left_1.png', 'images/character/walk/left/left_2.png',
'images/character/walk/left/left_3.png', 'images/character/walk/left/left_4.png',
'images/character/walk/left/left_5.png', 'images/character/walk/left/left_5.png',
'images/character/walk/left/left_7.png', 'images/character/walk/left/left_8.png',
'images/character/walk/left/left_9.png']

walkUp = ['images/character/walk/up/up_0.png',
'images/character/walk/up/up_1.png', 'images/character/walk/up/up_2.png',
'images/character/walk/up/up_3.png', 'images/character/walk/up/up_4.png',
'images/character/walk/up/up_5.png', 'images/character/walk/up/up_6.png',
'images/character/walk/up/up_7.png', 'images/character/walk/up/up_8.png',
'images/character/walk/up/up_9.png']

walkDown = ['images/character/walk/down/down_0.png',
'images/character/walk/down/down_1.png', 'images/character/walk/down/down_2.png',
'images/character/walk/down/down_3.png', 'images/character/walk/down/down_4.png',
'images/character/walk/down/down_5.png', 'images/character/walk/down/down_6.png',
'images/character/walk/down/down_7.png', 'images/character/walk/down/down_8.png',
'images/character/walk/down/down_9.png']


animationStay = ['images/character/stand/down/standdown_0.png']

class Player(Sprite):
	def __init__(self, x, y):
		Sprite.__init__(self)
		self.state = None
		self.image = Surface((120, 120))
		self.xvel = 0
		self.yvel = 0
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.image.set_colorkey((0, 0, 0))

		def make_boltAnim(anim_list, delay): #Добавляет задержку к каждому кадру
			boltAnim = []
			for cadr in anim_list:
				boltAnim.append((cadr, delay))
			Anim = pyganim.PygAnimation(boltAnim)
			return Anim

		self.boltAnimStay = make_boltAnim(animationStay, animationDelay)
		self.boltAnimStay.play()

		self.boltAnimLeft = make_boltAnim(walkLeft, animationDelay)
		self.boltAnimLeft.play()

		self.boltAnimRight = make_boltAnim(walkRight, animationDelay)
		self.boltAnimRight.play()

		self.boltAnimUp = make_boltAnim(walkUp, animationDelay)
		self.boltAnimUp.play()

		self.boltAnimDown = make_boltAnim(walkDown, animationDelay)
		self.boltAnimDown.play()

	def update(self, left, right, up, down, plantlist):
		if left:
			self.xvel = -move_speed
			self.image.fill((0,0,0))
			self.boltAnimLeft.blit(self.image, (0, 0))
		if right:
			self.xvel = move_speed
			self.image.fill((0,0,0))
			self.boltAnimRight.blit(self.image, (0, 0))
		if up:
			self.yvel = -move_speed
			self.image.fill((0,0,0))
			self.boltAnimUp.blit(self.image, (0, 0))
		if down:
			self.yvel = move_speed
			self.image.fill((0,0,0))
			self.boltAnimDown.blit(self.image, (0, 0))

		if not (left or right):
			self.xvel = 0
		if not (up or down):
			self.yvel = 0

		if not (left or right or up or down):
			self.image.fill((0,0,0))
			self.boltAnimStay.blit(self.image, (0, 0))

		self.rect.x += self.xvel
		self.collide(self.xvel, 0, plantlist)
		self.rect.y += self.yvel
		self.collide(0, self.yvel, plantlist)

	def playerPosition(self):
		return self.rect.x, self.rect.y

	def collide(self, xvel, yvel, plantlist): #Проверяет столкновение игрока с растениями
		for sprite in plantlist:
			if pygame.sprite.collide_rect(self, sprite):
				sprite.is_touched()			
			else:
				sprite.is_untouched()
