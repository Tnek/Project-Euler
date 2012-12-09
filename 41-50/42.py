#!/usr/bin/python
import math
FILE = open("42.txt", "r")
temp = FILE.read()
wlist = [word.strip('"') for word in temp.split(',')] 

letters = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def score(x): return sum([letters.index(x[i]) for i in range(len(x))])

def tri(x):
    y = (math.sqrt(8*x + 1) - 1) / 2
    return y == int(y)
print(len([i for i in wlist if tri(score(i))]))
