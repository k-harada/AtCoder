def solve(a, b, c):
    if c == 0:
        if b >= a:
            return 'Aoki'
        else:
            return 'Takahashi'
    else:
        if a >= b:
            return 'Takahashi'
        else:
            return 'Aoki'


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(2, 1, 0) == 'Takahashi'
    assert solve(2, 2, 0) == 'Aoki'
    assert solve(2, 2, 1) == 'Takahashi'


if __name__ == "__main__":
    test()
    main()
