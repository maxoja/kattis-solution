import itertools

dwarves = []

for _ in range(9) :
    dwarves.append(int(input()))

combinations = itertools.combinations(dwarves,7)
for combination in combinations :
    if sum(combination) == 100 :
        for dwarve in combination :
            print(dwarve)
        break
