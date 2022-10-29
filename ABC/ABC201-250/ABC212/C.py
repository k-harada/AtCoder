def solve(n, m, a_list, b_list):
    a_list_s = list(sorted(a_list))
    b_list_s = list(sorted(b_list))
    res = 10 ** 9 + 7
    i = 0
    j = 0
    while i < n and j < m:
        d = a_list_s[i] - b_list_s[j]
        res = min(res, abs(d))
        if d >= 0:
            j += 1
        else:
            i += 1
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list)
    print(res)


def test():
    assert solve(2, 2, [1, 6], [4, 9]) == 2
    assert solve(1, 1, [10], [10]) == 0
    assert solve(6, 8, [82, 76, 82, 82, 71, 70], [17, 39, 67, 2, 45, 35, 22, 24]) == 3


if __name__ == "__main__":
    test()
    main()
