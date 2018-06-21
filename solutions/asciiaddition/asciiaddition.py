convert = {
    'xxxxxx...xx...xx...xx...xx...xxxxxx':0,
    '....x....x....x....x....x....x....x':1,
    'xxxxx....x....xxxxxxx....x....xxxxx':2,
    'xxxxx....x....xxxxxx....x....xxxxxx':3,
    'x...xx...xx...xxxxxx....x....x....x':4,
    'xxxxxx....x....xxxxx....x....xxxxxx':5,
    'xxxxxx....x....xxxxxx...xx...xxxxxx':6,
    'xxxxx....x....x....x....x....x....x':7,
    'xxxxxx...xx...xxxxxxx...xx...xxxxxx':8,
    'xxxxxx...xx...xxxxxx....x....xxxxxx':9,
    '.......x....x..xxxxx..x....x.......':'+'
}
reverse = { str(convert[k]):k for k in convert }

data = [ input() for i in range(7) ]
n = (len(data[0])+1)//6

a = 0
b = 0
addfound = False

for i in range(n):
    string = ''.join([ data[y][i*6:i*6+5] for y in range(7)])
    d = convert[ string ]

    if d == '+':
        addfound = True
    elif addfound:
        b *= 10
        b += d
    else:
        a *= 10
        a += d

ans = str(a+b)
result = [ list('.'*(len(ans)*6 - 1)) for i in range(7) ]

for i in range(len(ans)):
    c = ans[i]
    
    for y in range(7):
        for x in range(5):
            result[y][i*6 + x] = reverse[c][y*5+x]

for r in result:
    print(''.join(r))
        
