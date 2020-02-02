M, K = map(int, input().split())

if K >= 2**M:
    print(-1)
elif M == 1 and K == 1:
    print(-1)
elif M == 1 and K == 0:
    print("0 0 1 1")
else:
    x_list = list(range(2**M))
    x_k_list = [x for x in x_list if x != K]
    res_list = x_k_list + [K] + list(reversed(x_k_list)) + [K]
    print(" ".join([str(r) for r in res_list]))
