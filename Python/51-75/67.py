#!/usr/bin/python
n = [[int(i) for i in j.split()] for j in open("67.txt", "r").readlines()]
n.reverse()

for r in range(len(n)):
    for c in range(len(n[r])):
        try: n[r+1][c] = max([n[r][c] + n[r+1][c], n[r][c + 1] + n[r+1][c]])
        except IndexError: pass
print(n[-1])
