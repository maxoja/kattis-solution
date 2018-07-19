from math import pi

a, n = tuple(map(float, input().split()))
print('Diablo is happy!' if (n**2)/4/pi >= a else 'Need more materials!')
