N = int(input())

res = 0


for p in range(1, 10**6+2):
    if N % p == 0:
        q = N // p - 1
        if q > p:
            res += q
        else:
            break

print(res)
