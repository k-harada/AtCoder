def solve(n, k, h_list):
    h_list_s = list(sorted(h_list))
    res = 10 ** 9
    for i in range(n - (k - 1)):
        r = h_list_s[i + k - 1] - h_list_s[i]
        res = min(r, res)
    return res


def main():
    n, k = map(int, input().split())
    h_list = [int(input()) for _ in range(n)]
    res = solve(n, k, h_list)
    print(res)


def test():
    assert solve(5, 3, [10, 15, 11, 14, 12]) == 2
    assert solve(5, 3, [5, 7, 5, 7, 7]) == 0


if __name__ == "__main__":
    test()
    main()
