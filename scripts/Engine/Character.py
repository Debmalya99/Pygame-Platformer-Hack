import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import pygame
import GameGlobals as gg
import Config
from BasicPhysics import *

class Character():
	def __init__(self, x, y):
		# images
		self.idle_right = []
		self.idle_left = []

		self.run_right = []
		self.run_left = []

		self.death_right = []
		self.death_left = []

		self.jump_right = []
		self.jump_left = []

		self.img_index = 0 # current frame
		self.counter = 0 # animation speed
		self.death_counter = 0

		# load assets
		self.load_assets()
		self.image = self.idle_right[self.img_index] # first frame

		# coordinates
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.rect.w = self.image.get_width()
		self.rect.h = self.image.get_height()

		self.direction = 0
		self.vel_y = 0
		self.jumped = False
		self.in_air = False

		self.animation = "idle"
		self.cool_down = 10 # wait 10 frames before next img animation


	# get the character rect
	def get_rect(self):
		return self.rect 
	
	# get the character position
	def get_position(self):
		return [self.rect.x,self.rect.y]

	# Load all character images
	def load_assets(self):
		for name, path in Config.Player.items():
			img = pygame.image.load(path)
			img = pygame.transform.scale(img, (gg.tile_size, gg.tile_size))
			img_left = pygame.transform.flip(img, True, False)

			if 'idle' in name:
				self.idle_right.append(img)
				self.idle_left.append(img_left)

			if 'run' in name:
				self.run_right.append(img)
				self.run_left.append(img_left)

			if 'fall' in name:
				self.fall_right.append(img)
				self.fall_left.append(img_left)

			if 'death' in name:
				self.death_right.append(img)
				self.death_left.append(img_left)

			if 'jump' in name:
				self.jump_right.append(img)
				self.jump_left.append(img_left)

	# handle idle animation
	def idle_animation(self):
		if self.counter > self.cool_down:
			self.img_index += 1
			self.counter = 0

		if self.img_index >= len(self.idle_right):
			self.img_index = 0

		if self.direction == 1 or self.direction == 0:
			self.image = self.idle_right[self.img_index]

		if self.direction == -1:
			self.image = self.idle_left[self.img_index]

	# handle jump animation
	def jump_animation(self):
		if self.counter > self.cool_down:
			self.img_index += 1
			self.counter = 0

		if self.img_index >= len(self.jump_right):
			self.img_index = 0

		if self.direction == 1 or self.direction == 0:
			self.image = self.jump_right[self.img_index]

		if self.direction == -1:
			self.image = self.jump_left[self.img_index]

	# handle running animation
	def run_animation(self):
		if self.counter > self.cool_down:
			self.img_index += 1
			self.counter = 0

		if self.img_index >= len(self.run_right):
			self.img_index = 0

		if self.direction == 1 or self.direction == 0:
			self.image = self.run_right[self.img_index]

		if self.direction == -1:
			self.image = self.run_left[self.img_index]

	# handle death animation
	def death_animation(self):
		game_over = gg.game_over

		if self.death_counter > self.cool_down + 1:
			self.death_counter = 0
			game_over = -1
		else:
			self.img_index += 1

		if self.img_index >= len(self.death_right):
			self.img_index = 0

		if self.direction == 1 or self.direction == 0:
			self.image = self.death_right[self.img_index]

		if self.direction == -1:
			self.image = self.death_left[self.img_index]

		self.death_counter += 1


	# handle key presses
	def controller(self, dx, dy):
		sounds = gg.sounds

		value = []
		key = pygame.key.get_pressed()

		# currently idle
		# if not key[pygame.K_w] or not key[pygame.K_a] or not key[pygame.K_d]:
		if not (gg.input_manager.is_action_pressed('ui_jump') and gg.input_manager.is_action_pressed('ui_left') and gg.input_manager.is_action_pressed('ui_right')):
			self.counter += 1
			self.animation = "idle"

		# currently jumping
		if gg.input_manager.is_action_pressed('ui_jump') and self.jumped == False and self.in_air == False:
			self.vel_y = gg.JUMP_HEIGHT # jump height
			self.jumped = True
			self.counter += 1
			self.animation = "jump"
			gg.sounds[1].play()

		if key[pygame.K_w] == False:
			self.jumped = False

		# currently running right
		if gg.input_manager.is_action_pressed('ui_right'):
			dx += 5
			self.counter += 1
			self.direction = 1
			self.animation = "run"

		# currently running left
		if gg.input_manager.is_action_pressed('ui_left'):
			dx -= 5
			self.counter += 1
			self.direction = -1
			self.animation = "run"

		value.append(dx)
		value.append(dy)
		return value

	# handle player collision ==> This function has been moved to BasicPhysics.py

	# handle the player
	def draw_player(self,collision_callback:callable):
		game_over = gg.game_over
		dx = 0
		dy = 0

		if game_over == 0:
			# input handler
			key = self.controller(dx, dy)
			dx = key[0]
			dy = key[1]

			# animation handling
			if self.animation == "idle":
				self.idle_animation()

			if self.animation == "jump":
				self.jump_animation()

			if self.animation == "run":
				self.run_animation()

			# add gravity
			self.vel_y += 1
			if self.vel_y > 10:
				self.vel_y = 10
			dy += self.vel_y

			# check for collision
			# col = self.collision(dx, dy)
			col = collision_callback(self,dx,dy)
			dx = col[0]
			dy = col[1]

			# handle out of bounds
			if self.rect.x + dx >= -25 and self.rect.x + dx <= 977:
				self.rect.x += dx

			if self.rect.y + dy >= 1000:
				game_over = -1
			else:
				self.rect.y += dy

		# gg.screen.blit(self.image, self.rect)
		gg.rendering_server.add_drawable(self.image,self.rect,2)

