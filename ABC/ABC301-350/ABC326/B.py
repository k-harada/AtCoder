def solve(n):
    for x in range(n, 1000):
        xs = str(x)
        a, b, c = int(xs[0]), int(xs[1]), int(xs[2])
        if a * b == c:
            return x
    return -1


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(320) == 326
    assert solve(144) == 144
    assert solve(516) == 600


if __name__ == "__main__":
    test()
    main()
