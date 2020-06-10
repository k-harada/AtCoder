def solve(n, a_list):
    res = 1
    if 0 in a_list:
        return 0
    for i in range(n):
        res *= a_list[i]
        if res > 10 ** 18:
            return -1
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(2, [1000000000, 1000000000]) == 1000000000000000000
    assert solve(3, [101, 9901, 999999000001]) == -1
    assert solve(31, [4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0]) == 0


if __name__ == "__main__":
    test()
    main()
