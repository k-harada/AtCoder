MOD = 998244353


def solve(a, b):
    primes = []
    counts = []
    # aを素因数分解
    x = a
    for i in range(2, a):
        if i * i > a:
            break
        c = 0
        while x % i == 0:
            c += 1
            x //= i
        if c > 0:
            primes.append(i)
            counts.append(c)
    if x > 1:
        primes.append(x)
        counts.append(1)
    # print(primes)
    # print(counts)
    even = 0
    if b % 2 == 0:
        even += 1
    res = b
    for c in counts:
        res *= (1 + b * c)
        if (b * c) % 2 == 1:
            even += 1
        res %= MOD
    if even == 0:
        res -= 1
        res %= MOD
    res *= pow(2, MOD - 2, MOD)
    res %= MOD
    return res


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(2, 3) == 6
    assert solve(924, 167) == 867046524
    assert solve(167167167167, 0) == 0


if __name__ == "__main__":
    test()
    main()
