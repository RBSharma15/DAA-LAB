keys = [10, 20, 30, 40]
p = [0, 0.1, 0.2, 0.4, 0.3]
q = [0.05, 0.1 ,0.05, 0.05, 0.1]  

n = len(keys)

C = [[0] * (n + 2) for _ in range(n + 2)]
W = [[0] * (n + 2) for _ in range(n + 2)]
R = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(1, n + 2):
    C[i][i-1] = q[i-1]
    W[i][i-1] = q[i-1]

for length in range(1, n + 1):  
    for i in range(1, n - length + 2):
        j = i + length - 1
        W[i][j] = W[i][j-1] + p[j] + q[j]
       
        min_cost = float('inf')
        root = None
        for r in range(i, j + 1):
            cost = C[i][r-1] + C[r+1][j] + W[i][j]
            if cost < min_cost:
                min_cost = cost
                root = r
       
        C[i][j] = min_cost
        R[i][j] = root

print(f"Minimum expected cost: {C[1][n]}")
print("Root matrix (R):")
for row in R[1:n+1]:
    print(row[1:n+1])