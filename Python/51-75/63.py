#!/usr/bin/python
x = 0; count = 0; i = 0
for i in range(22):
    while len(str(x**i)) <= i:
        x += 1
        if len(str(x**i)) == i: count += 1
    x = 0
print(count)
