import pygame
from pygame.sprite import Sprite
class Button(Sprite):
    def __init__(self,jensoo,msg):
        super().__init__()
        self.screen=jensoo.screen
        self.screen_rect=self.screen.get_rect()
        self.button_color=(71,68,68)
        self.text_color=(255,255,255)
        self.font=pygame.font.Font(pygame.font.get_default_font(),30)
        self.rect=pygame.Rect(0,0,300,50)
        self.rect.center=self.screen_rect.center
        self.play_msg(msg)
     
    def play_msg(self,msg):
        self.text_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.text_image_rect=self.text_image.get_rect()
        self.text_image_rect.center=self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.text_image,self.text_image_rect)

