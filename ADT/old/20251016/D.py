def solve(n):
    res = -1
    for i in range(n, 1000):
        p = i // 100
        q = (i % 100) // 10
        r = i % 10
        if p * q == r:
            res = i
            break
    return res


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
