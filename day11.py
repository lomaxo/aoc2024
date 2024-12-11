from functools import cache


data = '''0 1 10 99 999'''
data = "125 17"

with open("input/day11.txt") as file:
    data = file.read().strip()

stones = [int(n) for n in data.split()]


# Part 1

print(stones)
N = 25
for i in range(N):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone))%2 == 0:
            stone_str = str(stone)
            mid = len(stone_str)//2
            new_stones.append(int(stone_str[:mid]))
            new_stones.append(int(stone_str[mid:]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
    print(f"{i}: number of stones = {len(stones)}...")

print(f"Number of stones after {N} iterations = {len(stones)}")

# Part 2

@cache
def count_stones(stone, depth):
    if depth == 0:
        return 1

    if stone == 0:
        return count_stones(1, depth-1)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        mid = len(stone_str)//2
        return count_stones(int(stone_str[:mid]), depth-1) + count_stones(int(stone_str[mid:]), depth-1)
    else:
        return count_stones(stone * 2024, depth-1)

    # return count

depth = 75
# stones = [125,17]
stones = [int(n) for n in data.split()]
count = sum([count_stones(stone, depth) for stone in stones])

print(f"Number of stones after {N} iterations = {count}")

