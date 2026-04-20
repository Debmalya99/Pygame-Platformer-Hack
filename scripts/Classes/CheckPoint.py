import pygame
import Config

class CheckPoint(pygame.sprite.Sprite):
	def __init__(self, x, y, screen,tile_size = 50):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load(Config.Sprites["sign"])
		self.image = pygame.transform.scale(img, (int(tile_size // 1.3), int(tile_size // 1.3)) )
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y + 63 # adjust the height to go ontop of grass