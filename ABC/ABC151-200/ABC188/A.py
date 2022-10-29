def solve(x, y):
    w, z = min(x, y), max(x, y)
    if w + 3 > z:
        return 'Yes'
    else:
        return 'No'


def main():
    x, y = map(int, input().split())
    res = solve(x, y)
    print(res)


def test():
    assert solve(3, 5) == 'Yes'
    assert solve(16, 2) == 'No'
    assert solve(12, 15) == 'No'


if __name__ == "__main__":
    test()
    main()
