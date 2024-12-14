# AOC2024
- Day 1: Mainly just a case of reading the input into two lists. Using zip was handy.
- Day 2: A bit fiddly to do part 2. Some helper functions helped. Quite inefficient to generate all possible _reports_ before checking but it works
- Day 3: Had to use regex...
- Day 4: Spent far too long trying to solve it for +-MAS as well as X-MAS, and wondering why it didn't give the right number...
- Day 5: Tried brute forcing part 2 but that was too slow. Ended up sorting using a custom comparison function.
- Day 6: Part one pretty straightforward. Part two: ended up brute forcing it and it was quite slow. There's probably a neater way but this works...
- Day 7: Pretty straightforward. Had to reverse the operands to make my recursive solution apply from left to right. part 2 was a trivial addition. It's a bit slow though. Could maybe be optimized.
- Day 8: Part 1 was fine. Part 2 should have been relatively easy but took a bit of thinking about.
- Day 9: Part 1 was no problem. Ran out of time for part 2. Seems easy in principle but fiddly to get right.
- Day 10: Part 1 was a nice recursive function. Part 2, also fine once I'd worked out that lists aren't hashable, but tuples are, and that I needed to copy the list.
- Day 11: Took a while for find a way of optimizing for part 2. Tried creating a linked list to make insertions faster but that didn't work. Tried to implement my own memoisation but also didn't work for some reason so used functools @cache decorator.
Update: Just added my on memoisation and it worked fine. Not sure what I'd done wrong before.
- Day 12: Part 1 was a nice problem; I'm happy with the algorithm. Part 2 will require some more thinking...Update: Not as hard as I thought. Needed to count corners.

