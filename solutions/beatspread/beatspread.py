n = int(input())

for _ in range(n):
    s, d = tuple(map(int, input().split()))

    if d > s or (s+d)%2 == 1:
        print('impossible')
        continue
    
    b = (s+d)//2
    a = b - d
    
    print(b, a)

