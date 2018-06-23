n = int(input())
expected = 0
probs = []

for i in range(n):
    prob = float(input().split()[1])
    probs.append(prob)

expected = sum( [ (i+1)*p for i,p in enumerate(sorted(probs,reverse=True)) ] )

print(expected)
