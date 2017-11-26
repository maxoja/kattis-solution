def fact(n) :
    if n <= 1 :
        return 1
    return int(n*fact(n-1))

def stop_fact(a,b) :
    result = 1
    for i in range(a,b+1) :
        result *= i

    return result

def ncr(n,r) :
    return stop_fact(n-r+1,n)//fact(r)

n = int(input())
count = 0

for i in range(2,n+1) :
    if n < i :
        count += ncr(n,i)
    else :
        count += ncr(n,n-i)

print(count)
