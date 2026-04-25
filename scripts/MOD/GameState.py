import pygame
from Tile import TileSet
import os

class GameState:
    def __init__(self):

        # Window Related Options and variables
        self.screen_width = 640
        self.screen_height = 480
        self.window_title = "Mega Mod"
        self.FPS = 60
        self.screen = None

        ## Mainloop Related Flags and Variables
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.events = None



        ## Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.GREY = (128,128,128)
        self.DEAFULT_BLUE = (21, 74, 161)

        ## Some Common Game Objects
        self.player_ptr = None

        ## Tilesets
        self.tileset = TileSet(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), ## Mods directory
                'assets',
                'tilemap_packed.png'
            )
        )

        ## Tile definition
        self.tileset.add_tile_definition('grass',pygame.Rect(0,0,18,18))
        self.tileset.add_tile_definition('snow',pygame.Rect(0,72,18,18))
        self.tileset.add_tile_definition('dirt',pygame.Rect(0,36,18,18))

gg:GameState = GameState()