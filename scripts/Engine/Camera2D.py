import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import pygame
import GameGlobals as gg
import Config

class Camera2D:
    def __init__(self):
        self.position = [0,0]

    def set_position(self,x,y):
        self.position[0] = x
        self.position[1] = y

        offset_x = self.position[0] - gg.screen_width//2
        offset_y = self.position[1] - gg.screen_height//2

    # def transform_vec2(self,_x,_y): ## Basically call this function and use it as you want to
    #     offset_x = self.position[0] - gg.screen_width//2
    #     offset_y = self.position[1] - gg.screen_height//2

    #     return (offset_x,offset_y)

    
        