def solve(s, t):
    if s == t:
        return 'same'
    elif s.lower() == t.lower():
        return 'case-insensitive'
    else:
        return 'different'


def main():
    s = input()
    t = input()
    res = solve(s, t)
    print(res)


def test():
    assert solve('AbC', 'ABC') == 'case-insensitive'
    assert solve('xyz', 'xyz') == 'same'
    assert solve('aDs', 'kjH') == 'different'


if __name__ == "__main__":
    test()
    main()
