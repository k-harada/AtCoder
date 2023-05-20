def solve(n, m, a_list, b_list):
    res = 0
    for b in b_list:
        res += a_list[b - 1]
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list)
    print(res)


def test():
    assert solve(3, 2, [10, 20, 30], [1, 3]) == 40
    assert solve(4, 1, [1, 1, 1, 100], [4]) == 100
    assert solve(8, 4, [22, 75, 26, 45, 72, 81, 47, 29], [4, 6, 7, 8]) == 202


if __name__ == "__main__":
    test()
    main()
