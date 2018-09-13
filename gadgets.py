import pygame
from pygame.sprite import Sprite
from pygame.image import load


class lamp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load('images/lamp/LampOn.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class bucket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load('images/bucket/BucketFull.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class umbrella(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load('images/umbrella/umbrella.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
