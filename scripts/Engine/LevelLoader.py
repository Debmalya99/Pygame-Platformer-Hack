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

def str_level_to_num_array(str_level:str):
    out_array = []
    level_array = str_level.strip().splitlines()
    for line in level_array:
        line_arr = []
        for char_ in line:
            line_arr.append(symbols_table[char_])

        out_array.append(line_arr)
    
    return out_array