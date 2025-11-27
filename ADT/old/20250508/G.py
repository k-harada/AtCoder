def solve(n, s):
    count_row = [0] * n
    count_col = [0] * n
    for i in range(n):
        for j in range(n):
            if s[i][j] == "o":
                count_row[i] += 1
                count_col[j] += 1
    res = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] == "o":
                res += (count_row[i] - 1) * (count_col[j] - 1)
    return res


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    res = solve(n, s)
    print(res)


def test():
    assert solve(3, ["ooo", "oxx", "xxo"]) == 4
    assert solve(4, ["oxxx", "xoxx", "xxox", "xxxo"]) == 0
    assert solve(15, [
        "xooxxooooxxxoox",
        "oxxoxoxxxoxoxxo",
        "oxxoxoxxxoxoxxx",
        "ooooxooooxxoxxx",
        "oxxoxoxxxoxoxxx",
        "oxxoxoxxxoxoxxo",
        "oxxoxooooxxxoox",
        "xxxxxxxxxxxxxxx",
        "xooxxxooxxxooox",
        "oxxoxoxxoxoxxxo",
        "xxxoxxxxoxoxxoo",
        "xooxxxooxxoxoxo",
        "xxxoxxxxoxooxxo",
        "oxxoxoxxoxoxxxo",
        "xooxxxooxxxooox"
    ]) == 2960


if __name__ == "__main__":
    test()
    main()
