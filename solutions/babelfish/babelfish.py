import sys

line = input()
lex = dict()

while line != '':
    eng, bar = line.split()
    lex[bar] = eng
    line = input()

##print(lex)

for word in sys.stdin:
    word = word[:-1]
    if word not in lex:
        print('eh')
    else:
        print(lex[word])
