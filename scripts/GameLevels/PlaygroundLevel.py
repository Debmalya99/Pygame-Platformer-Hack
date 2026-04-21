import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from Engine.BaseLevel import BaseLevel
import GameGlobals as gg

from Engine.Character import Character

class PlaygroundLevel(BaseLevel):
    def __init__(self):
        super().__init__()

    def init_level(self):
        self.player:Character = Character(0,gg.screen_height - 130)
    
    def update(self, dt):
        self.player.draw_player()