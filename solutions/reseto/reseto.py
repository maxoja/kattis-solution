# Problem: Reseto
# URL: https://open.kattis.com/problems/reseto
# Start Date: 2018.7.19 - 18.45
# Accepted Date: 2018.7.19 - 19.06
# Coder: Tawan Thampipattanakul

def inputs():
    line = input()
    words = line.split()
    ints = map(int, words)
    return tuple(ints)

if __name__ == '__main__':
    n, k = inputs()
    crossed = [False]*(n+1)
    base = 2
    
    while k > 0:
        while crossed[base]:
            base += 1
            
        multiple = base
        
        while multiple <= n:
            if not crossed[multiple]:
                crossed[multiple] = True
                k -= 1
                
                if k == 0:
                    print(multiple)
                    break
            
            multiple += base
