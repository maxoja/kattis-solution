remaining = 4
year = int(input())

windowyears = {2018,}
current = 2018

while True:
    if current == year:
        print('yes')
        break
    
    current += 2
    remaining += 2
    while remaining > 12:
        remaining -= 12
        current += 1
    windowyears.add(current)

    if current > year:
        print('no')
        break

