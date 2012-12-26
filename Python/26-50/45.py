import math
hexa = lambda x: x * (2*x - 1)
def pent(x):
    y = (math.sqrt(1 + 24*x) + 1) / 6
    return y == int(y)
x = 144
while not pent(hexa(x)): x += 1
print(hexa(x))
