while True :
    a,b,c,d = tuple(map(int,input().split()))

    if a+b+c+d == 0 :
        break
    
    if b > a :
        a,b = b,a
    if d > c :
        c,d = d,c

    p1 = a*10 + b
    p2 = c*10 + d
    
    if a == 2 and b == 1 :
        p1 += 1000
    if c == 2 and d == 1 :
        p2 += 1000

    if a == b :
        p1 += 100*a
    if c == d :
        p2 += 100*c

    if p1 >= 1000 and p2 >= 1000 or p1 == p2:
        print('Tie.')
    elif p1 > p2 :
        print('Player 1 wins.')
    else :
        print('Player 2 wins.')
