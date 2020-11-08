def solve(n, a_list):

    a_list_cum_sum = [0] * n
    s = 0
    for i, a in enumerate(a_list):
        s += a
        a_list_cum_sum[i] = s

    x = 0
    max_v = 0
    res = 0
    for i, v in enumerate(a_list_cum_sum):
        max_v = max(v, max_v)
        res = max(res, x + max_v)
        x += v
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [2, -1, -2]) == 5
    assert solve(5, [-2, 1, 3, -1, -1]) == 2
    assert solve(5, [-1000, -1000, -1000, -1000, -1000]) == 0


if __name__ == "__main__":
    test()
    main()
