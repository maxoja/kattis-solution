def invalid(x, y, size_x, size_y) :
    return x < 0 or x >= size_x or y < 0 or y >= size_y

def next_day(old, size_x, size_y) :
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    result = []
    
    for y in range(size_y) :
        result.append('')
        for x in range(size_x) :
            prev = old[y][x]
            new = prev
            
            for direction in directions :
                dx = direction[0]
                dy = direction[1]

                px = x + dx
                py = y + dy

                if invalid(px,py,size_x,size_y) :
                    continue

                near = old[py][px]

                if prev == 'R' and near == 'P' :
                    new = near
                    break
                if prev == 'P' and near == 'S' :
                    new = near
                    break
                if prev == 'S' and near == 'R' :
                    new = near
                    break
                
            result[y] += new

    return result

n = int(input())
first = True

for _ in range(n) :
    if not first :
        print()

    size_y, size_x, n_day = tuple(map(int,input().split()))
    board = [ input() for __ in range(size_y) ]

    for __ in range(n_day) :
        board = next_day(board, size_x, size_y)

    for i in range(size_y) :
        print(''.join(board[i]))

    first = False
