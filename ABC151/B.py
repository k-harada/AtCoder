def solve(n, k, m, a_list):
    res = n * m - sum(a_list)
    if res < 0:
        return 0
    elif res > k:
        return -1
    else:
        return res


def main():
    n, k, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, m, a_list)
    print(res)


def test():
    assert solve(5, 10, 7, [8, 10, 3, 6]) == 8
    assert solve(4, 100, 60, [100, 100, 100]) == 0
    assert solve(4, 100, 60, [0, 0, 0]) == -1


if __name__ == "__main__":
    test()
    main()
