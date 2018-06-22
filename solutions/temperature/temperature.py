'''
brief : this problem can be transform into the following elementary math problem
"find the intersection between two lines"
'''

c, m = tuple(map(int, input().split()))

if c == 0 and m == 1:
    print('ALL GOOD')
elif c != 0 and m == 1:
    print('IMPOSSIBLE')
else:
    print(c/(1-m))
    
