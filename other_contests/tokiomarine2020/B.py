def solve(a, v, b, w, t):
    if v <= w:
        return "NO"
    if abs(b - a) <= t * (v - w):
        return "YES"
    else:
        return "NO"


def main():
    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input())
    res = solve(a, v, b, w, t)
    print(res)


def test():
    assert solve(1, 2, 3, 1, 3) == "YES"
    assert solve(1, 2, 3, 2, 3) == "NO"
    assert solve(1, 2, 3, 3, 3) == "NO"


if __name__ == "__main__":
    test()
    main()
