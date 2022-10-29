def solve(n, x, y):
    res_list = [0] * n
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = min(j - i, abs(i - x + 1) + abs(j - y + 1) + 1)
            res_list[d] += 1
    # print(res_list)
    return res_list[1:]


def main():
    n, x, y = map(int, input().split())
    res_list = solve(n, x, y)
    for res in res_list:
        print(res)


def test():
    assert solve(5, 2, 4) == [5, 4, 1, 0]
    assert solve(3, 1, 3) == [3, 0]
    assert solve(7, 3, 7) == [7, 8, 4, 2, 0, 0]


if __name__ == "__main__":
    test()
    main()
