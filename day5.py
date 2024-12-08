from itertools import permutations
from functools import cmp_to_key

data = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

with open("input/day5.txt") as file:
    data = file.read()[:-1]


rules, books = data.split('\n\n')

rule_dict = {}
for rule in rules.split('\n'):
    before, after, *other = rule.split('|')
    if int(before) in rule_dict:
        rule_dict[int(before)].append(int(after))
    else:
        rule_dict[int(before)] = [int(after)]

# print(rule_dict)

def book_is_valid(book: list[int]) -> bool:
    book_set = set()
    for page in book:
        rule_list = rule_dict.get(int(page), [])
        for rule in rule_list:
            if rule in book_set:
                return(False)
        book_set.add(int(page))
    return True

def get_middle_page(book: list[int]) -> bool:
    return book[len(book)//2]


valid_books = []
invalid_books = []
for book in books.split('\n'):
    book = [int(page) for page in book.split(',')]
    # print(book, book_is_valid(book))
    if book_is_valid(book):
        valid_books.append(book)
    else:
        invalid_books.append(book)

total = sum([get_middle_page(book) for book in valid_books])

# def get_valid_book_perm(book: list[int]) -> list[int]:
#     for perm in permutations(book):
#         if book_is_valid(perm):
#             return perm
#     print("No valid book found")
#     return []

def comp_pages(page1: int, page2: int):
    rule_list1 = rule_dict.get(page1, [])
    rule_list2 = rule_dict.get(page2, [])
    if page2 in rule_list1:
        return -1
    elif page1 in rule_list2:
        return 1
    else:
        return 0
    


for book in invalid_books:
    # print(get_valid_book_perm(book))
    book.sort(key=cmp_to_key(comp_pages))
    # print(book)

part_two = sum([get_middle_page(book) for book in invalid_books])

print(f"Sum of middle pages of correct books = {total}")
print(f"Sum of corrected middle pages = {part_two}")


