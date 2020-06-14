def solve(x, n, p_list):
    diff_min = 101
    res = 0
    for i in range(102):
        if i not in p_list:
            if abs(x - i) < diff_min:
                diff_min = abs(x - i)
                res = i
    return res


def main():
    x, n = map(int, input().split())
    p_list = list(map(int, input().split()))
    res = solve(x, n, p_list)
    print(res)


def test():
    assert solve(6, 5, [4, 7, 10, 6, 5]) == 8
    assert solve(10, 5, [4, 7, 10, 6, 5]) == 9
    assert solve(100, 0, []) == 100


if __name__ == "__main__":
    test()
    main()
