line = input()
counting = dict()
while line != '***':
    if line not in counting:
        counting[line] = 1
    else:
        counting[line] += 1

    line = input()

winner = ''
best = 0
bestcount = 0

for can, score in counting.items():
    if score == best:
        bestcount += 1
        continue
    if score < best:
        continue
    if score > best:
        winner = can
        best = score
        bestcount = 1
        continue

if bestcount > 1:
    print('Runoff!')
else:
    print(winner)
