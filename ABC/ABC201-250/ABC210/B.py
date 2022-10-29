def solve(n, s):
    for i, c in enumerate(s):
        if c == "1":
            if i % 2 == 0:
                return "Takahashi"
            else:
                return "Aoki"
    return "FALSE"


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(5, "00101") == "Takahashi"
    assert solve(3, "010") == "Aoki"


if __name__ == "__main__":
    test()
    main()
