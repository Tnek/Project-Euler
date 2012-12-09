#!/usr/bin/python
a = 1; b = 1; count = 2
while len(str(a)) < 1000:
    temp = a; a += b; b = temp; count += 1
print(count)
