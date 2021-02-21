def solve(a, b, c):
    d = a % 10
    e = pow(b, c, 4)
    if e == 0:
        e = 4
    return pow(d, e, 10)


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(4, 3, 2) == 4
    assert solve(1, 2, 3) == 1
    assert solve(3141592, 6535897, 9323846) == 2


if __name__ == "__main__":
    test()
    main()
