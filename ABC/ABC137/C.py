from collections import defaultdict

N = int(input())
d = defaultdict(int)

for _ in range(N):
    s = "".join(sorted(input()))
    d[s] += 1

res = 0
for k in d.keys():
    res += d[k] * (d[k] - 1) // 2

print(res)
