N, K = map(int, input().split())
A_list = list(map(int, input().split()))

LARGE = 10 ** 9 + 7
res_lr = 0
res_rl = 0

for i in range(N):
    for j in range(N):
        if A_list[i] > A_list[j]:
            if i < j:
                res_lr += 1
            else:
                res_rl += 1

res_1 = (res_lr * K) % LARGE
res_2 = ((res_lr + res_rl) * K * (K - 1) // 2) % LARGE

print((res_1 + res_2) % LARGE)
