level_tiles = '''
.GGGGGGGG.................
....GGGGG.......GGGG......
..........................
..GGGG....................
...........SSSSSSS........
...........GGGGGGG........
'''

level_array = level_tiles.strip().splitlines()

TILES = []

X = 0
Y = 0
TILE_SIZE = 18

for line in level_array:
    for char_ in line:
        # print(char_,X,Y)
        if char_ == '.':
            X += TILE_SIZE
        
        elif char_ == 'S':
            TILES.append({'name':'snow','loc':(X,Y)})
            X += TILE_SIZE

        elif char_ == 'G':
            TILES.append({'name':'grass','loc':(X,Y)})
            X += TILE_SIZE

    Y += TILE_SIZE
    X = 0



