def solve(n):
    k = 0
    s = 0
    while s < n:
        k += 1
        s += k
    return k


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(12) == 5
    assert solve(100128) == 447


if __name__ == "__main__":
    test()
    main()
