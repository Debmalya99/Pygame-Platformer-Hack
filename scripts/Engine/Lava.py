import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
import Config
import GameGlobals as gg


class Lava(pygame.sprite.Sprite):
	def __init__(self, x, y, screen):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load(Config.Sprites["lava"])
		self.image = pygame.transform.scale(img, (gg.tile_size, gg.tile_size))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y