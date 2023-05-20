def solve(n, t, c_list, r_list):
    if t in c_list:
        s = t
    else:
        s = c_list[0]
    w = 0
    r = 0
    for i in range(n):
        if c_list[i] == s and r_list[i] > r:
            w = i + 1
            r = r_list[i]
    return w


def main():
    n, t = map(int, input().split())
    c_list = list(map(int, input().split()))
    r_list = list(map(int, input().split()))
    res = solve(n, t, c_list, r_list)
    print(res)


def test():
    assert solve(4, 2, [1, 2, 1, 2], [6, 3, 4, 5]) == 4
    assert solve(4, 2, [1, 3, 1, 4], [6, 3, 4, 5]) == 1
    assert solve(2, 1000000000, [1000000000, 1], [1, 1000000000]) == 1


if __name__ == "__main__":
    test()
    main()
