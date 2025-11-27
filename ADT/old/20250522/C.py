def solve(s):
    if len(s) % 2 == 1:
        return "No"
    m = len(s) // 2
    for i in range(m):
        if s[2 * i] != s[2 * i + 1]:
            return "No"
    odd_set = set(s[::2])
    if len(odd_set) < m:
        return "No"
    return "Yes"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("aabbcc") == "Yes"
    assert solve("aab") == "No"
    assert solve("zzzzzz") == "No"


if __name__ == "__main__":
    test()
    main()
