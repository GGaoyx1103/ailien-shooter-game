import pygame

class Policeman:
    def __init__(self,jensoo):
        self.screen=jensoo.screen
        self.settings=jensoo.settings
        self.screen_rect=self.screen.get_rect()
        self.image=pygame.image.load("image\\femaleofficer.bmp").convert()
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.policeman_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.policeman_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.policeman_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.policeman_speed
        self.rect.x=self.x
        self.rect.y=self.y

    def re_position(self):
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)