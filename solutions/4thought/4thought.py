def check(ops, ans):
    if len(ops) == 3:
        s = '4 ' + ops[0] + ' 4 ' + ops[1] + ' 4 ' + ops[2] + ' 4'
        result = eval(s)
        if result == ans:
            return s
        else:
            return False

    for o in ['+','-','*','//']:
        ops.append(o)
        r = check(ops, ans)
        if r != False:
            return r
        else:
            ops.pop()

    return False

t = int(input())
for _ in range(t):
    n = int(input())
    result = check([], n)
    if result == False:
        print('no solution')
    else:
        print(result.replace('//', '/'),'=',n)
