n = [1] + [0]*200
for i in [1, 2, 5, 10, 20, 50, 100, 200]:
    for j in range(i, 201): n[j] += n[j-i]
print(n[200])
