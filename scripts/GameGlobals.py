import pygame
import Config
from pygame import mixer

from Engine.Servers.RenderingServer import RenderingServer


# ------------ Globals ------------

# dimensions: 18 x 20
screen_width = 20*50			# screen width
screen_height = 18*40			# screen height
tile_size = 50
world_tiles = []				# first layer
FPS = 60
GAME_TITLE = "Hackers Union"

## Initializations
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(GAME_TITLE)


### Some Flags
in_menu = True
game_finished = False
game_over = 0 					# Game-Over flag
current_level = 0				# level counter
max_levels = 3					# number of game levels (0 indexed)
score_count = 0					# coin score count

	# --> Sounds
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

sounds = []
menu_sound = False
game_sound = False

plats = []			# group of platforms
check_points = []	# group of checkpoints
lava_tiles = []		# group of lava tiles


### Now let us create the servers
rendering_server = RenderingServer(screen_width,screen_height,screen)