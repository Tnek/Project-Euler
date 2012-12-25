import math
hexa = lambda x: x * (2*x - 1)
def penta_check(x):
    y = (math.sqrt(1 + 24*x) + 1) / 6
    return y == int(y)
x = 144
while not penta_check(hexa(x)): x += 1
print(hexa(x))
