H, W = map(int, input().split())
S = [[0]*W for _ in range(H)]

for i in range(H):
    Si = list(input())
    for j in range(W):
        if Si[j] == '#':
            S[i][j] = 1

# row
S_row = [[0]*W for _ in range(H)]
for i in range(H):
    c = 0
    for j in range(W):
        if S[i][j] == 1:
            c = 0
        else:
            c += 1
        S_row[i][j] = c
    # reverse
    for j in range(W-2, -1, -1):
        if S_row[i][j+1] > 0 and S_row[i][j] > 0:
            S_row[i][j] = S_row[i][j+1]

# col
S_col = [[0]*W for _ in range(H)]
for j in range(W):
    c = 0
    for i in range(H):
        if S[i][j] == 1:
            c = 0
        else:
            c += 1
        S_col[i][j] = c
    # reverse
    for i in range(H-2, -1, -1):
        if S_col[i+1][j] > 0 and S_col[i][j] > 0:
            S_col[i][j] = S_col[i+1][j]

# res
res = max([max([S_row[i][j] + S_col[i][j] - 1 for j in range(W)]) for i in range(H)])
print(res)
