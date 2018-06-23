n = int(input())

for _ in range(n):
    inputs = list(map(int, input().split()))
    size = inputs.pop(0)
    sorted_input = sorted(inputs)

##    print(inputs)
##    print(sorted_input)

    first_dif_original = inputs[1]-inputs[0]
    first_dif_sorted = sorted_input[1] - sorted_input[0]
    arith_original = True
    arith_sorted = True

    for i in range(size-1):
        if inputs[i+1] - inputs[i] != first_dif_original:
            arith_original = False
        if sorted_input[i+1] - sorted_input[i] != first_dif_sorted:
            arith_sorted = False
        if not arith_original and not arith_sorted:
            break

    if not arith_original and not arith_sorted:
        print("non-arithmetic")
    elif arith_original:
        print("arithmetic")
    else:
        print("permuted arithmetic")

        
        
    

    
