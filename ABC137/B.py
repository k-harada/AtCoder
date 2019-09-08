K, X = map(int, input().split())

res_min = max(-100000, X - K + 1)
res_max = min(100000, X + K - 1)

print(" ".join([str(i) for i in range(res_min, res_max + 1)]))
