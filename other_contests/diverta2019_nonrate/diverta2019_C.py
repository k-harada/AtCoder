N = int(input())

res = 0
BxA = 0
xxA = 0
Bxx = 0

for _ in range(N):
    s = list(input())
    for i in range(len(s) - 1):
        if s[i] + s[i + 1] == "AB":
            res += 1
    if s[0] == "B" and s[-1] == "A":
        BxA += 1
    elif s[0] == "B":
        Bxx += 1
    elif s[-1] == "A":
        xxA += 1

res_2 = 0
if xxA == 0 and Bxx == 0 and BxA != 0:
    res_2 = BxA - 1
else:
    res_2 = min(BxA + xxA, Bxx + BxA)

print(res + res_2)