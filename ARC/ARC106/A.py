def solve(n):
    list_3 = []

    x3 = 3
    while x3 < n:
        list_3.append(x3)
        x3 *= 3
    list_5 = []

    x5 = 5
    while x5 < n:
        list_5.append(x5)
        x5 *= 5

    for i3, x3 in enumerate(list_3):
        for i5, x5 in enumerate(list_5):
            if x3 + x5 == n:
                return f'{i3 + 1} {i5 + 1}'
    return '-1'


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(106) == '4 2'
    assert solve(1024) == '-1'
    assert solve(10460353208) == '21 1'


if __name__ == "__main__":
    test()
    main()
