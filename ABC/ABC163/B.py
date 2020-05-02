def solve(n, m, a_list):
    res = n - sum(a_list)
    if res >= 0:
        return res
    else:
        return -1


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(41, 2, [5, 6]) == 30
    assert solve(10, 2, [5, 6]) == -1
    assert solve(11, 2, [5, 6]) == 0
    assert solve(314, 15, [9, 26, 5, 35, 8, 9, 79, 3, 23, 8, 46, 2, 6, 43, 3]) == 9


if __name__ == "__main__":
    test()
    main()
