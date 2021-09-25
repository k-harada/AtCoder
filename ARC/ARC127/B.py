def roll_1(s):
    r = ""
    for c in s:
        if c == "0":
            r += "1"
        elif c == "1":
            r += "2"
        else:
            r += "0"
    return r


def solve(n, l):
    res_0 = []
    three = [0] * (3 ** 11)
    three[1] = 1
    three[2] = 2

    for m in range(1, 11):
        for i in range(3 ** m, 2 * 3 ** m):
            three[i] = 10 ** m + three[i - 3 ** m]
        for i in range(2 * 3 ** m, 3 * 3 ** m):
            three[i] = 2 * 10 ** m + three[i - 2 * 3 ** m]

    for i in range(n):
        res_0.append(str(2 * 10 ** (l - 1) + three[i]))
    res_1 = [roll_1(r) for r in res_0]
    res_2 = [roll_1(r) for r in res_1]
    res = res_0 + res_1 + res_2
    # print(res)
    return res


def main():
    n, l = map(int, input().split())
    res = solve(n, l)
    for r in res:
        print(r)


def test():
    assert solve(2, 2) == ['20', '21', '01', '02', '12', '10']


if __name__ == "__main__":
    test()
    main()
