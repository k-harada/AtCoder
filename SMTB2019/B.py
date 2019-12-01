def solve(n):
    for i in range(n + 1):
        if int(i * 1.08) == n:
            return i
    return ":("


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(432) == 400
    assert solve(1079) == ":("
    assert solve(1001) == 927


if __name__ == "__main__":
    test()
    main()
