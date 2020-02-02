def solve(x):
    y = x % 100
    ny = y // 5
    if y % 5 != 0:
        ny += 1
    if x // 100 >= ny:
        return 1
    else:
        return 0


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(615) == 1
    assert solve(217) == 0


if __name__ == "__main__":
    test()
    main()
