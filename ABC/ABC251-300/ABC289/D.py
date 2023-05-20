def solve(n, a_list, m, b_list, x):
    dp = [0] * (x + 1)
    dp[0] = 1
    for b in b_list:
        dp[b] = -1
    for i in range(x):
        if dp[i] == 1:
            for a in a_list:
                c = i + a
                if c <= x and dp[c] == 0:
                    dp[c] = 1
    if dp[x] == 1:
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    m = int(input())
    b_list = list(map(int, input().split()))
    x = int(input())
    res = solve(n, a_list, m, b_list, x)
    print(res)


def test():
    assert solve(3, [3, 4, 5], 4, [4, 5, 6, 8], 15) == "Yes"
    assert solve(4, [2, 3, 4, 5], 4, [3, 4, 5, 6], 8) == "No"
    assert solve(4, [2, 5, 7, 8], 5, [2, 9, 10, 11, 19], 20) == "Yes"


if __name__ == "__main__":
    test()
    main()
