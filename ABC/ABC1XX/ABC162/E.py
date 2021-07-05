MOD = 10 ** 9 + 7


def solve(n, k):
    # primes
    is_prime = [1] * (k + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for p in range(2, k + 1):
        if p * p > k:
            break
        if is_prime[p]:
            for q in range(p * p, k + 1, p):
                is_prime[q] = 0
    primes = [p for p in range(k + 1) if is_prime[p]]

    res_arr = [0] + [pow(k // i, n, MOD) for i in range(1, k + 1)]
    # print(res_arr)
    for p in primes:
        for i in range(1, k // p + 1):
            res_arr[i] -= res_arr[i * p]
    # print(res_arr)
    res = sum([i * res_arr[i] for i in range(k + 1)]) % MOD
    # print(res)
    return res


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(3, 2) == 9
    assert solve(3, 200) == 10813692
    # assert solve(100000, 100000) == 742202979


if __name__ == "__main__":
    test()
    main()
