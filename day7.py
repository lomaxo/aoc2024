data = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

with open("input/day7.txt") as file:
    data = file.read()[:-1]

lines = data.split('\n')

def get_poss_results(operands: list[int]) -> list[int]:
    if len(operands) == 1:
        return [operands[0]]
    else:
        head = operands[0]
        tail = operands[1:]
        add = [head + t for t in get_poss_results(tail)]
        mul = [head * t for t in get_poss_results(tail)]
        concat = [int(str(t) + str(head)) for t in get_poss_results(tail)]
        return add + mul + concat

total = 0
for line in lines:
    res, operands = line.split(": ")
    res = int(res)
    operands = [int(op) for op in operands.split(' ')]
    if res in get_poss_results(list(reversed(operands))):
        total += res

print(f"Total = {total}")
