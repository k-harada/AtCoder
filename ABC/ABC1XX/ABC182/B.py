def solve(n, a_list):
    # primes
    primes = [1] * 1000
    primes[0] = 0
    primes[1] = 0
    for p in range(1000):
        if primes[p]:
            for q in range(p * p, 1000, p):
                primes[q] = 0

    res = -1
    gcd_cnt = 0
    for p in range(2, 1000):
        r = 0
        if primes[p] == 0:
            continue
        for a in a_list:
            if a % p == 0:
                r += 1
        if r > gcd_cnt:
            res = p
            gcd_cnt = r
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [3, 12, 7]) == 3
    assert solve(5, [8, 9, 18, 90, 72]) == 2
    assert solve(5, [1000, 1000, 1000, 1000, 1000]) == 2


if __name__ == "__main__":
    test()
    main()
