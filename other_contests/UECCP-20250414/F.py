from subprocess import Popen, PIPE


# from nagiss-san's AC
def fast_prime_factorization(n):
    # 素因数分解（ロー法）  O(n^(1/4) polylog(n))
    return list(map(int, Popen(["factor", str(n)], stdout=PIPE).communicate()[0].split()[1:]))


def solve(k):
    primes = fast_prime_factorization(k)
    primes_count = dict()
    for p in primes:
        if p not in primes_count.keys():
            primes_count[p] = 1
        else:
            primes_count[p] += 1
    res = 1
    for p in primes_count.keys():
        c = primes_count[p]
        x = 0
        v = 0
        r = 0
        while x + p ** r <= c:
            x += p ** r
            v = p ** (r + 1)
            r += 1
        # print(c, x, v, r)
        for s in range(r, 0, -1):
            k = (c - x) // ((p ** s - 1) // (p - 1))
            x += k * (p ** s - 1) // (p - 1)
            v += k * (p ** s)
        # print(p, v)
        res = max(res, v)

    return res


def main():
    k = int(input())
    res = solve(k)
    print(res)


if __name__ == "__main__":
    main()
