#!/usr/bin/python
def chain(x):
    count = 1
    while x != 1:
        if x % 2 == 0:
            x /= 2
            count += 1
        else:
            x = (x * 3) + 1
            count += 1
    return count

count = 500001
temp = 0
while count < 1000000:
    if chain(count) > temp:
        ans = count
        temp = chain(count)
    count += 2
print(ans)
