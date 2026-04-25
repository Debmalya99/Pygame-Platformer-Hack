level_tiles = '''
.GGGGGGGG........DDD......
....GGGGG.......GGGG......
................DDDD......
..GGGG....................
...........SSSSSSS........
SSSSSSSSSSSGGGGGGG........
'''

level_array = level_tiles.strip().splitlines()

TILES = []

X = 0
Y = 0
TILE_SIZE = 18

for line in level_array:
    for char_ in line:
        
        if char_ == 'S':
            TILES.append({'name':'snow','loc':(X,Y)})
        elif char_ == 'G':
            TILES.append({'name':'grass','loc':(X,Y)})
        elif char_ == 'D':
            TILES.append({'name':'dirt','loc':(X,Y)})
            
        X += TILE_SIZE
    Y += TILE_SIZE
    X = 0



