from bisect import bisect_right


def solve(n):
    primes = [1] * (10 ** 6)
    primes[0] = 0
    primes[1] = 0
    for p in range(10 ** 6):
        if primes[p] == 1:
            for q in range(p * p, 10 ** 6, p):
                primes[q] = 0
    res = 0
    primes = [p for p in range(10 ** 6) if primes[p]]
    for k in range(2, len(primes)):
        c = primes[k]
        m0 = c ** 2
        if m0 > n:
            break
        for i in range(k):
            a = primes[i]
            m1 = m0 * (a ** 2)
            if m1 * a >= n:
                break
            r = n // m1
            bc = bisect_right(primes, r)
            bc = min(bc, k)
            if bc > i + 1:
                res += bc - (i + 1)

    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(1000) == 3
    assert solve(1000000000000) == 2817785


if __name__ == "__main__":
    # test()
    main()
