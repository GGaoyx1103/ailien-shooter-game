import pygame
import sys
from time import sleep
from settings import Settings
from game_stats import GameStats
from policeman import Policeman
from bullet import Bullet
from aliens import Alien
from button import Button
from score_board import Score

class PowerpuffGirls:
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,
                                             self.settings.screen_height))
        pygame.display.set_caption("The Powerpuff girls")
        self.game_stats=GameStats(self)
        self.is_seleted=False
        self.game_active=False
        self.levels=pygame.sprite.Group()
        self.l2=Button(self,"LEVEL TWO")
        self.l1=Button(self,"LEVEL ONE")   
        self.l3=Button(self,"LEVEL THREE")
        self.button=Button(self,"PLAY")  
        self.policeman=Policeman(self)    
        self.bg_color=self.policeman.image.get_at((0,0))
        self.clock=pygame.time.Clock()
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self.score=Score(self)
        
        self._create_fleet()
        self._select_level()
        
    def _create_fleet(self):
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        x_position,y_position=alien_width,alien_height
        while y_position < self.settings.screen_height-3*alien_height:
            while x_position < self.settings.screen_width-2*alien_width:
                self._create_alien(x_position,y_position)             
                x_position += 2*alien_width
            x_position=alien_width
            y_position += 2*alien_height
    
    def _create_alien(self,x_position,y_position):
        new_alien=Alien(self)
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        new_alien.x=float(new_alien.rect.x)
        self.aliens.add(new_alien)

    def _select_level(self):
        self.l1.rect.y=self.l2.rect.y-2*self.l2.rect.height
        self.l1.text_image_rect.center=self.l1.rect.center
        self.l3.rect.y=self.l2.rect.y+2*self.l2.rect.height
        self.l3.text_image_rect.center=self.l3.rect.center
        self.levels.add(self.l1,self.l2,self.l3)

    def run_game(self):
        while True:
            self._check_event()
            if self.game_active:
                self.policeman.update()
                self._update_bullet()
                self._update_alien()                     
            self._update_screen()       
            self.clock.tick(60)

    def _check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_event_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._check_event_keyup(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    self._check_level(mouse_pos)
    
    def _check_level(self,mouse_pos):
        detect1=self.l1.rect.collidepoint(mouse_pos)
        detect2=self.l2.rect.collidepoint(mouse_pos)
        detect3=self.l3.rect.collidepoint(mouse_pos)
        detect_play=self.button.rect.collidepoint(mouse_pos)
        if not self.is_seleted:
            if detect1 and not self.game_active:
                self._load_game()           
            elif detect2 and not self.game_active:
                self._load_game()
                self.settings._initialize_settings_l2()  
            elif detect3 and not self.game_active:
                self._load_game()
                self.settings._initialize_settings_l3()
        else:
            if detect_play and not self.game_active:
                self.game_active=True
                pygame.mouse.set_visible(False)

    def _load_game(self):
        self.settings._initialize_settings()
        self.game_stats.game_reset()
        self.score.prep_score()
        self.score.pre_level()
        self.score.show_policeman()
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.policeman.re_position()
        self.levels.empty()
        self.is_seleted=True


    def _check_event_keydown(self,event):
        if event.key == pygame.K_RIGHT:
            self.policeman.moving_right=True          
        elif event.key == pygame.K_LEFT:
            self.policeman.moving_left=True
        elif event.key == pygame.K_UP:
            self.policeman.moving_up=True
        elif event.key == pygame.K_DOWN:
            self.policeman.moving_down=True
        elif event.key == pygame.K_SPACE:
            bullet=Bullet(self)
            self.bullets.add(bullet)

    def _check_event_keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.policeman.moving_right=False         
        elif event.key == pygame.K_LEFT:
            self.policeman.moving_left=False
        elif event.key == pygame.K_UP:
            self.policeman.moving_up=False
        elif event.key == pygame.K_DOWN:
            self.policeman.moving_down=False
    
    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.top <= 0:
                    self.bullets.remove(bullet)
        collisions=pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True)
        if collisions:
            for alien in collisions.values():
                self.game_stats.score += self.settings.alien_point*len(alien)
            self.score.prep_score()
            if self.game_stats.score >= self.game_stats.score_highest:
                    self.game_stats.score_highest=self.game_stats.score
                    self.score.prep_high_score()
        if not self.aliens:
            self.bullets.empty()
            self.policeman.re_position()
            self._create_fleet()
            self.settings.speed_up()
            self.game_stats.level += 1
            self.score.pre_level()
           
    def _update_alien(self):
        self.aliens.update()
        self._check_fleet_edge()
        if pygame.sprite.spritecollideany(self.policeman,self.aliens):
            self._policeman_hit()
        self._check_fleet_bottom_edge()

    def _policeman_hit(self):
        if self.game_stats.policeman_left > 0:
            self.game_stats.policeman_left -= 1
            self.score.show_policeman()
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.policeman.re_position()
            sleep(0.5)
        else:
            self.game_active=False
            self._select_level()
            self.is_seleted=False
            pygame.mouse.set_visible(True)
                   
        
    def _check_fleet_bottom_edge(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._policeman_hit()
                break

    def _check_fleet_edge(self):
        for alien in self.aliens.sprites():
                 if alien.check_edges():
                      for alien in self.aliens.sprites():
                           alien.rect.y += self.settings.fleet_drop
                      self.settings.fleet_direction *= -1
                      break
                                        
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.bullets.draw(self.screen)       
        self.policeman.blitme()
        self.aliens.draw(self.screen)
        self.score.show_score()
        if not self.game_active:
            for level in self.levels.sprites():
                level.draw_button()
        if not self.game_active and self.is_seleted:
            self.button.draw_button()
        pygame.display.flip()


jensoo=PowerpuffGirls()
jensoo.run_game()