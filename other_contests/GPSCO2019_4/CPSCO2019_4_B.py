# B

# input
N, D = map(int, input().split())
worktable = [[0]*N for _ in range(D)]

for d in range(D):
    S = list(input())
    for n in range(N):
        if S[n] == "o":
            worktable[d][n] = 1

# bruce
res = 0
for d1 in range(D):
    for d2 in range(d1+1, D):
       r = 0
       for n in range(N):
           if worktable[d1][n] == 1 or worktable[d2][n] == 1:
               r += 1
       if r > res:
           res = r

print(res)
