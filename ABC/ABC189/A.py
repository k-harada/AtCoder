def solve(s):
    if s[0] == s[1] and s[0] == s[2]:
        return 'Won'
    else:
        return 'Lost'


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve('SSS') == 'Won'
    assert solve('WVW') == 'Lost'


if __name__ == "__main__":
    test()
    main()
