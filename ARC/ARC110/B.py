def solve(n, t):

    if n == 1:
        if t[0] == "1":
            return 20000000000
        else:
            return 10000000000

    # start
    if t[0] == "1":
        if t[1] == "1":
            start = 0
        else:
            start = 1
    else:
        start = 2

    # check if valid
    for i in range(n):
        if (i + start) % 3 == 2:
            if t[i] != "0":
                return 0
        else:
            if t[i] != "1":
                return 0

    # count 0
    count_0 = (n + start) // 3
    if t[-1] == '0':
        return 10000000000 - count_0 + 1
    else:
        return 10000000000 - count_0


def main():
    n = int(input())
    t = input()
    res = solve(n, t)
    print(res)


def test():
    assert solve(4, '1011') == 9999999999
    assert solve(22, '1011011011011011011011') == 9999999993
    assert solve(1, '1') == 20000000000
    assert solve(1, '0') == 10000000000
    assert solve(2, '11') == 10000000000
    assert solve(3, '110') == 10000000000


if __name__ == "__main__":
    test()
    main()
