#!/usr/bin/python
letters = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def score(x): return sum([letters.index(x[i]) for i in range(len(x))])
nlist = [i.strip('"') for i in open("22.txt", "r").read().split(",")]
nlist.sort()
print(sum([(nlist.index(i)+1) * score(i) for i in nlist]))
