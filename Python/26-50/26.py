def check(x):
    for i in range(1, x):
        if 1 == 10**i % x: return i
c = [check(i) for i in range(1000)]
n = range(1000)
print(n[c.index(max(c))])
