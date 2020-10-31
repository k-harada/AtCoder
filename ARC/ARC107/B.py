def solve(n, k):
    count_ab = [0] * (2 * n + 1)
    for i in range(1, n + 1):
        count_ab[i] = (i - 1)
    for i in range(n + 1, 2 * n + 1):
        count_ab[i] = 2 * n + 1 - i

    res = 0
    for i in range(2, 2 * n + 1):
        if 2 <= k + i <= 2 * n:
            res += count_ab[i] * count_ab[k + i]
    # print(count_ab, res)
    return res


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(2, 1) == 4
    assert solve(2525, -425) == 10314607400


if __name__ == "__main__":
    test()
    main()
