def solve_sub_123(s):
    if s == "0":
        return 0
    r = 1
    for i, c in enumerate(s):
        if r == 1:
            if c in ["1", "2", "3"]:
                r = 1
            elif c in ["4", "5", "6"]:
                r = 2
            elif c in ["7", "8", "9"]:
                r = 3
            else:
                return -1
        elif r == 2:
            if c in ["2", "3", "4", "5", "6"]:
                r = 2
            elif c in ["7", "8", "9"]:
                r = 3
            else:
                return -1
        elif r == 3:
            if c in ["0", "1", "2"]:
                return -1
            else:
                r = 3
    return r


def solve_sub(s):

    sol_123 = solve_sub_123(s)
    if sol_123 >= 0:
        return sol_123

    r = 0
    dp = [[0] * 2 for _ in range(len(s) + 1)]
    dp[0][0] = 1
    dp[0][1] = 0

    for i, c in enumerate(s):
        r *= 10
        r += int(c)
        r0 = solve_sub_123(str(r))
        r1 = solve_sub_123(str(r - 1))
        if r0 >= 0:
            dp[i + 1][0] = 1
        elif dp[i][0] == 1 and c in ["4", "5", "6", "7", "8", "9"]:
            dp[i + 1][0] = 1
        elif dp[i][1] == 1 and c in ["0", "1", "2"]:
            dp[i + 1][0] = 1
        if r1 >= 0:
            dp[i + 1][1] = 1
        elif dp[i][0] == 1 and c in ["5", "6", "7", "8", "9"]:
            dp[i + 1][1] = 1
        elif dp[i][1] == 1 and c in ["1", "2", "3"]:
            dp[i + 1][1] = 1
        elif dp[i][1] == 1 and c == "0":
            dp[i + 1][0] = 1
            dp[i + 1][1] = 1

    if dp[-1][0] == 1:
        return 4
    else:
        return 5


def solve(t, n_list):
    res = []
    for s in n_list:
        res.append(solve_sub(s))
    # print(res)
    return res


def main():
    t = int(input())
    n_list = [input() for _ in range(t)]
    res = solve(t, n_list)
    for r in res:
        print(r)


def test():
    assert solve(5, ["456", "10000", "123", "314", "91"]) == [2, 4, 1, 2, 4]
    # res = solve(100, [str(x) for x in range(1, 101)])
    # for i in range(100):
    #     print(i + 1, res[i])


if __name__ == "__main__":
    test()
    main()
