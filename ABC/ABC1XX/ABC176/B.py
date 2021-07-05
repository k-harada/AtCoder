def solve(ns):
    d = 0
    for s in ns:
        d += int(s)
        d %= 9
    if d == 0:
        return 'Yes'
    else:
        return 'No'


def main():
    ns = input()
    res = solve(ns)
    print(res)


def test():
    assert solve("123456789") == 'Yes'
    assert solve("0") == 'Yes'
    assert solve("31415926535897932384626433832795028841971693993751058209749445923078164062862089986280") == 'No'


if __name__ == "__main__":
    test()
    main()
