import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import pygame
import Config
from Checkpoint import CheckPoint
from Platform import Platform
from Lava import Lava
import Levels
import GameGlobals as gg


class Level:
    def __init__(self):
        pass

    