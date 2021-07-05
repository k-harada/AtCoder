MOD = 10 ** 9 + 7


def solve(n, k):
    cum_left = [0] * (n + 2)
    cum_right = [0] * (n + 2)
    for i in range(n + 1):
        cum_left[i + 1] = cum_left[i] + i
        cum_right[i + 1] = cum_right[i] + n - i
    # print(cum_left, cum_right)
    res = 0
    for i in range(k, n + 2):
        res += cum_right[i] - cum_left[i] + 1
        res %= MOD
    return res


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(3, 2) == 10
    assert solve(200000, 200001) == 1
    assert solve(141421, 35623) == 220280457


if __name__ == "__main__":
    test()
    main()
