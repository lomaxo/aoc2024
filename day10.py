from copy import deepcopy
data = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

with open("input/day10.txt") as file:
    data = file.read().strip()


rows = data.split('\n')
map_data = [[int(n) for n in row] for row in rows]

# print(map_data)

X_SIZE = len(map_data[0])
Y_SIZE = len(map_data)

def get_routes_pt1(map_data, x, y) -> set[tuple[int, int]]:
    # print(x,y, map_data[y][x])
    peaks = set()
    if map_data[y][x] == 9:
        peaks = set()
        peaks.add((x,y))
        return peaks
    else:
        current_value = map_data[y][x]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for dx, dy in dirs:
            if (0 <= y+dy < Y_SIZE) and (0 <= x+dx < X_SIZE):
                if map_data[y+dy][x+dx] == current_value+1:
                     peaks = peaks.union(get_routes_pt1(map_data, x+dx, y+dy))
        return peaks

def get_routes(map_data, path, x, y) -> set[tuple[tuple[int, int]]]:
    # print(x,y, map_data[y][x])
    paths = set()
    path = deepcopy(path)
    path.append((x,y))
    # print(path)
    if map_data[y][x] == 9:
        paths.add(tuple(path))
        return paths
    else:
        current_value = map_data[y][x]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for dx, dy in dirs:
            if (0 <= y+dy < Y_SIZE) and (0 <= x+dx < X_SIZE):
                if map_data[y+dy][x+dx] == current_value+1:
                     paths = paths.union(get_routes(map_data, path, x+dx, y+dy))
        return paths


total = 0
for y in range(len(map_data)):
    for x in range(len(map_data[0])):
        if map_data[y][x] == 0:
            total += len(get_routes(map_data, [], x, y))
print(f"Total part 1: {total}")
#
# r = get_routes(map_data, [], 2, 0)
# for l in r:
#     print(l)
