#!/usr/bin/python
n = [[int(j) for j in i] for i in [i.split() for i in open("11.txt", "r").readlines()]]
z = []
for i in n:  # Horizontally
    for j in range(len(i)):
        try: z.append(i[j] * i[j+1] * i[j+2] * i[j+3])
        except Exception: pass
for i in range(len(n)):  # Vertically
    for j in range(len(n[i])):
        try: z.append((n[i])[j] * (n[i+1])[j] * (n[i+2])[j] * (n[i+3])[j])
        except Exception: pass
for i in range(len(n)):  # Diagonally
    for j in range(len(n[i])):
        try: z.append((n[i])[j] * (n[i+1])[j+1] * (n[i+2])[j+2] * (n[i+3])[j+3])
        except Exception: pass
        try: z.append((n[i])[j] * (n[i-1])[j+1] * (n[i-2])[j+2] * (n[i-3])[j+3])
        except Exception: pass
print(max(z))
