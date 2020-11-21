def solve(s, p):
    for i in range(1, min(p + 1, 10 ** 6 + 1)):
        if p % i == 0:
            if i + p // i == s:
                return 'Yes'
    return 'No'


def main():
    s, p = map(int, input().split())
    res = solve(s, p)
    print(res)


def test():
    assert solve(3, 2) == 'Yes'
    assert solve(1000000000000, 1) == 'No'
    assert solve(2, 1) == 'Yes'


if __name__ == "__main__":
    test()
    main()
