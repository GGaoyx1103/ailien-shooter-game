class GameStats:
    def __init__(self,jensoo):
        self.settings=jensoo.settings
        self.game_reset()
        self.score_highest=0
   
    def game_reset(self):
        self.policeman_left=self.settings.policeman_limit
        self.score=0
        self.level=1