def solve(n, s):
    res = ""
    for i in range(n):
        res += s[i] * 2
    return res


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(8, "beginner") == "bbeeggiinnnneerr"
    assert solve(3, "aaa") == "aaaaaa"


if __name__ == "__main__":
    test()
    main()
