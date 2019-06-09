N = int(input())
W_list = list(map(int, input().split()))

S1 = 0
S2 = sum(W_list)

res = abs(S2 - S1)

for i in range(N):
    S1 += W_list[i]
    S2 -= W_list[i]
    r = abs(S2 - S1)
    if r < res:
        res = r

print(res)
