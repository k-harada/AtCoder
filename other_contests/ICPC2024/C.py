def solve(x, y):
    if x * y < 0:
        res = max(abs(x), abs(y))
    else:
        res = abs(x) + abs(y)
    return res


def main():
    n = int(input())
    res = []
    for _ in range(n):
        x, y = map(int, input().split())
        res.append(solve(x, y))
    for r in res:
        print(r)


def test():
    assert solve(0, 0) == 0
    assert solve(0, 1) == 1
    assert solve(1, 0) == 1
    assert solve(2, 1) == 3
    assert solve(2, -1) == 2
    assert solve(-3, 2) == 3
    assert solve(-1, -3) == 4


if __name__ == "__main__":
    test()
    main()
