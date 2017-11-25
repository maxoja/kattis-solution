start_grid = [['w','w','w'],['w','w','w'],['w','w','w']]
directions = [[0,0], [1,0],[-1,0],[0,1],[0,-1]]
target_pattern = [['w','w','w'],['w','w','w'],['w','w','w']]
history = []

def copy_grid(grid) :
    result = []
    for i in range(3) :
        result.append([])
        for j in range(3) :
            result[i].append(grid[i][j])

    return result
    
def reset() :
    history = []

def load_target_pattern() :
    global target_pattern
    
    for y in range(3) :
        row = input()
        for x,cell in enumerate(row) :
            if cell == '*' :
                target_pattern[y][x] = 'b'
            else :
                target_pattern[y][x] = 'w'
                
def out_of_range(x, y) :
    if x < 0 or x >= 3 :
        return True
    if y < 0 or y >= 3 :
        return True
    return False

def click_at(current, x, y) :
    global directions
    grid = copy_grid(current)
    
    for direction in directions :
        dx = direction[0]
        dy = direction[1]

        px = x+dx
        py = y+dy
        
        if out_of_range(px, py) :
            continue

        if grid[py][px] == 'w' :
            grid[py][px] = 'b'
        else :
            grid[py][px] = 'w'

    return grid

def match_pattern(a, b) :
    for x in range(3) :
        for y in range(3) :
            if a[y][x] != b[y][x] :
                return False

    return True

def match_target(grid) :
    global target_pattern
    return match_pattern(grid, target_pattern)

def match_history(grid) :
    global history

    for h in history :
        if match_pattern(grid, h) :
            return True

    return False

queue = []

def find_min_move() :
    global history

    queue.append((copy_grid(start_grid), 0))

    while len(queue) > 0 :
        task = queue[0]
        del queue[0]
        current = task[0]
        count = task[1]
        if match_pattern( current, target_pattern ) :
            return count

        for x in range(3) :
            for y in range(3):
                next = click_at(current,x,y)
                queue.append((next,count+1))
                
if __name__ == '__main__' :
    n = int(input())
    
    while n > 0 :
        reset()
        load_target_pattern()
        print(find_min_move())
        n-= 1
