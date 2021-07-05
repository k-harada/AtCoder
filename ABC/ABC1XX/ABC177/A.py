def solve(d, t, s):
    if t * s >= d:
        return 'Yes'
    else:
        return 'No'


def main():
    d, t, s = map(int, input().split())
    res = solve(d, t, s)
    print(res)


def test():
    assert solve(1000, 15, 80) == 'Yes'
    assert solve(2000, 20, 100) == 'Yes'
    assert solve(10000, 1, 1) == 'No'


if __name__ == "__main__":
    test()
    main()
