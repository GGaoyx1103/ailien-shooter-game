import pygame
from pygame.sprite import Sprite
from settings import Settings
class Bullet(Sprite):
    def __init__(self,jensoo):
        super().__init__()
        self.screen=jensoo.screen
        self.settings=Settings()
        self.image=pygame.image.load("image\\bullet.bmp")
        self.rect=self.image.get_rect()
        self.rect.midtop=jensoo.policeman.rect.midtop
        self.y=float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y=self.y

   