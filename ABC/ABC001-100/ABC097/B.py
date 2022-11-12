def solve(x):
    res = 1
    for p in range(2, 10):
        for b in range(2, x + 1):
            r = pow(b, p)
            if r <= x:
                res = max(res, r)
            if r > x:
                break
    return res


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(10) == 9
    assert solve(1) == 1
    assert solve(999) == 961


if __name__ == "__main__":
    test()
    main()
