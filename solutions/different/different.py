import sys

def getdif(stra, strb, i, bor):
    if i < 0:
        return ''

    a = int(stra[i])
    b = int(strb[i])
    c = a - b - bor

    if c >= 0:
        bor = 0
    else:
        bor = 1
        c += 10

    return getdif(stra, strb, i-1, bor) + str(c)


def smaller(stra, strb, i):
    if i >= len(stra):
        return False
    
    a = int(stra[i])
    b = int(strb[i])

    if a < b:
        return True
    elif a == b:
        return smaller(stra, strb, i+1)
    else:
        return False


for line in sys.stdin:
    inputs = line.split()
    stra = inputs[0]
    strb = inputs[1]

    lena = len(stra)
    lenb = len(strb)

    if lena < lenb:
        stra, strb, lena, lenb = strb, stra, lenb, lena
    elif lena == lenb and smaller(stra, strb, 0):
        stra, strb, lena, lenb = strb, stra, lenb, lena

    strb = '0'*(lena-lenb) + strb

##    print(stra, strb)

    result = getdif(stra, strb, lena-1, 0)
    while result[0] == '0' and len(result) > 1:
        result = result[1:]
    print(result)

