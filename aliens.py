import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,jensoo):
        super().__init__()
        self.screen=jensoo.screen
        self.image=pygame.image.load("image\cutealien.bmp")
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=(self.rect.height)/2
        self.x=float(self.rect.x)
        self.settings=jensoo.settings

    def update(self):
        self.x += (self.settings.alien_speed)*(self.settings.fleet_direction)
        self.rect.x=self.x

    def check_edges(self):
        return (self.rect.right >= self.settings.screen_width) or (self.rect.left <= 0)
