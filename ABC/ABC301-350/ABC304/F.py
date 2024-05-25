MOD = 998244353


def solve(n, s):
    # 約数全列挙
    factors = [1]
    for i in range(2, n + 1):
        if i * i > n:
            break
        elif i * i == n:
            factors.append(i)
            break
        elif n % i == 0:
            factors.append(i)
            factors.append(n // i)
    factors = list(sorted(factors))
    # print(factors)
    counter = [0] * len(factors)
    for i, m in enumerate(factors):
        counter_m = [1] * m
        for j, c in enumerate(s):
            if c == ".":
                counter_m[j % m] = 0
        r = pow(2, sum(counter_m), MOD)
        for p in range(i):
            if m % factors[p] == 0:
                r -= counter[p]
                r %= MOD
        counter[i] = r
    return sum(counter) % MOD


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(6, "##.#.#") == 3
    assert solve(7, "...####") == 1
    assert solve(12, "####.####.##") == 19


def test_large():
    print(solve(40320, "#" * 40320))


if __name__ == "__main__":
    test()
    # test_large()
    main()
