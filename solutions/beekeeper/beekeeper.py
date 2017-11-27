vowels = ['a','e','i','o','u','y']

while True :
    n = int(input())

    if n == 0 :
        break

    best_word = ''
    best_pair = -1
    
    for _ in range(n) :
        word = input()
        count = 0

        for i in range(len(word)-1) :
            if word[i] == word[i+1] and word[i] in vowels :
                count += 1
                
        if count > best_pair:
            best_word = word
            best_pair = count

    print(best_word)
