t = int(input())

for _ in range(t) :
    input()
    nc,ne = tuple(map(int,input().split()))
    ncs = list(map(int,input().split()))
    nes = list(map(int,input().split()))
    nc_average = sum(ncs)/len(ncs)
    ne_average = sum(nes)/len(nes)

    count = 0
    
    for s in ncs :
        if s < nc_average and s > ne_average :
            count += 1

    print(count)
    
