num_case = 1

while True :
    try :
        data = list(map(int,input().split()))[1:]
        
        min_val = min(data)
        max_val = max(data)
        range_of_val = max_val - min_val

        print('Case %d: %d %d %d' % (num_case, min_val, max_val, range_of_val))
        
        num_case += 1
    except EOFError :
        break
