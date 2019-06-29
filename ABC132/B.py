n = int(input())
p_list = list(map(int, input().split()))

res_sum = 0

for i in range(n-2):
    res = True
    p, q, r = p_list[i], p_list[i+1], p_list[i+2]
    if q == min(p, q, r):
        res = False
    elif p == min(p, q, r) and r == min(p, q, r):
        res = False
    elif p == min(p, q, r):
        if q > r:
            res = False
    else:
        if q > p:
            res = False
    if res:
        res_sum += 1

print(res_sum)
