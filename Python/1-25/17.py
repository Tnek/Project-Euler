#!/usr/bin/python
s = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
t = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
d = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

ans = 0
for i in range(1, 1000):
    if i >= 100:
        if int(str(i)[1]) != 0 or int(str(i)[2]) != 0:
            ans += len("and")
        if int(str(i)[1]) == 1:
            ans += len(t[int(str(i)[2])])
        else:
            ans += len(d[int(str(i)[1])])
            ans += len(s[int(str(i)[2])])
        ans += len(s[int(str(i)[0])])
        ans += len("hundred")
    elif i >= 10:
        if int(str(i)[0]) == 1:
            ans += len(t[int(str(i)[1])])
        else:
            ans += len(d[int(str(i)[0])])
            ans += len(s[int(str(i)[1])])
    elif i < 10:
        ans += len(s[i])
ans += len("onethousand")
print(ans)
