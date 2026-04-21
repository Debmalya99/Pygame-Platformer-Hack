import pygame

class GlobalResourceStore:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}

    def load_image(self,image_id,image_filepath):
        self.images[image_id] = pygame.image.load(image_filepath)
        print(f"{self.__class__.__name__}::load_image::{image_filepath} loaded successfully")


    def get_image(self,image_id):
        if image_id not in self.images.keys():
            print(f"{self.__class__.__name__}::get_image::Image with id:{image_id} not found")
            return None
        return self.images.get(image_id,None)