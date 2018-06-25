i = 1
line = input()
while line != 'END':
    space = line.split('*')[1:-1]
    dist = [ len(s) for s in space ]
    even = True
    for d in dist[1:]:
        if d == dist[0]:
            continue
        else:
            print(i, 'NOT EVEN')
            even = False
            break

    if even:
        print(i, 'EVEN')
    
    line = input()
    i += 1
