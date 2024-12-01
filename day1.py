data = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open("input/day1.txt") as file:
    lines = file.readlines()


# lines = data.split("\n")
# print(lines)

list1 = []
list2 = []
for line in lines:
    numbers = line.split()
    list1.append(int(numbers[0]))
    list2.append(int(numbers[1]))

slist1 = sorted(list1)
slist2 = sorted(list2)
# print(list1)
distance = 0
for pairs in zip(slist1, slist2):
    distance += abs(pairs[0]-pairs[1])

print(f"Total distance = {distance}")

similarity = 0
for pairs in zip(list1, list2):
    # print(pairs[0], list2.count(pairs[0]),pairs[0] * list2.count(pairs[0]))
    similarity += pairs[0] * list2.count(pairs[0])

print(f"Total similarity = {similarity}")
