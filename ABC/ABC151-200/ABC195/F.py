def solve(a, b):

    primes = [
        2, 3, 5, 7, 11,
        13, 17, 19, 23, 29,
        31, 37, 41, 43, 47,
        53, 59, 61, 67, 71
    ]

    dp = [[0] * (2 ** 20) for _ in range(a, b + 2)]
    dp[0][0] = 1

    for i in range(a, b + 1):
        d = 0
        for j in range(20):
            if i % primes[j] == 0:
                d += 2 ** j
        for k in range(2 ** 20):
            dp[i - a + 1][k] += dp[i - a][k]
        for k in range(2 ** 20):
            if k ^ d == k + d:
                dp[i - a + 1][k + d] += dp[i - a][k]

    return sum(dp[-1])


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(2, 4) == 6
    assert solve(1, 1) == 2
    # assert solve(123456789000, 123456789050) == 2125824


if __name__ == "__main__":
    test()
    main()
