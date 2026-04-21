import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class BaseLevel:
    def __init__(self):
        pass

    def init_level(self):
        pass

    def update(self,dt):
        pass