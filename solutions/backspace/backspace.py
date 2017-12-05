#https://open.kattis.com/problems/backspace

def process_result(input_line) :
    result = []
    
    for character in input_line :
        result.pop() if character == '<' else result.append(character)

    return ''.join(result)

if __name__ == '__main__' :
    input_line = input()
    result = process_result(input_line)

    if result != '' :
        print(result)
