p,a,b,c,d,n = tuple(map(int, input().split()))
maxd, maxv = None,None

from math import cos, sin, pi

def func(i):
    return p*(sin(a*i+b) + cos(c*i+d) + 2)

for i in range(1,n+1):
    price = func(i)
    if maxv == None or price > maxv:
        maxv = price
    if maxd == None or maxd < maxv-price:
        maxd = maxv-price

if maxd == None or maxd == 0:
    print('0.00')
else:
    print(maxd)
