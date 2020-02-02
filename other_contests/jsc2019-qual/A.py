M, D = map(int, input().split())
res = 0

for m in range(1, M + 1):
    for d in range(1, D + 1):
        d1 = d // 10
        d2 = d % 10
        if m == d1 * d2 and d1 >= 2 and d2 >= 2:
            res += 1
print(res)
