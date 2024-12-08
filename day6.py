from copy import deepcopy

data = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

with open("input/day6.txt") as file:
    data = file.read()
    data = data[:-1]

mapdata = data.split('\n')
y_size = len(mapdata)
x_size = len(mapdata[0])

mapdata = [list(row) for row in mapdata]
# print(mapdata)
x_dir = 0
y_dir = -1

def rotate(x, y):
    return -y, x

def get_dir_marker(x, y):
    if x > 0:
        return '>'
    elif x < 0:
        return '<'
    elif y < 0:
        return '^'
    else:
        return 'v'


# Find "^"
start_x = 0
start_y = 0
for y in range(y_size):
    for x in range(x_size):
        if mapdata[y][x] == '^':
            start_x, start_y = x, y
            
print(start_x, start_y)

# Part 1
x, y = start_x, start_y
while x >= 0 and x < x_size and y >=0 and y < y_size:
    if mapdata[y][x] == '#':
        x -= x_dir
        y -= y_dir
        x_dir, y_dir = rotate(x_dir, y_dir)
    else:
        mapdata[y][x] = 'X'
    x += x_dir
    y += y_dir

count = 0
for row in mapdata:
    # print(row)
    count += row.count('X')

print(f"Total spaces = {count}")

# Part 2
def is_loop(mapdata, x, y):
    x_dir, y_dir = 0, -1
    been_here = set()
    while x >= 0 and x < x_size and y >=0 and y < y_size:
        if mapdata[y][x] == '#':
            x -= x_dir
            y -= y_dir
            x_dir, y_dir = rotate(x_dir, y_dir)
        else:
            if (x, y, x_dir, y_dir) in been_here:
                return True
            mapdata[y][x] = get_dir_marker(x_dir, y_dir)
            been_here.add((x, y, x_dir, y_dir))
        x += x_dir
        y += y_dir

    return False

total = 0
for y in range(len(mapdata)):
    for x in range(len(mapdata[0])):
        map_copy = deepcopy(mapdata)
        map_copy[y][x] = '#'
        # print(f"testing x={x}, y={y}")
        if is_loop(map_copy, start_x, start_y):
            total += 1

print(total)
