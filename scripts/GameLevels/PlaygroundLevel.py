import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# from Engine.BaseLevel import BaseLevel ## DELETE
# import GameGlobals as gg
import Levels

symbols_table = {
    ".": 0,     # BLANK SPACE (Empty Air)
    "1": 1,     # GROUND_1 (Standard Solid)
    "2": 2,     # GROUND_2 (Standard Solid)
    "↔": 2.1,   # MOVING PLATFORM (Horizontal)
    "↕": 2.2,   # MOVING PLATFORM (Vertical)
    "3": 3,     # GROUND_3
    "4": 4,     # GROUND_4
    "5": 5,     # GROUND_5
    "6": 6,     # GROUND_6
    "7": 7,     # GROUND_7
    "8": 8,     # GROUND_8
    "9": 9,     # GROUND_9
    "A": 10,    # GROUND_10
    "B": 11,    # GROUND_11
    "w": 12,    # GRASS_1 (Offset Foliage)
    "x": 13,    # GRASS_2 (Offset Foliage)
    "y": 14,    # GRASS_3 (Offset Foliage)
    "z": 15,    # GRASS_4 (Offset Foliage)
    "v": 16,    # GRASS_5 (Offset Foliage)
    "&": 17,    # BUSH_1 (Decorative)
    "%": 18,    # BUSH_2 (Decorative)
    "T": 19,    # TREE_1 (Living Decor)
    "†": 20,    # TREE_2 (Dead Decor)
    "o": 21,    # ROCK_1 (Small)
    "O": 22,    # ROCK_2 (Large)
    "¶": 23,    # CHECKPOINT (Spawn/Save Point)
    "*": 24     # LAVA (Hazard/Death)
}

inv_symbols_table = {v:k for k,v in symbols_table.items()}

for index,_level in enumerate(Levels.level,1):
    str_level = ""
    print(f"Processing Level: {index}")
    for _line in _level:
        str_line = "".join(inv_symbols_table[key] for key in _line)
        str_level += str_line + '\n'

    # print(str_level)
    # print("-"*50)


# --------------------------------------------------------------------------------------------------------------------------------------------
levels = [
    '''
....................
....................
....................
....w...............
..w.2...............
..2......ywx........
.......↕.123........
↕........4B8x..ywwww
wx..yx...4B97..12222
67..22...4B6...4BBBB
.....↔..y48....4BBBB
........5A8w.↕.4BBBB
.........493...5BBBB
......↕..4B8....5666
wwwwwwx..4B8.......¶
2222223..4B8.....yww
BBBBBB8..4B8wx..↕5BB
BBBBBB8..4B922....5B
''',    ## This was Level 1
'''
666BBB6666666666666B
...4B8¶.............
wx.5B8ww..w..y..yx..
23..5666..6..6..13..
B8x...ywwx......48..
B93ww.1223.ywxww48..
BB923.4BB8.12222A8.↕
BBBB8.4BB8...4BBB8x.
BBBB8.4BB8.yw4BBB92.
BBBB8.4BB8.42ABBB8..
BBBB7.4B67.4BBBBB8..
BBB7.y47...566BBB8.↕
BB8.y27.......5BB8w.
BB8.27..wx..yx.5667.
BB8.7...13..52w.....
BB8..........52w...↕
BB8........↕..52wwww
BB8............52222
''', ## This was level 2
'''
66666666666666666666
....................
....................
wx.w..w..w..w..yx...
22.2..2..2..2..23...
BB*B**B**B**B**B8...
BB666666666666667...
B8.................↕
B8..................
B8.w..w..w..w..yx...
B8.2..2..2..2..13...
B8.B..B..B..B..48...
B8.B**B**B**B**BB***
B8.66666666666666666
B8.................¶
B8.w..w..w..w.....ww
B8.2..2..2..2..↕..52
BB*B**B**B**B**.**.5
''', ## This was Level 3
'''
B666666666666666666B
8..................4
8..................4
8..................4
8..................4
8..................4
8..................4
8..................4
8..................4
8..................4
8..................4
8..................4
8..................4
8wwwwwwwwwwwwwwwwww4
9222222222222222222A
BBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBB
''', ## This was Level 4
]

def str_level_to_num_array(str_level:str):
    out_array = []
    level_array = str_level.strip().splitlines()
    for line in level_array:
        line_arr = []
        for char_ in line:
            line_arr.append(symbols_table[char_])

        out_array.append(line_arr)
    
    return out_array

for index,level_ in enumerate(levels,1):
    out = str_level_to_num_array(level_)
    print(f"Level: {index}")
    print(out)
    print("-"*50)
    