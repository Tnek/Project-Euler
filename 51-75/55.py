palin_add = lambda x: x + int(str(x)[::-1])
lychrel = [False for i in range(10000)]

temp = []

for i in range(len(lychrel)):
    if lychrel[i]: pass
    else:
        x = i
        temp = []
        for j in range(1, 51):
            temp.append(i)
            x = palin_add(x)
            if x == int(str(x)[::-1]):
                for k in temp: lychrel[k] = True
                break
print(lychrel.count(False))
