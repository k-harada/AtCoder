def solve(x, y, a, b):
    res = 0
    z = x
    while True:
        if (a - 1) * z >= b:
            # gym
            res += (y - z - 1) // b
            break
        else:
            z *= a
        if z >= y:
            break
        res += 1
    return res


def main():
    x, y, a, b = map(int, input().split())
    res = solve(x, y, a, b)
    print(res)


def test():
    assert solve(4, 20, 2, 10) == 2
    assert solve(1, 1000000000000000000, 10, 1000000000) == 1000000007


if __name__ == "__main__":
    test()
    main()
