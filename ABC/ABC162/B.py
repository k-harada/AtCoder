def solve(n):
    res = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        else:
            res += i
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(15) == 60
    assert solve(1000000) == 266666333332


if __name__ == "__main__":
    test()
    main()
