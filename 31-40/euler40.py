#!/usr/bin/python
count = 1
d = " "
while len(d) <= 1000000:
    d += str(count)
    count += 1
print(int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000]))
