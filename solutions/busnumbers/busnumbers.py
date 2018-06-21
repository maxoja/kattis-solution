n = int(input())
seq = sorted(list(map(int, input().split())))

prevs = []


for i in range(len(seq)):
    current = seq[i]
    nxt = -1 if i == len(seq)-1 else seq[i+1]

    if nxt == current+1:
        prevs.append(current)
        continue

    else:
        if prevs:
##            print('enter' , prevs)
            if len(prevs) >= 2:
                print(str(prevs[0]) + '-' + str(current), end=' ')
            else:
                print(prevs[0], current, end=' ')
                
            prevs = []
            
        else:
            print(current, end=' ')
