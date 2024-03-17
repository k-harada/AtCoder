def solve(x):
    q, r = x // 10, x % 10
    if r == 0:
        return q
    else:
        return q + 1


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(27) == 3
    assert solve(-13) == -1
    assert solve(40) == 4
    assert solve(-20) == -2
    assert solve(123456789123456789) == 12345678912345679


if __name__ == "__main__":
    test()
    main()
