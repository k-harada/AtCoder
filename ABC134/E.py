from bisect import bisect_left
N = int(input())
A_list = [0] * N
for i in range(N):
    A_list[i] = int(input())

res_list = [-1] * N
for i in range(N):
    j = bisect_left(res_list, A_list[i])
    res_list[j - 1] = A_list[i]

res = 0
for i in range(N):
    if res_list[i] >= 0:
        res += 1

print(res)
