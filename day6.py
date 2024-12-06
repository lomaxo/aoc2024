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

# Find "^"
start_x = 0
start_y = 0
for y in range(y_size):
    for x in range(x_size):
        if mapdata[y][x] == '^':
            start_x, start_y = x, y
            
print(start_x, start_y)
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
    print(row)
    count += row.count('X')

print(f"Total spaces = {count}")
