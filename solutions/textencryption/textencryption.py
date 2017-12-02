#https://open.kattis.com/problems/textencryption

while True :
    n = int(input())

    if n == 0 :
         break

    message = input()
    message = message.replace(' ','')
    message = message.upper()

    encrypted = [ '' for x in range(len(message)) ]

    for i in range(n) :
        for j in range(i,len(encrypted),n) :
            encrypted[j] = message[0]
            message = message[1:]

    print(''.join(encrypted))
