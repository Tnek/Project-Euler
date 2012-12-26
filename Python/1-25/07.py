import math
n = 200000
plist = [False] * 2 + [True] * n
for i in range(2, int(math.sqrt(n))+2):
    if plist[i]:
        for j in range(i**2, n+1, i): plist[j] = False
print([i for i in range(len(plist)) if plist[i]][10000])
