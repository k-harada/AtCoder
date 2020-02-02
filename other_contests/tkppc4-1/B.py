N, K = map(int, input().split())
a_list = list(map(int, input().split()))

a_max = 0
res = -1

for i in range(N):
    a = a_list[i]
    if a < K:
        if a > a_max:
            a_max = a
            res = i + 1

print(res)
