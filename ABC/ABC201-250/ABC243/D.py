def solve(n, x, s):
    lr_list = []
    d_minus = 0
    res = x

    for i in range(n):
        if s[i] == "L":
            lr_list.append(0)
        elif s[i] == "R":
            lr_list.append(1)
        else:
            if len(lr_list) > 0:
                _ = lr_list.pop()
            else:
                d_minus += 1

    for _ in range(d_minus):
        res = res // 2

    for c in lr_list:
        res = res * 2 + c

    return res


def main():
    n, x = map(int, input().split())
    s = input()
    res = solve(n, x, s)
    print(res)


def test():
    assert solve(3, 2, "URL") == 6
    assert solve(4, 500000000000000000, "RRUU") == 500000000000000000
    assert solve(30, 123456789, "LRULURLURLULULRURRLRULRRRUURRU") == 126419752371


if __name__ == "__main__":
    test()
    main()
