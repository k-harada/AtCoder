def solve(n):
    if n <= 125:
        return 4
    elif n <= 211:
        return 6
    else:
        return 8


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(214) == 8
    assert solve(1) == 4
    assert solve(126) == 6


if __name__ == "__main__":
    test()
    main()
