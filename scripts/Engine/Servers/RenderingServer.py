import pygame
from enum import Enum

class DrawableType(Enum):
    DT_IMAGE = 0
    DT_TEXT = 1
    DT_DEBUG_RECT = 2 # If you wish to draw a rectangle for debug purposes
    DT_DEBUG_CIRCLE = 3 # If you wish to draw a rectangle for debug purposes

class RenderingServer:
    def __init__(
            self,
            screen_width,
            screen_height,
            screen, #a valid pygame screen

    ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen

        self.rendering_buffer = [] ## Add stuff to this rendering buffer that will be blit later on


    def add_drawable(
            self,
            drawable,
            location_vec2,
            z_index,
            drawable_type = DrawableType.DT_IMAGE
    ):
        self.rendering_buffer.append((
            drawable,   # The actual image or something that you wish to draw
            location_vec2, # Its location. Might as well take a rect
            z_index,
            drawable_type
        ))

    def flush(self):
        ## First sort the items

        if len(self.rendering_buffer) > 0:
            self.rendering_buffer = sorted(self.rendering_buffer,key= lambda x: x[2]) # Sort by the z_index

        for item in self.rendering_buffer:
            _drawable = item[0]
            _location = item[1]
            _drawable_type = item[3]
            if _drawable_type == DrawableType.DT_IMAGE:
                self.screen.blit(_drawable,_location)

        ## And clear the rendering buffer
        self.rendering_buffer.clear()

    def clear_screen(self,color):
        self.screen.fill(color)