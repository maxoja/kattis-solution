t = int(input())

for _ in range(t):
    bx,by = tuple(map(float, input().split()))
    ncandle = int(input())
    possible = False
    
    for __ in range(ncandle):
        cx,cy = tuple(map(float, input().split()))
        if abs(cx-bx) <= 8 and abs(cy-by) <= 8:
            possible = True
            
    if possible:
        print('light a candle')
    else:
        print('curse the darkness')
