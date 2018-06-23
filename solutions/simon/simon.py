n = int(input())
for _ in range(n):
    line = input()
    if line[:10] == 'simon says':
        print(line[11:])
    else:
        print()
