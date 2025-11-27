def solve_sub(t, h):
    q = h // 5
    r = h % 5
    s = 3 * q
    if t % 3 == 0:
        if r <= 2:
            s += r
        else:
            s += 3
    elif t % 3 == 1:
        if r <= 1:
            s += r
        elif r <= 4:
            s += 2
        else:
            s += 3
    else:
        if r == 0:
            s += 0
        elif r <= 3:
            s += 1
        elif r <= 4:
            s += 2
        else:
            s += 3
    # print(t, s, h)
    return t + s


def solve(n, h_list):
    t = 0
    for h in h_list:
        t = solve_sub(t, h)
    return t


def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    res = solve(n, h_list)
    print(res)


def test():
    assert solve(3, [6, 2, 2]) == 8
    assert solve(9, [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]) == 82304529
    assert solve(5, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 3000000000


def test_sub():
    assert solve_sub(0, 1) == 1
    assert solve_sub(0, 2) == 2
    assert solve_sub(0, 3) == 3
    assert solve_sub(0, 4) == 3
    assert solve_sub(0, 5) == 3
    assert solve_sub(1, 1) == 2
    assert solve_sub(1, 2) == 3
    assert solve_sub(1, 3) == 3
    assert solve_sub(1, 4) == 3
    assert solve_sub(1, 5) == 4
    assert solve_sub(2, 1) == 3
    assert solve_sub(2, 2) == 3
    assert solve_sub(2, 3) == 3
    assert solve_sub(2, 4) == 4
    assert solve_sub(2, 5) == 5


if __name__ == "__main__":
    test_sub()
    test()
    main()
