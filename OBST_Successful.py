keys = [10, 20, 30, 40]
p = [0, 0.1 ,0.2 ,0.4 ,0.3] 
n = len(keys)

C = [[0] * (n + 2) for _ in range(n + 2)]
R = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(1, n + 1):
    C[i][i - 1] = 0
    C[i][i] = p[i]
    R[i][i] = i

C[n + 1][n] = 0

for d in range(1, n):
    for i in range(1, n - d + 1):
        j = i + d
        min_cost = float('inf')
        total_prob = sum(p[i:j + 1])
        for k in range(i, j + 1):
            cost = C[i][k - 1] + C[k + 1][j]
            if cost < min_cost:
                min_cost = cost
                Kmin = k
        C[i][j] = min_cost + total_prob
        R[i][j] = Kmin

print(C[1][n])