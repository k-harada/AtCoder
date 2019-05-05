N = int(input())
A_list = list(map(int, input().split()))

res_list = [0]*N
count_list = [0]*30

for i in range(N):
    A = A_list[i]
    for j in range(29, -1, -1):
        if A >= 2 ** j:
            A -= 2 ** j
            count_list[j] += 1
    res = 0
    for j in range(29, -1, -1):
        if count_list[j] % 2 == 0:
            res += count_list[j] * (2 ** j)
        else:
            res += (i + 1 - count_list[j]) * (2 ** j)
    res_list[i] = res

for r in res_list:
    print(r)