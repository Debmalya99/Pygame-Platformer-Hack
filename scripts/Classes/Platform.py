import pygame
import Config
import random

class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, move_x, move_y, screen,tile_size=50):
		self.screen = screen
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load(Config.Sprites["ground_2"])
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.move_direction = 1
		self.move_counter = random.randint(0, 40)

		self.move_x = move_x # flag to move in x direction
		self.move_y = move_y # flag to move in y direction

	# handle platform movement
	def update(self):
		self.rect.x += self.move_direction * self.move_x
		self.rect.y += self.move_direction * self.move_y
		self.move_counter += 1

		if abs(self.move_counter) > 50:
			self.move_direction *= -1
			self.move_counter *= -1