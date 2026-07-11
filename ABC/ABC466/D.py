def solve(n, m, rc_list):
    res = 0

    r_list = [0] * (n + 1)
    c_list = [0] * (n + 1)

    for r, c in reversed(rc_list):
        if r_list[r] == c_list[c] == 0:
            res += 1
        r_list[r] = 1
        c_list[c] = 1

    return res


def main():
    n, m = map(int, input().split())
    rc_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, rc_list)
    print(res)


def test():
    assert solve(3, 6, [(1, 1), (1, 2), (3, 3), (3, 2), (1, 3), (1, 3)]) == 2
    assert solve(2, 3, [(1, 2), (2, 1), (1, 1)]) == 1


if __name__ == "__main__":
    test()
    main()
