def solve(s):
    n = len(s)
    left_a = 0
    right_a = 0
    for i in range(n):
        if s[i] == "a":
            left_a += 1
        else:
            break
    for i in range(n - 1, -1, -1):
        if s[i] == "a":
            right_a += 1
        else:
            break
    # ALL a
    if left_a == n:
        return "Yes"
    if left_a > right_a:
        return "No"
    t = ["a"] * (right_a - left_a) + list(s)
    m = len(t)
    for i in range(m):
        if t[i] != t[m - 1 - i]:
            return "No"
    return "Yes"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("kasaka") == "Yes"
    assert solve("atcoder") == "No"
    assert solve("php") == "Yes"


if __name__ == "__main__":
    test()
    main()
