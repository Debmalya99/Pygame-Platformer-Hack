import pygame

class TileSet:
    def __init__(self,filename):
        self.filename = filename
        self.atlas = pygame.image.load(self.filename)
        self.tile_defs = {}

    def add_tile_definition(
            self,
            tile_name,
            tile_rect,
            collision=False
    ):
        self.tile_defs[tile_name] = {
            'rect':tile_rect,
            'collision':collision
        }

    
    def get_tile(
            self,
            tile_name
    ):
        return self.tile_defs.get(tile_name,None)
    
    def draw_tile(self,tile_name,location,screen):
        tile_ = self.get_tile(tile_name=tile_name)
        screen.blit(
            source=self.atlas,
            dest=location,
            area=tile_['rect']
        )
