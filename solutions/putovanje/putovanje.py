# Problem: putovanje
# URL: https://open.kattis.com/problems/putovanje
# Start Date: 2018.7.19 - 19.21
# Accepted Date: 2018.7.19 - 19.38
# Coder: Tawan Thampipattanakul

def getInputs():
    return tuple(map(int, input().split()))

def getFruits():
    return list(map(int, input().split()))

def getFruitCount(fruits, space, i, count = 0):
    if i >= len(fruits):
        return count
    if fruits[i] > space:
        return getFruitCount(fruits, space, i+1, count)
    else:
        return getFruitCount(fruits, space-fruits[i], i+1, count+1)
    
def getMaximum(c, fruits, start=0):
    if start >= len(fruits):
        return 0
    else:
        return max(getFruitCount(fruits, c, start), getMaximum(c, fruits, start+1))

if __name__ == '__main__':
    n, c = getInputs()
    fruits = getFruits()
    best = getMaximum(c, fruits)

    print(best)
