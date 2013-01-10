def check(x):
    for i in range(1, x):
        if 1 == 10**i % x: return i
    return 0
c = [check(i) for i in range(1000)]
print(c.index(max(c)))
