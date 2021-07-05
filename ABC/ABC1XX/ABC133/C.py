L, R = map(int, input().split())

if R - L >= 2018:
    print(0)
else:
    res = 2018
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            r = (i * j) % 2019
            res = min(res, r)
    print(res)
