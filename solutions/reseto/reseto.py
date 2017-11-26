n,k = tuple(map(int,input().split()))
numbers = list(range(2,n+1))

minimum = 2
count = 0
finished = False

while not finished :
    set_new_minimum = False
    new_minimum = -1

    i = minimum-2
    while i < len(numbers) :
        if numbers[i] < 0 :
            i += numbers[i]*-1
            continue

        if numbers[i] % minimum == 0 :
            count += 1
            if count == k :
                print(numbers[i])
                finished = True
                break
            if i < len(numbers)-1 and numbers[i+1] < 0:
                numbers[i] = numbers[i+1]-1
            else :
                numbers[i] = -1
        else :
            if not set_new_minimum :
                set_new_minimum = True
                new_minimum = numbers[i]
        
        i += 1

    minimum = new_minimum
