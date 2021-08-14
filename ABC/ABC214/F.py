LARGE = 10 ** 9 + 7
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def solve(s):
    n = len(s)
    dp = [0] * (n + 2)
    dp[0] = 1
    dp[1] = 0
    cum_sum = [0, 1, 1]
    position = dict()
    for c in ALPHABET:
        position[c] = -1
    for _i, c in enumerate(s):
        i = _i + 1
        left = position[c] - 1
        # print(i, left)
        dp[i + 1] = (cum_sum[i - 2 + 3] - cum_sum[left - 1 + 3]) % LARGE
        cum_sum.append((cum_sum[-1] + dp[i]) % LARGE)
        position[c] = i
    # print(dp)
    # print(cum_sum)
    return sum(dp[2:]) % LARGE


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("abc") == 4
    assert solve("aa") == 1
    assert solve("abca") == 6
    assert solve("chokudai") == 54


if __name__ == "__main__":
    test()
    main()
