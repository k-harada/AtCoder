from bisect import bisect_right
from collections import defaultdict

s = list(input())
t = list(input())

L = len(s)
M = len(t)

ss = s * 2

ind_dict = defaultdict(list)
for i in range(2 * L):
    ind_dict[ss[i]].append(i)


def query_str(c, ind):
    if len(ind_dict[c]) == 0:
        return -1
    else:
        r = bisect_right(ind_dict[c], ind)
        return ind_dict[c][r]


res_total = 0
res = -1
for i in range(M):
    res = query_str(t[i], res)
    if res == -1:
        res_total = 0
        break
    if res >= L:
        res -= L
        res_total += L

if res == -1:
    print(-1)
else:
    print(res_total + res + 1)

