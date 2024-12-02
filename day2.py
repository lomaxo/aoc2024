data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

lines = data.split("\n")

with open("input/day2.txt") as file:
    lines = file.readlines()

def get_sign(pair):
    if pair[0] == pair[1]:
        return 0
    return (pair[1]-pair[0])/abs(pair[1]-pair[0])

def get_diff(pair):
    return abs(pair[1]-pair[0])

def check_is_safe(levels: list):
    # print(levels)
    pairs = [(levels[i], levels[i+1]) for i in range(len(levels)-1)]
    # print(pairs)
    safe = True
    direction = get_sign(pairs[0])
    for pair in pairs:
        if get_sign(pair) != direction:
            safe = False
            continue
        if get_diff(pair) > 3 or get_diff(pair) == 0:
            safe = False
            continue
    return safe

def drop_one_level(line:list) -> list[list]:
    return [line[:i] + line[i+1:] for i in range(len(line))]


total_safe = 0
for line in lines:
    levels = [int(n) for n in line.split()]
    # print(levels)
    if check_is_safe(levels):
        total_safe += 1
    else:
        # print("checking alternatives")
        for alt in drop_one_level(levels):
            # print(alt)
            if check_is_safe(alt):
                total_safe +=1
                break

print(f"Safe reports = {total_safe}")

