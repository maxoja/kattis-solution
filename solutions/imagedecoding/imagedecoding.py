first_image = True

while True :
    num_line = int(input())

    if num_line == 0 :
        break

    if not first_image :
        print()
        
    first_image = False

    size = 0
    initialized_size = False
    error = False
    
    for _ in range(num_line):
        input_values = input().split()
        char_type = input_values[0]
        line_data = list(map(int,input_values[1:]))
        count = 0
        for data in line_data :
            print(char_type*data, end='')
            char_type = '.' if char_type == '#' else '#'
            count += data
        print()
        if initialized_size :
            if size != count :
                error = True
        else :
            initialized_size = True
            size = count

    if error :
        print('Error decoding image')
    
