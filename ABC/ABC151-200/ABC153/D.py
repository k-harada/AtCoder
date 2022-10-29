def solve(h):
    if h == 1:
        return 1
    else:
        return 2 * solve(h // 2) + 1


def main():
    h = int(input())
    res = solve(h)
    print(res)


def test():
    assert solve(2) == 3
    assert solve(4) == 7
    assert solve(1000000000000) == 1099511627775


if __name__ == "__main__":
    test()
    main()
