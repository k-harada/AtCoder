def solve(n, x_list):
    x_list_s = list(sorted(x_list))
    res = sum(x_list_s[n:-n]) / (3 * n)
    return res


def main():
    n = int(input())
    x_list = list(map(int, input().split()))
    res = solve(n, x_list)
    print(res)


def test():
    assert solve(1, [10, 100, 20, 50, 30]) == 100 / 3
    assert solve(2, [3, 3, 3, 4, 5, 6, 7, 8, 99, 100]) == 5.5


if __name__ == "__main__":
    # test()
    main()
