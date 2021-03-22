def solve(n, m, ab_list, s):
    pn_list_rev = []
    left = 0
    right = len(s)
    while True:
        if s[left] == "g":
            if s[right - 1] == "w":
                pn_list_rev.append("n")
                start = int(s[left + 5:right - 1])
            else:
                pn_list_rev.append("p")
                start = int(s[left + 5:right])
            break
        left += 1
        if s[right - 1] == "w":
            right -= 3
            pn_list_rev.append("n")
        else:
            right -= 1
            pn_list_rev.append("p")
    pn_list = list(reversed(pn_list_rev))
    # print(start, pn_list)

    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][start] = 1

    for i, pn in enumerate(pn_list):
        d = [0] * (n + 1)
        for a, b in ab_list:
            if dp[i % 2][b] == 1:
                d[a] += 1
        if pn == "n":
            for j in range(1, n + 1):
                if d[j] > 0:
                    dp[(i + 1) % 2][j] = 1
                else:
                    dp[(i + 1) % 2][j] = 0
        else:
            c = sum(dp[i % 2])
            for j in range(1, n + 1):
                if d[j] < c:
                    dp[(i + 1) % 2][j] = 1
                else:
                    dp[(i + 1) % 2][j] = 0
    return sum(dp[len(pn_list) % 2])


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    s = input()
    res = solve(n, m, ab_list, s)
    print(res)


def test():
    assert solve(3, 6, [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)], '"group1w"ww') == 3
    assert solve(3, 2, [(1, 2), (2, 3)], '"group3w"') == 2
    assert solve(3, 1, [(1, 1)], '""group1w"ww"ww') == 1


if __name__ == "__main__":
    test()
    main()
