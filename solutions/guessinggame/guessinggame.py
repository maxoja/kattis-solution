minimum = 1
maximum = 10
dishonest = False

def reset_game() :
    global minimum
    global maximum
    global dishonest
    minimum = 1
    maximum = 10
    dishonest = False
    

while True :
    guessing_number = int(input())

    if guessing_number == 0 :
        break

    response = input()

    if response == 'right on' :
        if guessing_number < minimum or guessing_number > maximum :
            dishonest = True
            
        if dishonest :
            print('Stan is dishonest')
        else :
            print('Stan may be honest')
            
        reset_game()
        continue

    if dishonest :
        continue
    
    if response == 'too high' :
        if guessing_number <= minimum :
            dishonest = True

        if guessing_number <= maximum :
            maximum = guessing_number - 1
    elif response == 'too low' :
        if guessing_number >= maximum :
            dishonest = True

        if guessing_number >= minimum :
            minimum = guessing_number + 1
            

    
    
