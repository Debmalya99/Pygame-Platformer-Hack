import pygame
import Config
from .CheckPoint import CheckPoint
from .Platform import Platform

class World:
	def __init__(self,screen_width,screen_height,levels,screen,current_level=0,tile_size=50):
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.levels = levels
		self.screen = screen
		self.tile_size = tile_size
		self.current_level = current_level
		self.world_tiles = []
		self.assets = {}
		self.load_assets()
		self.initialize_tiles()

	# Load game assets
	def load_assets(self):
		# Load the background
		self.background = pygame.image.load(Config.Sprites["background"])
		self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))

		# Create an asset dictionary
		for name, path in Config.Sprites.items():
			if name != "background":
				self.assets[name] =  pygame.image.load(path)

	# Makes an image game object
	def create_tile(self, row, col, name, custom_size, custom_location):
		global tile_size
		global world_tiles

		# default size
		if not custom_size:

			img = pygame.transform.scale(self.assets[name], (self.tile_size, self.tile_size))
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
		global platforms
		global check_points
		global environmentals
		global world_tiles
		global current_level
		
        # self.platforms = None
        # self.check_points = None
        # self.environmentals = None
        # self.world_tiles = None
        # self.current_level = None

		world_tiles = []

		row = 0
		index = 0
		for r in self.levels[self.current_level]:
			col = 0
			for tile in r:
				if (tile == 1):
					self.create_tile(row, col, "ground_1", False, False)

				if (tile == 2):
					self.create_tile(row, col, "ground_2", False, False)

				if (tile == 2.1):	# moving platform (Horizontal)
					platform = Platform(col * tile_size, row * tile_size , 1, 0, self.screen)
					plats[0].add(platform)

				if (tile == 2.2):	# moving platform (Vertical)
					platform = Platform(col * tile_size, row * tile_size , 0, 1, self.screen)
					plats[0].add(platform)

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
					location.append(col * self.tile_size)
					location.append(row * self.tile_size + 50)
					self.create_tile(row, col, "grass_1", False, location)

				if (tile == 13):
					location = []
					location.append(col * self.tile_size)
					location.append(row * self.tile_size + 50)
					self.create_tile(row, col, "grass_2", False, location)

				if (tile == 14):
					location = []
					location.append(col * self.tile_size)
					location.append(row * self.tile_size + 50)
					self.create_tile(row, col, "grass_3", False, location)

				if (tile == 15):
					location = []
					location.append(col * self.tile_size)
					location.append(row * self.tile_size + 50)
					self.create_tile(row, col, "grass_4", False, location)

				if (tile == 16):
					location = []
					location.append(col * self.tile_size)
					location.append(row * self.tile_size + 50)
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
					check = CheckPoint(col * self.tile_size, row * self.tile_size, self.screen)
					check_points[0].add(check)

				if (tile == 24):
					lava = Lava(col * self.tile_size, row * self.tile_size, self.screen)
					lava_tiles[0].add(lava)

				index += 1
				col += 1
			row += 1

		# reverse the list so assets are drawn from bottom to top
		world_tiles = [ele for ele in reversed(world_tiles)]

	# Draw the background
	def draw_world(self):
		self.screen.blit(self.background, (0, 0))

	# Draw the world data from the tiles we created
	def draw_tiles(self):
		if world_tiles:
			for tile in world_tiles:
				self.screen.blit(tile[0], tile[1])
