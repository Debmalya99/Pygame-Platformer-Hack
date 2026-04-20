import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import pygame
import Config
from Checkpoint import CheckPoint
from Platform import Platform
from Lava import Lava
import Levels
import GameGlobals as gg

from Camera2D import Camera2D


class World():
	def __init__(self,camera:Camera2D=None):
		self.assets = {}
		self.camera:Camera2D = None#camera
		self.load_assets()
		self.initialize_tiles()

	# Load game assets
	def load_assets(self):
		# Load the background
		self.background = pygame.image.load(Config.Sprites["background"])
		self.background = pygame.transform.scale(self.background, (gg.screen_width, gg.screen_height))

		# Create an asset dictionary
		for name, path in Config.Sprites.items():
			if name != "background":
				self.assets[name] =  pygame.image.load(path)

	# Makes an image game object
	def create_tile(self, row, col, name, custom_size, custom_location):
		tile_size = gg.tile_size
		world_tiles = gg.world_tiles

		# default size
		if not custom_size:

			img = pygame.transform.scale(self.assets[name], (tile_size, tile_size))
			img_rect = img.get_rect()

			if not custom_location:
				img_rect.x = col * tile_size
				img_rect.y = row * tile_size
				t = (img, img_rect)
				world_tiles.append(t)
			else:
				img_rect.x = custom_location[0]
				img_rect.y = custom_location[1]
				t = (img, img_rect)
				world_tiles.append(t)

		else:
			img = pygame.transform.scale(self.assets[name], (custom_size[0], custom_size[1]))
			img_rect = img.get_rect()

			if not custom_location:
				img_rect.x = col * tile_size
				img_rect.y = row * tile_size
				t = (img, img_rect)
				world_tiles.append(t)
			else:
				img_rect.x = custom_location[0]
				img_rect.y = custom_location[1]
				t = (img, img_rect)
				world_tiles.append(t)

	# Initialize game tiles
	def initialize_tiles(self):
		# gg.platforms
		# gg.check_points
		# gg.environmentals
		# gg.world_tiles
		# gg.current_level

		world_tiles = []

		row = 0
		index = 0
		for r in Levels.level[gg.current_level]:
			col = 0
			for tile in r:
				if (tile == 1):
					self.create_tile(row, col, "ground_1", False, False)

				if (tile == 2):
					self.create_tile(row, col, "ground_2", False, False)

				if (tile == 2.1):	# moving platform (Horizontal)
					platform = Platform(col * gg.tile_size, row * gg.tile_size , 1, 0, gg.screen)
					gg.plats[0].add(platform)

				if (tile == 2.2):	# moving platform (Vertical)
					platform = Platform(col * gg.tile_size, row * gg.tile_size , 0, 1, gg.screen)
					gg.plats[0].add(platform)

				if (tile == 3):
					self.create_tile(row, col, "ground_3", False, False)

				if (tile == 4):
					self.create_tile(row, col, "ground_4", False, False)

				if (tile == 5):
					self.create_tile(row, col, "ground_5", False, False)

				if (tile == 6):
					self.create_tile(row, col, "ground_6", False, False)

				if (tile == 7):
					self.create_tile(row, col, "ground_7", False, False)

				if (tile == 8):
					self.create_tile(row, col, "ground_8", False, False)

				if (tile == 9):
					self.create_tile(row, col, "ground_9", False, False)

				if (tile == 10):
					self.create_tile(row, col, "ground_10", False, False)

				if (tile == 11):
					self.create_tile(row, col, "ground_11", False, False)

				if (tile == 12):
					location = []
					location.append(col * gg.tile_size)
					location.append(row * gg.tile_size + 50)
					self.create_tile(row, col, "grass_1", False, location)

				if (tile == 13):
					location = []
					location.append(col * gg.tile_size)
					location.append(row * gg.tile_size + 50)
					self.create_tile(row, col, "grass_2", False, location)

				if (tile == 14):
					location = []
					location.append(col * gg.tile_size)
					location.append(row * gg.tile_size + 50)
					self.create_tile(row, col, "grass_3", False, location)

				if (tile == 15):
					location = []
					location.append(col * gg.tile_size)
					location.append(row * gg.tile_size + 50)
					self.create_tile(row, col, "grass_4", False, location)

				if (tile == 16):
					location = []
					location.append(col * gg.tile_size)
					location.append(row * gg.tile_size + 50)
					self.create_tile(row, col, "grass_5", False, location)

				if (tile == 17):
					self.create_tile(row, col, "bush_1", False, False)

				if (tile == 18):
					self.create_tile(row, col, "bush_2", False, False)

				if (tile == 19):
					self.create_tile(row, col, "tree_1", False, False)

				if (tile == 20):
					self.create_tile(row, col, "tree_2", False, False)

				if (tile == 21):
					self.create_tile(row, col, "rock_1", False, False)

				if (tile == 22):
					self.create_tile(row, col, "rock_2", False, False)

				if (tile == 23):
					check = CheckPoint(col * gg.tile_size, row * gg.tile_size, gg.screen)
					gg.check_points[0].add(check)

				if (tile == 24):
					lava = Lava(col * gg.tile_size, row * gg.tile_size, gg.tile_size)
					gg.tile_size[0].add(lava)

				index += 1
				col += 1
			row += 1

		# reverse the list so assets are drawn from bottom to top
		world_tiles = [ele for ele in reversed(world_tiles)]

	# Draw the background
	def draw_background(self):
		gg.screen.blit(self.background, (0, 0))

	# Draw the world data from the tiles we created
	def draw_tiles(self):
		if gg.world_tiles:
			for tile in gg.world_tiles:
				if self.camera != None:
					render_pos = pygame.Vector2(tile[1].topleft) - self.camera.position
					gg.screen.blit(tile[0], render_pos)
				else:
					# gg.screen.blit(tile[0], tile[1])
					gg.rendering_server.add_drawable(tile[0],tile[1],1)
