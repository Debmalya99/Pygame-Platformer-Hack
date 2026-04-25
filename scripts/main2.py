import os
import sys
import pygame
import importlib
import importlib.util

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),".")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"MOD")))

from MOD.GameState import GameState,gg

### Main Loop. Event the initialization is being done in the main loop.

pygame.init()
pygame.mixer.init()
gg.screen = pygame.display.set_mode((gg.screen_width,gg.screen_height))
pygame.display.set_caption(gg.window_title)

## Load the level
level_file = os.path.join(os.getcwd(),'MOD','simple_level.py')
module_name = os.path.splitext(os.path.basename(level_file))[0]
_spec = importlib.util.spec_from_file_location(module_name,level_file)
level = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(level)

while(gg.is_running):
	gg.clock.tick(gg.FPS)
	gg.events = pygame.event.get()
	for _event in gg.events:
		if _event.type == pygame.QUIT:
			gg.is_running = False


	gg.screen.fill(gg.DEAFULT_BLUE)

	## Here be the rendering functions
	# gg.tileset.draw_tile('grass',(100,100),gg.screen)
	for tile in level.TILES:
		gg.tileset.draw_tile(
			tile['name'],
			tile['loc'],
			gg.screen
		)

	pygame.display.flip()

pygame.quit()