def solve(n, ab_list):
    # 全部燃えるのに何秒か
    t_all = 0.0
    for a, b in ab_list:
        t_all += a / b
    t_half = t_all / 2
    res = 0.0
    t_now = 0.0
    for a, b in ab_list:
        t_add = a / b
        if t_now + t_add < t_half:
            t_now += t_add
            res += a
        else:
            res += b * (t_half - t_now)
            break
    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert abs(solve(3, [(1, 1), (2, 1), (3, 1)]) - 3.0) < 0.0000001
    assert abs(solve(3, [(1, 3), (2, 2), (3, 1)]) - 3.833333333) < 0.0000001
    assert abs(solve(5, [(3, 9), (1, 2), (4, 6), (1, 5), (5, 3)]) - 8.916666666666) < 0.0000001


if __name__ == "__main__":
    test()
    main()
