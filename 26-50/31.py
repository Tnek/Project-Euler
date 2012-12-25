n = [0 for i in range(201)]; n[0] = 1
for i in [1, 2, 5, 10, 20, 50, 100, 200]:
    for j in range(i, 200 + 1): n[j] += n[j-i]
print(n[200])
