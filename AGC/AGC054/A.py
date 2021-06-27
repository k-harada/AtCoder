def solve(n, s):
    if s[0] != s[-1]:
        return 1
    for i in range(n - 1):
        if s[i] != s[0] and s[i + 1] != s[0]:
            return 2
    return -1


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(4, "abba") == 2
    assert solve(3, "aba") == -1


if __name__ == "__main__":
    test()
    main()
