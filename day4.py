data = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

# with open("input/day4.txt") as file:
    #  data = file.read()

grid = data.split('\n')
# grid = grid[:-1]

def search_xmas(grid: list[list], x, y, xdir, ydir):
    word = ''
    while len(word) < 4 and x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
            # print(grid[y][x])
            word += grid[y][x]
            x += xdir
            y += ydir
    return  word == "XMAS"

print(grid)
found = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'X':
            # print(grid[y][x])
            found += search_xmas(grid, x, y, 1, 0)
            found += search_xmas(grid, x, y, -1, 0)
            found += search_xmas(grid, x, y, 0, 1)
            found += search_xmas(grid, x, y, 0, -1)
            found += search_xmas(grid, x, y, 1, 1)
            found += search_xmas(grid, x, y, -1, -1)
            found += search_xmas(grid, x, y, 1, -1)
            found += search_xmas(grid, x, y, -1, 1)
print(f"Found XMAS {found} times")

def search_mas(grid: list[list], x, y, xdir, ydir):
    word = ''
    x = x - xdir
    y = y - ydir

    while len(word) < 3 and x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
            # print(grid[y][x])
            word += grid[y][x]
            x += xdir
            y += ydir
    return  1 if word == "MAS" else 0 

def search_x(grid: list[list], x, y, xdir, ydir):
    found = 0
    found += search_mas(grid, x, y, xdir, ydir):
    found += search_mas(grid, x, y, ydir, -xdir)
    found += search_mas(grid, x, y, -ydir, xdir)

    if found == 2:
         return 1
    return 0

found = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'A':
            # print(grid[y][x]
                      
            found += search_x(grid, x, y, 1, 0)
            found += search_x(grid, x, y, 1, 1)
            found += search_x(grid, x, y, -1, 0)
            found += search_x(grid, x, y, -1, -1)

            # found += search_x(grid, x, y, -1, 0)
            # found += search_x(grid, x, y, 0, 1)
            # found += search_x(grid, x, y, 0, -1)
            # found += search_x(grid, x, y, -1, -1)
            # found += search_x(grid, x, y, 1, -1)
            # found += search_x(grid, x, y, -1, 1)
print(f"Found X-MAS {found} times")