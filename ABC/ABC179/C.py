def solve(n):
    res = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j >= n:
                break
            res += 1
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(3) == 3
    assert solve(100) == 473
    # assert solve(1000000) == 13969985


if __name__ == "__main__":
    test()
    main()
