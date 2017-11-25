def all_equal(sequence) :
    for i in range(1,len(sequence)) :
        if sequence[i-1] != sequence[i] :
            return False
    return True

def dif_sequence_of(sequence) :
    result = []
    for i in range(len(sequence)-1) :
        result.append(sequence[i+1] - sequence[i])
    return result

def find_next_value(sequences) :
    last_sequence = True
    for i in range(len(sequences))[::-1] :
        if last_sequence :
            sequences[i].append(sequences[i][-1])
            last_sequence = False
            continue

        sequences[i].append(sequences[i][-1] + sequences[i+1][-1])

    return sequences[0][-1]
    
input_line = input()
input_values = input_line.split()
sequences = [list(map(int,input_values[1:]))]

while not all_equal(sequences[-1]) :
    sequences.append(dif_sequence_of(sequences[-1]))


print(len(sequences)-1, find_next_value(sequences))
    
