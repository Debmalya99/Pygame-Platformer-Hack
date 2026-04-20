# ------------ imports ------------
import Config
import Levels
from Engine.Button import Button
from Engine.Platform import Platform
from Engine.World import World
from Engine.Character import Character

import random
import pygame
from pygame.locals import *
from pygame import mixer

# # ------------ Globals ------------
import GameGlobals as gg
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------

class Game():
	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 2, 512)
		mixer.init()
		self.fps = gg.FPS
		self.clock = pygame.time.Clock()
		self.game_menu()
		self.start()

	# setup in-game menu
	def game_menu(self):
		play_img = pygame.image.load(Config.UI["play"])
		quit_img = pygame.image.load(Config.UI["quit"])
		continue_img = pygame.image.load(Config.UI["continue"])
		resume_img = pygame.image.load(Config.UI["resume"])

		play_img = pygame.transform.scale(play_img, (200, 70))
		quit_img = pygame.transform.scale(quit_img, (200, 70))
		continue_img = pygame.transform.scale(continue_img, (200, 70))
		resume_img = pygame.transform.scale(resume_img, (200, 70))

		self.play_button = Button(gg.screen_width // 2 - 100, gg.screen_height // 2, play_img)
		self.quit_button = Button(gg.screen_width // 2 - 100, gg.screen_height // 2 + 110, quit_img)
		self.continue_button = Button(gg.screen_width // 2 - 100, gg.screen_height // 2, continue_img)
		self.resume_button = Button(gg.screen_width // 2 - 100, gg.screen_height // 2, resume_img)

	# load sounds
	def sounds(self):
		sounds = gg.sounds

		theme_fx = pygame.mixer.Sound(Config.Sounds["theme"])
		theme_fx.set_volume(0.5)

		jump_fx = pygame.mixer.Sound(Config.Sounds["jump"])
		jump_fx.set_volume(0.5)

		over_fx = pygame.mixer.Sound(Config.Sounds["over"])
		over_fx.set_volume(0.5)

		complete_fx = pygame.mixer.Sound(Config.Sounds["complete"])
		complete_fx.set_volume(0.5)

		gg.sounds.append(theme_fx)
		gg.sounds.append(jump_fx)
		gg.sounds.append(over_fx)
		gg.sounds.append(complete_fx)

		gg.sounds[0].play(-1) # loop game theme

	# resets platform group
	def reset_groups(self):
		plats = gg.plats
		check_points = gg.check_points
		lava_tiles = gg.lava_tiles

		plats = []
		check_points = []
		lava_tiles = []

		self.plat_group.empty()
		self.check_group.empty()
		self.lava_group.empty()

	# create all properties
	def properties(self):
		plats = gg.plats
		check_points = gg.check_points
		lava_tiles = gg.lava_tiles

		self.plat_group = pygame.sprite.Group()
		self.check_group = pygame.sprite.Group()
		self.lava_group = pygame.sprite.Group()

		gg.plats.append(self.plat_group)
		gg.check_points.append(self.check_group)
		gg.lava_tiles.append(self.lava_group)

	# load level
	def load_level(self):
		game_over = gg.game_over

		self.reset_groups()
		self.properties()
		world = World()
		player = Character(0, gg.screen_height - 130)
		game_over = 0

		values = []
		values.append(player)
		values.append(world)
		return values

	# handle level timer
	def game_timer(self):
		current_level = gg.current_level
		timer = 30
		ttext = str(timer)

		self.timer_counter, self.timer_text = timer, ttext.rjust(3)
		pygame.time.set_timer(pygame.USEREVENT, 1000)
		self.timer_font = pygame.font.SysFont('comicsansms', 25)

	# start game functionality
	def start(self):
		in_menu = gg.in_menu
		game_over = gg.game_over
		game_finished = gg.game_finished
		max_levels = gg.max_levels
		current_level = gg.current_level

		self.sounds()
		self.properties()
		world = World()
		player = Character(0, gg.screen_height - 130)
		self.game_timer()

		##  LABEL: MAIN_LOOP
		run = True
		while(run):
			self.clock.tick(self.fps)

			# draw assets onto the screen
			world.draw_world()

			# setup main menu
			if in_menu:
				if self.quit_button.draw():
					run = False
				if self.play_button.draw():
					in_menu = False
			else:
				world.draw_tiles()
				gg.check_points[0].draw(gg.screen)
				gg.lava_tiles[0].draw(gg.screen)
				player.draw_player()

				# player active
				if game_over == 0:
					gg.plats[0].update()

				# player finished level
				if game_over == 1:
					self.timer_counter = 0
					current_level += 1
					values = self.load_level()
					player = values[0]
					world = values[1]

					if current_level == gg.max_levels:
						game_finished = True
					else:
						self.game_timer()
				# player death
				if game_over == -1:
					self.timer_counter = 0
					if self.resume_button.draw():
						values = self.load_level()
						player = values[0]
						world = values[1]
						self.game_timer()
					if self.quit_button.draw():
						run = False

				# player won
				if game_finished:
					self.timer_counter = 0
					if self.quit_button.draw():
						run = False

				gg.plats[0].draw(gg.screen)
				gg.screen.blit(self.timer_font.render(self.timer_text, True, (47, 48, 29)), (60, 42))

			## LABEL: RAW_INPUT_HANDLING
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						# run = False
						in_menu = True

				# game timer
				if event.type == pygame.USEREVENT:
					self.timer_counter -= 1
					if self.timer_counter > 0:
						self.timer_text = str(self.timer_counter).rjust(3)
					else:
						# player ran out of time
						self.timer_text = '0'.rjust(3)
						if not game_finished:
							game_over = -1

			pygame.display.update()

# Start the game
game = Game()
pygame.quit()
