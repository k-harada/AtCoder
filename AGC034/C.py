from heapq import heappop, heappush

N, X = map(int, input().split())

b_list = [0]*N
l_list = [0]*N
u_list = [0]*N

for i in range(N):
    b, l, u = map(int, input().split())
    b_list[i] = b
    l_list[i] = l
    u_list[i] = u

# lose weight
lose_weight = sum([b_list[i]*l_list[i] for i in range(N)])

# win weight
win_weight = [(X - b_list[i])*u_list[i]+b_list[i]*l_list[i] for i in range(N)]

h = []
for i in range(N):
    heappush(h, (-win_weight[i], i))

used_flg = [0]*N
res = 0
while True:
    win, i = heappop(h)
    if win + lose_weight < 0:
        break
    elif win + lose_weight == 0:
        res += X
        used_flg[i] = 1
        lose_weight = 0
        break
    else:
        res += X
        used_flg[i] = 1
        lose_weight += win

r_min = X
i_min = -1
for i in range(N):
    if used_flg[i] == 0:
        if lose_weight > b_list[i]*l_list[i]:
            p = lose_weight - b_list[i]*l_list[i]
            q = u_list[i]
            if p % q == 0:
                r = p // q + b_list[i]
            else:
                r = p // q + b_list[i] + 1
            if r < r_min:
                r_min = r
                i_min = i
        else:
            p = lose_weight
            q = l_list[i]
            if p % q == 0:
                r = p // q
            else:
                r = p // q + 1
            if r < r_min:
                r_min = r
                i_min = i

res_temp = res + r_min

# post process
if i_min != -1:
    used_flg[i_min] = 1

post_list = [i for i in range(N) if used_flg[i] == 1]
win_total = sum([win_weight[i] for i in post_list])
lose_weight_org = sum([b_list[i]*l_list[i] for i in range(N)])

for i in post_list:
    lose_weight = lose_weight_org - (win_total - win_weight[i])

    if lose_weight > b_list[i] * l_list[i]:
        p = lose_weight - b_list[i] * l_list[i]
        q = u_list[i]
        if p % q == 0:
            r = p // q + b_list[i]
        else:
            r = p // q + b_list[i] + 1
        if r < r_min:
            r_min = r
            i_min = i
    else:
        p = lose_weight
        q = l_list[i]
        if p % q == 0:
            r = p // q
        else:
            r = p // q + 1
        if r < r_min:
            r_min = r
            i_min = i

print(res + r_min)

