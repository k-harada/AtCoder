def solve(n, m):
    i_max = [-1] * 10
    for d in range(1, 10):
        res = 0
        for i in range(n):
            res = res * 10 + d
            res %= m
            if res == 0:
                i_max[d] = i + 1
    r = max(i_max)
    # print(i_max)
    if r == -1:
        return -1
    for i in range(9, 0, -1):
        if i_max[i] == r:
            return int(str(i) * r)


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    print(res)


def test():
    assert solve(7, 12) == 888888
    assert solve(9, 12) == 888888888
    assert solve(1, 3) == 9
    assert solve(1000, 25) == -1
    assert solve(30, 1) == 999999999999999999999999999999


if __name__ == "__main__":
    test()
    main()
