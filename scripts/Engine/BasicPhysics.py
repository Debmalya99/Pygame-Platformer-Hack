import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import pygame
import GameGlobals as gg
import Config

def bp_collision(player_ptr, dx, dy):
		plats = gg.plats
		check_points = gg.check_points
		lava_tiles = gg.lava_tiles
		game_over = gg.game_over
		world_tiles = gg.world_tiles
		game_finished = gg.game_finished
		current_level = gg.current_level
		max_levels = gg.max_levels

		values = []
		collision_thresh = 20 # distance between moving platform in y dir

		player_ptr.in_air = True
		for tile in gg.world_tiles:
			# check for collision in x direction ...
			if tile.rect.colliderect(player_ptr.rect.x + dx, player_ptr.rect.y, player_ptr.rect.w, player_ptr.rect.h):
				dx = 0 # if we collide, stop player

			# check collision in y direction of expected dy (change in y)
			if tile.rect.colliderect(player_ptr.rect.x, player_ptr.rect.y + dy, player_ptr.rect.w, player_ptr.rect.h):
				# check if jumping
				if player_ptr.vel_y < 0:
					player_ptr.vel_y = 0
					dy = tile.rect.bottom - player_ptr.rect.top # dist between top of player and bottom of block

				# check if falling
				elif player_ptr.vel_y >= 0:
					player_ptr.vel_y = 0
					player_ptr.in_air = False
					dy = tile.rect.top - player_ptr.rect.bottom

		# check for collision with platforms
		for platform in gg.plats[0]:
			# check for x collision using expected position (dx) value
			if platform.rect.colliderect(player_ptr.rect.x + dx, player_ptr.rect.y, player_ptr.rect.w, player_ptr.rect.h):
				dx = 0
			# check for y collision
			if platform.rect.colliderect(player_ptr.rect.x, player_ptr.rect.y + dy, player_ptr.rect.w, player_ptr.rect.h):
				# check if below platform
				if abs((player_ptr.rect.top + dy) - platform.rect.bottom) < collision_thresh:
					player_ptr.vel_y = 0
					dy = platform.rect.bottom - player_ptr.rect.top
				# check if above platform
				elif abs((player_ptr.rect.bottom + dy) - platform.rect.top) < collision_thresh:
					player_ptr.rect.bottom = platform.rect.top - 1
					player_ptr.in_air = False
					dy = 0
				# move sideways with the platform
				if platform.move_x != 0:
					player_ptr.rect.x += platform.move_direction

		# check for collision with checkpoint
		if pygame.sprite.spritecollide(player_ptr, gg.check_points[0], False):
			print("Collided with a checkpoint!")
			if gg.current_level + 1 > gg.max_levels:
				gg.game_finished = True
				gg.game_over = 0
			else:
				gg.game_over = 1

		# check for collision with lava
		if pygame.sprite.spritecollide(player_ptr, gg.lava_tiles[0], False):
			player_ptr.death_animation()
			player_ptr.rect.y = player_ptr.rect.y
			player_ptr.rect.x = player_ptr.rect.x

		values.append(dx)
		values.append(dy)
		return values