p = int(input())
a_list = list(map(int, input().split()))
r_list = [0] * p

fact = [0] * p
fact[0] = 1
for i in range(1, p):
    fact[i] = fact[i - 1] * i % p

fact_inv = [0] * p
fact_inv[-1] = pow(fact[-1], p-2, p)
for i in range(p-2, -1 ,-1):
    fact_inv[i] = (fact_inv[i+1] * (i+1)) % p

ncr = [(fact[p-1] * fact_inv[p-1-i] * fact_inv[i]) % p for i in range(p)]

for j in range(p):
    if a_list[j] == 0:
        continue
    k = 1
    for i in range(p-1, -1, -1):
        r_list[i] -= ncr[i] * k
        r_list[i] %= p
        k *= -j
        k %= p
    r_list[0] += 1

r_list[0] %= p
print(*r_list)
