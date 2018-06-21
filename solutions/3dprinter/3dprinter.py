from math import log
from math import ceil

n_statue = int(input())
print(ceil(log(n_statue, 2))+1)

##for i in range(1, 100000):
##    if 2**(i-1) >= n_statue:
##        print(i)
##        break
