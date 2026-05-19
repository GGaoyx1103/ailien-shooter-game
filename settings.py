class Settings:
    def __init__(self):
        self.screen_width=1290
        self.screen_height=723
        self.bg_color=(250,204,213)
        self.fleet_drop=5
        self.policeman_limit=3
        self.speedup_scale=1.1
        self.point_increment=1.5
        self._initialize_settings()

    def _initialize_settings(self):
        self.policeman_speed=2.5
        self.bullet_speed=4.0
        self.alien_speed=1.0
        self.alien_point=50
        self.fleet_direction=1
    
    def _initialize_settings_l2(self):
        self.alien_speed=1.5
        
    def _initialize_settings_l3(self):
        self.alien_speed=2


    def speed_up(self):
        self.policeman_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_point *= self.point_increment

    
        