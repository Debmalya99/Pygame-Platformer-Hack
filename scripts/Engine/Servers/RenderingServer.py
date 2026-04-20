import pygame

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
            z_index
    ):
        self.rendering_buffer.append((
            drawable,   # The actual image or something that you wish to draw
            location_vec2, # Its location. Might as well take a rect
            z_index
        ))

    def flush(self):
        ## First sort the items

        if len(self.rendering_buffer) > 0:
            self.rendering_buffer = sorted(self.rendering_buffer,key= lambda x: x[2]) # Sort by the z_index

        for item in self.rendering_buffer:
            _drawable = item[0]
            _location = item[1]
            # z_index = item[0]

            self.screen.blit(_drawable,_location)

        ## And clear the rendering buffer
        self.rendering_buffer.clear()