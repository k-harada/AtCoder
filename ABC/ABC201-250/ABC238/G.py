from subprocess import Popen, PIPE


# from nagiss-san's AC
def fast_prime_factorization(n):
    # 素因数分解（ロー法）  O(n^(1/4) polylog(n))
    return list(map(int, Popen(["factor", str(n)], stdout=PIPE).communicate()[0].split()[1:]))


def solve(n, q, a_list, lr_list):
    small_primes = dict()
    large_primes = dict()
    primes = [1] * 1000001
    primes[0] = 0
    primes[1] = 0
    for p in range(1001):
        if primes[p]:
            for q in range(p * p, 1001, p):
                primes[q] = 0

    for p in range(1001):
        if primes[p]:
            small_primes[p] = [0] * n
    for i, a in enumerate(a_list):
        r = fast_prime_factorization(a)
        for p in r:
            if p < 1000:
                small_primes[p][i] += 1

    small_primes_cum = dict()
    for p in small_primes.keys():
        s = 0
        cum = [0]
        for c in small_primes[p]:
            s += c
            cum.append(s)
        small_primes_cum[p] = cum

    res = []

    for l, r in lr_list:
        fail = 0
        for p in small_primes_cum.keys():
            if (small_primes_cum[p][r] - small_primes_cum[p][l - 1]) % 3 != 0:
                fail = 1
                break

        if fail == 1:
            res.append("No")
        else:
            res.append("Yes")

    return res


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    lr_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, a_list, lr_list)
    for r in res:
        print(r)


def test():
    assert solve(8, 5, [7, 49, 30, 1, 15, 8, 6, 10], [(1, 2), (2, 3), (4, 4), (5, 8), (3, 8)]) == [
        "Yes", "No", "Yes", "No", "Yes"
    ]


if __name__ == "__main__":
    test()
    main()
