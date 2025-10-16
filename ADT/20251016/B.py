def solve(n, d, t_list):
    res = -1
    for i in range(n - 1):
        if t_list[i + 1] - t_list[i] <= d:
            res = t_list[i + 1]
            break
    return res


def main():
    n, d = map(int, input().split())
    t_list = list(map(int, input().split()))
    res = solve(n, d, t_list)
    print(res)


def test():
    assert solve(4, 500, [300, 900, 1300, 1700]) == 1300
    assert solve(5, 99, [100, 200, 300, 400, 500]) == -1
    assert solve(4, 500, [100, 600, 1100, 1600]) == 600


if __name__ == "__main__":
    test()
    main()
