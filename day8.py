from itertools import combinations
import math
data = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''
#
# data = '''T.........
# ...T......
# .T........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........'''
#
with open("input/day8.txt") as file:
    data = file.read()[:-1]

antenna_map = []

def disp_map(map):
    for row in map:
        print(''.join(row))

for line in data.split('\n'):
    antenna_map.append(list(line))

antenna_dict = {}

Y_SIZE = len(antenna_map)
X_SIZE = len(antenna_map[0])

for y in range(len(antenna_map)):
    for x in range(len(antenna_map[0])):
        if antenna_map[y][x] != '.':
            if antenna_map[y][x] in antenna_dict:
                antenna_dict[antenna_map[y][x]].append((x,y))
            else:
                antenna_dict[antenna_map[y][x]] = [(x,y)]

disp_map(antenna_map)

def is_in_range(coord):
    x, y = coord
    return x >= 0 and x < X_SIZE and y >= 0 and y < Y_SIZE

def get_antinode_pair(ant1: tuple[int,int], ant2: tuple[int,int]):
    ax1, ay1 = ant1[0], ant1[1]
    ax2, ay2 = ant2[0], ant2[1]
    nx1 = ax1 - (ax2 - ax1)
    ny1 = ay1 - (ay2 - ay1)
    nx2 = ax2 + (ax2 - ax1)
    ny2 = ay2 + (ay2 - ay1)
    return (nx1, ny1), (nx2, ny2)

def get_antinodes_from_pair(ant1, ant2):
    ax1, ay1 = ant1[0], ant1[1]
    ax2, ay2 = ant2[0], ant2[1]
    dx = (ax2 - ax1)
    dy = (ay2 - ay1)
    l = math.gcd(dx, dy)
    dx /= l
    dy /= l
    x = ax1
    y = ay1
    antinodes = set()
    while x < X_SIZE and x >=0:
        x += dx
        y += dy
        if is_in_range((x,y)):
            antinodes.add((x, y))
    x = ax1
    y = ay1
    while x >= 0 and x < X_SIZE:
        x -= dx
        y -=dy
        if is_in_range((x,y)):
            antinodes.add((x,y))
    antinodes.add((ax1, ay1))
    antinodes.add((ax2, ay2))
    return antinodes

antinode_map = [list('.' * len(antenna_map[0])) for _ in antenna_map]

#Part 1
antinodes = set()
for antenna in antenna_dict:
    # print(antenna_dict[antenna])
    pairs = combinations(antenna_dict[antenna], 2) 
    for pair in pairs:
        an1, an2 = get_antinode_pair(*pair)
        if is_in_range(an1):
            antinodes.add(an1)
        if is_in_range(an2):
            antinodes.add(an2)
print(f"Part 1: Total number of antinodes = {len(antinodes)}")

# Part 2

antinodes = set()
for antenna in antenna_dict:
    pairs = combinations(antenna_dict[antenna], 2) 
    for pair in pairs:
        an = get_antinodes_from_pair(*pair)
        for antinode in an:
            if is_in_range(antinode):
                antinodes.add(antinode)
for an in antinodes:
    x, y = an
    antinode_map[int(y)][int(x)] = '#'
print()
disp_map(antinode_map)
print(f"Part 2: Total antinodes = {len(antinodes)}")

