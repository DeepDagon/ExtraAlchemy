from pygame import display, image, time, event, init, key
from pygame.locals import *
from Constant import *
from Player import *
#from Plants import *

pygame.init()

#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #Полный экран
screen = pygame.display.set_mode((display_width, display_height)) #Размеры окна
pygame.display.set_caption(display_title) #Надпись вверху окна
background_image = pygame.image.load(background_one) #Фон поля
clock = pygame.time.Clock() #Для FPS

class Sprite:
	def __init__(self, xpos, ypos, filename):
		self.x = xpos
		self.y = ypos
		self.bitmap = pygame.image.load(filename)
		self.bitmap.set_colorkey((0, 0, 0))
	def render(self):
		screen.blit(self.bitmap,(self.x, self.y))
		print("Я РАБОТАЮ")

sunPlants = Sprite(0,0, 'images/plants/sunPlants.png')
shadowPlants = Sprite(200,50, 'images/plants/shadowPlants.png')
waterPlants = Sprite(500,0, 'images/plants/waterPlants.png')

def baserender(): #Рендер всего
	screen.blit(background_image, (0, 0)) #Установка фонового изображения (поле)

	sunPlants.render()
	shadowPlants.render()
	waterPlants.render()
	global animCount, standAnimCount

	if animCount + 1 >= 30:
		animCount = 0
	if standAnimCount + 1 >= 8:
		standAnimCount = 0

	if left or right or up or down:
		if left:
			screen.blit(walkLeft[animCount // 3], (x,y))
			animCount += 1
			print(animCount, left, "Анимация влево")
		if right:
			screen.blit(walkRight[animCount // 3], (x,y))
			animCount += 1
			print(animCount, right, "Анимация вправо", animCount // 3)
		if up:
			screen.blit(walkUp[animCount // 3], (x,y))
			animCount += 1
			print(animCount, up, "Анимация вверх")
		if down:
			screen.blit(walkDown[animCount // 3], (x,y))
			animCount += 1
			print(animCount, down, "Анимаци вниз")
	else:
		screen.blit(stand[standAnimCount // 3], (x,y))
		standAnimCount += 1
		print("Стою")

	pygame.display.update()

def event_handler(): #Идентефикация нажатия на клавиши
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE)):
			pygame.quit()
			isRunning = False

def walk(): #Ходьба
	pygame.init()
	global x, y, width, height, speed
	global display_width, display_height
	global left, right, up, down

	keys = pygame.key.get_pressed()
    
	if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or  keys[pygame.K_DOWN]: 
		if keys[pygame.K_LEFT] and x > 1:
			x -= speed
			left = True
			right = False
			up = False
			down = False
		if keys[pygame.K_RIGHT] and x < display_width - width - 1:
			x += speed
			left = False
			right = True
			up = False
			down = False
			print("Я ИДУ ВПРАВО", x, y)
		if keys[pygame.K_UP] and y > 1:
			y -= speed
			left = False
			right = False
			up = True
			down = False
		if keys[pygame.K_DOWN] and y < display_height - height + 1:
			y += speed
			left = False
			right = False
			up = False
			down = True
	else:
		left = False
		right = False
		up = False
		down = False
		animCount = 0

isRunning = True

while isRunning:
	event_handler()
	walk()
	baserender()
	clock.tick(30)  #Кадров в секунду

pygame.quit()


