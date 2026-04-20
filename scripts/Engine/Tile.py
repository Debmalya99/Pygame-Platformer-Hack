import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import pygame
import GameGlobals as gg
import Config
from EngineMath import Vector2

from Servers.RenderingServer import RenderingServer

from enum import Enum

class Tile:
    def __init__(
            self,
            position: Vector2,
            image:pygame.image,
            tile_size:Vector2 = None,
            rect:pygame.rect = None,

    ):
        self.position = position
        self.image = image
        self.rect = rect
        self.tile_size = tile_size

        if tile_size is not None: ## i.e. we wish to have a custom tile size
            self.image = pygame.transform.scale(self.image,self.tile_size.as_list())
            self.rect = self.image.get_rect()

        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def render(self,rserver:RenderingServer,z_index:int):
        rserver.add_drawable(self.image,self.rect,z_index)

    def get_rect(self):
        return self.rect

        



