import math

attitude, degree = tuple(map(int,input().split()))
speed = 1
radian = degree/180*math.pi
sin_value = math.sin(radian)
speed_y = sin_value*speed

if speed_y > 0 :
    print('safe')
else :
    print(int(attitude/(-1*speed_y)))
