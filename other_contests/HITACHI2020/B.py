def solve(a, b, m, a_list, b_list, xyc_list):
    res = min(a_list) + min(b_list)
    for x, y, c in xyc_list:
        r = a_list[x - 1] + b_list[y - 1] - c
        res = min(res, r)
    return res


def main():
    a, b, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    xyc_list = [list(map(int, input().split())) for _ in range(m)]
    res = solve(a, b, m, a_list, b_list, xyc_list)
    print(res)


def test():
    assert solve(2, 3, 1, [3, 3], [3, 3, 3], [[1, 2, 1]]) == 5
    assert solve(1, 1, 2, [10], [10], [[1, 1, 5], [1, 1, 10]]) == 10
    assert solve(2, 2, 1, [3, 5], [3, 5], [[2, 2, 2]]) == 6


if __name__ == "__main__":
    test()
    main()
