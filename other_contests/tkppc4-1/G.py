LARGE = 10 ** 9 + 7

Q = int(input())
N_list = list(map(int, input().split()))
res_list = [0] * Q

for i in range(Q):
    n = N_list[i]
    if n <= 1:
        res = n
    else:
        if n % 3 == 0:
            res = pow(3, n // 3, LARGE)
        elif n % 3 == 1:
            res = (pow(3, (n - 4) // 3, LARGE) * 4) % LARGE
        else:
            res = (pow(3, (n - 2) // 3, LARGE) * 2) % LARGE
    res_list[i] = res

print(" ".join([str(r) for r in res_list]))
