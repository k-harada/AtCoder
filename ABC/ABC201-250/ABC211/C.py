LARGE = 10 ** 9 + 7


def solve(s):
    dp = dict()
    dp["start"] = 1
    for c in "chokudai":
        dp[c] = 0

    for c in s:
        if c == "c":
            dp["c"] = (dp["c"] + dp["start"]) % LARGE
        elif c == "h":
            dp["h"] = (dp["h"] + dp["c"]) % LARGE
        elif c == "o":
            dp["o"] = (dp["o"] + dp["h"]) % LARGE
        elif c == "k":
            dp["k"] = (dp["k"] + dp["o"]) % LARGE
        elif c == "u":
            dp["u"] = (dp["u"] + dp["k"]) % LARGE
        elif c == "d":
            dp["d"] = (dp["d"] + dp["u"]) % LARGE
        elif c == "a":
            dp["a"] = (dp["a"] + dp["d"]) % LARGE
        elif c == "i":
            dp["i"] = (dp["i"] + dp["a"]) % LARGE
    return dp["i"]


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("chchokudai") == 3
    assert solve("atcoderrr") == 0
    assert solve("chokudaichokudaichokudai") == 45


if __name__ == "__main__":
    test()
    main()
