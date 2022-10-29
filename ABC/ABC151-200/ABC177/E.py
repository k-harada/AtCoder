def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(n, a_list):

    # set-wise co-prime
    r = a_list[0]
    for i in range(1, n):
        r = gcd(r, a_list[i])
    if r != 1:
        return 'not coprime'

    # prime factorization
    # list primes
    primes_1st = list(range(10 ** 6 + 1))
    for p in range(2, 10 ** 3):
        if primes_1st[p] == p:
            for q in range(p * p, 10 ** 6 + 1, p):
                primes_1st[q] = p

    primes_count = [0] * (10 ** 6 + 1)
    for i in range(n):
        a = a_list[i]
        prime_factors = []
        while a > 1:
            prime_factors.append(primes_1st[a])
            a = a // primes_1st[a]
        for p in set(prime_factors):
            primes_count[p] += 1
    if max(primes_count) > 1:
        return 'setwise coprime'
    else:
        return 'pairwise coprime'


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve(3, [3, 4, 5]) == 'pairwise coprime'
    assert solve(3, [6, 10, 15]) == 'setwise coprime'
    assert solve(3, [6, 10, 16]) == 'not coprime'


if __name__ == "__main__":
    test()
    main()
