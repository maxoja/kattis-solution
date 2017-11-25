import math

def check_n_fact(n, limit) :
    accumulator = 1
    for i in range(1,n+1) :
        if accumulator*i > limit :
            return False
        
        accumulator *= i

    return True

def check_two_power_n(n, limit) :
    accumulator = 1
    for i in range(n) :
        if accumulator*2 > limit :
            return False
        accumulator *= 2

    return True

def check_n_power_four(n,limit) :
    for i in range(1,5) :
        if n**i > limit :
            return False

    return True

def check_n_power_three(n,limit) :
    for i in range(1,4) :
        if n**i > limit :
            return False

    return True

def check_n_power_two(n,limit) :
    for i in range(1,3) :
        if n**i > limit :
            return False

    return True

def check_n_log_n(n, limit) :
    return math.log(n,2) <= limit/n

def check_n(n,limits) :
    return n <= limits

input_values = tuple(map(int,input().split()))
clock_speed, n, big_o_type = input_values

checks = [check_n_fact, check_two_power_n, check_n_power_four, check_n_power_three, check_n_power_two, check_n_log_n, check_n]
print('AC') if checks[big_o_type-1](n, clock_speed) else print('TLE')
    

