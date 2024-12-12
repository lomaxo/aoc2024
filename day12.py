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
        return sum([c.walls for c in self.cells])

class Cell:
    def __init__(self, letter):
        self.region = None
        self.walls = 4 #set([0,1,2,3]) # Clockwise from N.
        self.letter = letter
        self.region = Region([self])

    def __repr__(self):
        # return f"{self.letter}-{self.region.region_id:<3}:{len(self.region):<2}:{self.walls}"
        return f"{self.letter}:{len(self.region):<3}:{self.walls}"

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
        for direction in [(0, -1),(1, 0),(0, 1), (-1, 0)]:
            this_cell = cell_map[y][x]
            dx, dy = direction
            if (0 <= y+dy < len(cell_map)) and (0 <= x+dx < len(cell_map[0])) :
                neighbour = cell_map[y+dy][x+dx]
            else:
                neighbour = None
            if neighbour and neighbour.letter == this_cell.letter:
                this_cell.region.merge_regions(neighbour.region)
                this_cell.walls -= 1
            if x == 0 and y == 0:
                print("Testion direction", direction, this_cell.walls)

region_set = set()
for row in cell_map:
    for cell in row:
        region_set.add(cell.region)

disp_map(cell_map)

# print(len(region_set))

price = 0
for r in region_set:
    price += r.get_perimeter() * len(r)
    print (r.letter, len(r), r.get_perimeter())


print(f"Total price = {price}")
