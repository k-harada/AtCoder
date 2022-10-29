def solve(n, s):
    if n % 2 == 1:
        return "No"
    m = n // 2
    for i in range(m):
        if s[i] != s[m + i]:
            return "No"
    return "Yes"


def main():
    n = int(input())
    s = list(input())
    res = solve(n, s)
    print(res)


def test():
    assert solve(6, "abcabc") == "Yes"
    assert solve(6, "abcadc") == "No"
    assert solve(1, "z") == "No"


if __name__ == "__main__":
    test()
    main()
