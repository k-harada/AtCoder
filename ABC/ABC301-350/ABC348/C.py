def solve(n, ac_list):
    col_dict = dict()
    for a, c in ac_list:
        if c not in col_dict.keys():
            col_dict[c] = a
        else:
            col_dict[c] = min(col_dict[c], a)
    res = max(col_dict.values())
    return res


def main():
    n = int(input())
    ac_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ac_list)
    print(res)


def test():
    assert solve(4, [(100, 1), (20, 5), (30, 5), (40, 1)]) == 40
    assert solve(10, [
        (68, 3),
        (17, 2),
        (99, 2),
        (92, 4),
        (82, 4),
        (10, 3),
        (100, 2),
        (78, 1),
        (3, 1),
        (35, 4),
    ]) == 35


if __name__ == "__main__":
    test()
    main()
