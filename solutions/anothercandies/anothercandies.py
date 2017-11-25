t = int(input())

for _ in range(t) :
    input()
    n = int(input())
    accumulator = 0
    
    for __ in range(n) :
        num_candies = int(input())
        accumulator += num_candies
        accumulator %= n

    print("YES") if accumulator == 0 else print("NO")
    
    
    
