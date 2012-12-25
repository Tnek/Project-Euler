#!/usr/bin/python
print(str(sum([int(i) for i in open("13.txt", "r").readlines()]))[:10])
