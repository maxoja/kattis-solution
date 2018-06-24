import sys
used = set()
for line in sys.stdin:
    for word in line.split():
        low = word.lower()
        if low in used:
            print('.', end=' ')
        else:
            used.add(low)
            print(word, end=' ')
    print()
