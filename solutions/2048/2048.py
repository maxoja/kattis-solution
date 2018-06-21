grid = [ list(map(int, input().split())) for i in range(4) ]
merged = [ [False,]*4 for i in range(4) ]
direction = int(input())
dirmap = {0:'l', 1:'u', 2:'r', 3:'d'}
direction = dirmap[direction]

def push(y, x, d):
    val = grid[y][x]
    grid[y][x] = 0
    
    if d == 'l':
        while x-1 >= 0 and grid[y][x-1] == 0:
            x -= 1
        if x-1 >= 0 and not merged[y][x-1]and grid[y][x-1] == val:
            grid[y][x-1] += val
            merged[y][x-1] = True
        else:
            grid[y][x] = val

    elif d == 'r':
        while x+1 < 4 and grid[y][x+1] == 0:
            x += 1
        if x+1 < 4 and not merged[y][x+1] and  grid[y][x+1] == val:
            grid[y][x+1] += val
            merged[y][x+1] = True
        else:
            grid[y][x] = val

    elif d == 'u':
        while y-1 >= 0 and grid[y-1][x] == 0:
            y -= 1
        if y-1 >= 0 and not merged[y-1][x] and grid[y-1][x] == val:
            grid[y-1][x] += val
            merged[y-1][x] = True
        else:
            grid[y][x] = val

    elif d == 'd':
        while y+1 < 4 and grid[y+1][x] == 0:
            y += 1
        if y+1 < 4 and not merged[y+1][x] and grid[y+1][x] == val:
            grid[y+1][x] += val
            merged[y+1][x] = True
        else:
            grid[y][x] = val

if direction == 'l':
    for x in range(4):
        for y in range(4):
            push(y, x, direction)
elif direction == 'r':
    for x in range(4)[::-1]:
        for y in range(4):
            push(y, x, direction)

elif direction == 'u':
    for y in range(4):
        for x in range(4):
            push(y, x, direction)

elif direction == 'd':
    for y in range(4)[::-1]:
        for x in range(4):
            push(y, x, direction)

for row in grid:
    for col in row:
        print(col, end=' ')
    print()
        
