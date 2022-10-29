N, K = map(int, input().split())
LARGE = 10 ** 9 + 7

# (N - K - 1)Ci * (K - 1)C(i - 1)


def p_inv(k, p):
    return pow(k, p-2, p)


res_list = [0] * K

ncr1 = N - K + 1
ncr2 = 1
res_list[0] = N - K + 1

for i in range(2, min(N - K + 2, K + 1)):

    ncr1 *= N - K + 2 - i
    ncr1 *= p_inv(i, LARGE)
    ncr1 = ncr1 % LARGE

    ncr2 *= K + 1 - i
    ncr2 *= p_inv(i - 1, LARGE)
    ncr2 = ncr2 % LARGE

    res_list[i - 1] = (ncr1 * ncr2) % LARGE

for r in res_list:
    print(r)
