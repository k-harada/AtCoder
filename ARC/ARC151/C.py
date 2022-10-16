def solve(n, m, xy_list):
    if m == 0:
        if n % 2 == 1:
            return "Takahashi"
        else:
            return "Aoki"
    # 部分ゲームが何個あるかを数える
    res = 0
    for i in range(m - 1):
        v = abs(xy_list[i + 1][1] - xy_list[i][1])
        if v == 0:
            res ^= 1
    # print(first, second)
    d1 = xy_list[0][0] - 1
    d2 = n - xy_list[m - 1][0]

    if d1 <= 1 and d2 <= 1:
        res ^= d1
        res ^= d2
        if res != 0:
            return "Takahashi"
        else:
            return "Aoki"
    elif d1 <= 1 or d2 <= 1:
        return "Takahashi"
    elif abs(d1 - d2) >= 2:
        return "Takahashi"
    elif d1 == d2:
        if res != 0:
            return "Takahashi"
        else:
            return "Aoki"
    else:
        if res == 0:
            return "Takahashi"
        else:
            if max(d1, d2) % 2 == 0:
                return "Takahashi"
            else:
                if res == 0:
                    return "Takahashi"
                else:
                    return "Aoki"


def main():
    n, m = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, xy_list)
    print(res)


def test():
    assert solve(7, 2, [(2, 0), (4, 1)]) == "Takahashi"
    assert solve(3, 3, [(1, 1), (2, 0), (3, 1)]) == "Aoki"
    assert solve(1000000000000000000, 0, []) == "Aoki"


if __name__ == "__main__":
    test()
    main()
