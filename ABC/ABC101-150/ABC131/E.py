# 答えみた
N, K = map(int, input().split())

M = N - 1
flg = 1
R = (N-1) * (N-2) // 2
edge_list = []
for i in range(2, N+1):
    edge_list.append([1, i])

if K > R:
    flg = -1
elif K == R:
    pass
else:
    for i in range(2, N):
        for j in range(i+1, N+1):
            edge_list.append([i, j])
            M += 1
            R -= 1
            if K == R:
                break
        if K == R:
            break

if flg == -1:
    print(-1)
else:
    print(M)
    for edge in edge_list:
        p, q = edge
        print(str(p), str(q))
