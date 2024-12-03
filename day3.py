import re

data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

with open("input/day3.txt") as file:
    data = file.read()

reg = "mul\(\d+,\d+\)"


# Part 1
# total = 0
# for catch in re.findall(reg, data):
#     print(catch)
#     x, y= re.findall("\d+", catch)
#     print(x, y)
#     x ,y = int(x), int(y)
#     total += x*y
#
# print(total)
#
# Part 2

regpt2 = "mul\(\d+,\d+\)|do\(\)|don't\(\)"

total = 0
do_mul = True
for catch in re.findall(regpt2, data):
    print(catch)
    if catch == "do()":
        do_mul = True
    elif catch == "don't()":
        do_mul = False
    else:
        if do_mul:
            x, y= re.findall("\d+", catch)
            print(x, y)
            x ,y = int(x), int(y)
            total += x*y
        else:
            do_mul = False

print(total)
