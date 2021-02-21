def solve(s):
    res = 0
    temp = "."
    weight = 0
    for i in range(2, len(s)):
        if s[i - 2] == s[i - 1] != s[i] and s[i - 2] != temp:
            temp = s[i - 2]
            weight += 1
        if s[i] != temp:
            res += weight
        else:
            res += weight - 1
    # print(res)
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("accept") == 3
    assert solve("atcoder") == 0
    assert solve("anerroroccurred") == 16


if __name__ == "__main__":
    test()
    main()
