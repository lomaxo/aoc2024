data = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

with open("input/day12.txt") as file:
    data = file.read().strip()
#
# data = '''AAAA
# BBCD
# BBCC
# EEEC'''
#
class Region:
    next_region_id = 0
    def __init__(self, cells):
        self.region_id = Region.next_region_id
        Region.next_region_id += 1
        self.cells = set(cells)
        self.letter = cells[0].letter

    def add_cell(cell):
        assert cell.region == None
        self.cells.add(cell)
        cell.region = self

    def merge_regions(self, other):
        for cell in other.cells:
            self.cells.add(cell)
            cell.region = self
    
    def __len__(self):
        return len(self.cells)

    def get_perimeter(self):
        return sum([c.wall_count for c in self.cells])

    def get_corners(self):
        return sum([c.corners for c in self.cells])

class Cell:
    def __init__(self, letter):
        self.region = None
        self.wall_count = 4 #
        self.walls = set([0,1,2,3]) # Clockwise from N.
        self.letter = letter
        self.region = Region([self])
        self.corners = None

    def __repr__(self):
        # return f"{self.letter}-{self.region.region_id:<3}:{len(self.region):<2}:{self.wall_count}"
        return f"{self.letter}:{len(self.region):<3}:{self.corners}"

    
def update_corners(cell_map):
    corner_set = [set([0,1]),set([1,2]),set([2,3]),set([3,0])]
    adjacents_to_check = [(-1, 1),(-1,-1), (1, -1), (1, 1)]
    no_walls = [set([2,3]),set([3,0]),set([0,1]),set([1,2])]
    for y in range(len(cell_map)):
        for x in range(len(cell_map[0])):
            this_cell = cell_map[y][x]
            corners = 0
            # inside corners
            for c in corner_set:
                if this_cell.walls.issuperset(c):
                    corners += 1

            for dir, c, no_wall in zip(adjacents_to_check, corner_set, no_walls):
                dx, dy = dir
                if (0 <= y+dy < len(cell_map)) and (0 <= x+dx < len(cell_map[0])) :
                    if cell_map[y+dy][x+dx].walls.issuperset(c) and this_cell.walls.intersection(no_wall) == set():
                        corners += 1
            this_cell.corners = corners

def disp_map(cell_map):
    for row in cell_map:
        for cell in row:
            print(f" {cell} ", end="")
        print()
    print()


rows = data.split('\n')
cell_map = [[Cell(c) for c in row] for row in rows]

disp_map(cell_map)

for y in range(len(cell_map)):
    for x in range(len(cell_map[0])):
        # add neighbours to my region
        for wall_num, direction in enumerate([(0, -1),(1, 0),(0, 1), (-1, 0)]):
            this_cell = cell_map[y][x]
            dx, dy = direction
            if (0 <= y+dy < len(cell_map)) and (0 <= x+dx < len(cell_map[0])) :
                neighbour = cell_map[y+dy][x+dx]
            else:
                neighbour = None
            if neighbour and neighbour.letter == this_cell.letter:
                this_cell.region.merge_regions(neighbour.region)
                this_cell.wall_count -= 1
                this_cell.walls.remove(wall_num)
            if x == 0 and y == 0:
                print("Testion direction", direction, this_cell.wall_count)

region_set = set()
for row in cell_map:
    for cell in row:
        region_set.add(cell.region)

update_corners(cell_map)

disp_map(cell_map)

# print(len(region_set))

#Part 1

price = 0
for r in region_set:
    price += r.get_perimeter() * len(r)
    print (r.letter, len(r), r.get_perimeter())


print(f"Part 1: Total price = {price}")

# Part 2

price = 0
for r in region_set:
    price += r.get_corners() * len(r)
    print (r.letter, len(r), r.get_corners())


print(f"Part 2: Total price = {price}")
