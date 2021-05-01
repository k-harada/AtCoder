def solve(n, d, h, dh_list):

    res = 0.0
    for d_, h_ in dh_list:
        r = h - (h - h_) * d / (d - d_)
        res = max(res, r)
    # print(res)
    return res


def main():
    n, d, h = map(int, input().split())
    dh_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, d, h, dh_list)
    print(res)


def test():
    assert abs(solve(1, 10, 10, [(3, 5)]) - 2.857142857142857) < 0.001
    assert abs(solve(1, 10, 10, [(3, 2)]) - 0.0) < 0.001
    assert abs(solve(5, 896, 483, [(228, 59), (529, 310), (339, 60), (78, 266), (659, 391)]) - 245.3080684596577) < 0.001


if __name__ == "__main__":
    test()
    main()
