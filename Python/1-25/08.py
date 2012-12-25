#!/usr/bin/python
n = open("08.txt", "r").read()
c = 1 ; ans = []
for x in range(len(n)-5):
    temp = n[x:x+5]
    for y in range(5): c*= int(temp[y])
    ans.append(c) ; c = 1
print(max(ans))
