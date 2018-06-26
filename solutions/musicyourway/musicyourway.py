attr = input().split()
n = int(input())
songs = [ { a:v for a,v in zip(attr,input().split()) } for i in range(n) ]

n = int(input())
for _ in range(n):
    a = input()
    result = sorted(songs, key=lambda song:song[a])
    print(' '.join(attr))
    for r in result:
        for k in attr:
            print(r[k], end=' ')
        print()
    print()
    songs = result
