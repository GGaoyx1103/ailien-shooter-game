import pygame
import pygame.font

class Score:
    def __init__(self,jensoo):
        self.screen=jensoo.screen
        self.screen_rect=self.screen.get_rect()
        self.jensoo=jensoo
        self.settings=jensoo.settings
        self.stats=jensoo.game_stats
        original_image=pygame.image.load("image\\femaleofficer.bmp").convert()
        self.small_image=pygame.transform.scale(original_image,(50,50))
        self.text_color=(0,0,0)
        self.font=pygame.font.Font(pygame.font.get_default_font(),25)
        self.prep_score()
        self.prep_high_score()
        self.pre_level()
        self.show_policeman()

    def prep_score(self):
        sc=int(round(self.stats.score,-1))
        str_score=f"score:{sc}"
        self.score_image=self.font.render(str_score,True,
                                          self.text_color,self.settings.bg_color)
        self.score_image_rect=self.score_image.get_rect()
        self.score_image_rect.right=self.screen_rect.width-20
        self.score_image_rect.top=5

    def prep_high_score(self):
        sc=int(round(self.stats.score_highest,-1))
        sc_high=f"the highest score:{sc}"
        self.high_score_image=self.font.render(sc_high,True,
                                          self.text_color,self.settings.bg_color)
        self.high_score_image_rect=self.high_score_image.get_rect()
        self.high_score_image_rect.centerx=self.screen_rect.centerx
        self.high_score_image_rect.top=10

    def pre_level(self):
        level=self.stats.level
        self.show_level=f"level:{level}"
        self.level_image=self.font.render(self.show_level,True,
                                          self.text_color,self.settings.bg_color)
        self.level_image_rect=self.level_image.get_rect()
        self.level_image_rect.right=self.screen_rect.width-20
        self.level_image_rect.top=self.score_image_rect.bottom+10

    def show_policeman(self):
        self.policemans=pygame.sprite.Group()
        for policeman_number in range(self.stats.policeman_left):
            small_police=pygame.sprite.Sprite()            
            small_police.image=self.small_image
            small_police.rect=small_police.image.get_rect()
            small_police.rect.x=10+policeman_number*small_police.rect.width
            small_police.rect.y=10
            self.policemans.add(small_police)

    def show_score(self):
        self.screen.blit(self.score_image,self.score_image_rect)
        self.screen.blit(self.high_score_image,self.high_score_image_rect)
        self.screen.blit(self.level_image,self.level_image_rect)
        self.policemans.draw(self.screen)
