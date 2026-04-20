import pygame
import math

class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
    def __add__(self, other):
        return Vector2(self.x + other.x,self.y + other.y)
    
    def scale(self, scalar):
        return Vector2(scalar*self.x,scalar*self.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x,self.y - other.y)
    
    def as_list(self):
        return [self.x,self.y]
    
    def __abs__(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def norm(self):
        return self*(1/abs(self))
    
    def __str__(self):
        return f"Vector2::x: {self.x}, y: {self.y}"


def world_2_screen(v:Vector2,screen_width,screen_height):
    _x = v.x + screen_width//2
    _y = -v.y + screen_height//2
    return Vector2(_x,_y)

### For testing purposes

if __name__ == "__main__":
    v1 = Vector2(3,4)
    print(Vector2(1,1) - v1)
    print(v1.as_list())


