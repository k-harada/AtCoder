def solve(k, a, b):
    for i in range(a, b + 1):
        if i % k == 0:
            return "OK"
    return "NG"


def main():
    k = int(input())
    a, b = map(int, input().split())
    res = solve(k, a, b)
    print(res)


def test():
    assert solve(7, 500, 600) == "OK"
    assert solve(4, 5, 7) == "NG"
    assert solve(1, 11, 11) == "OK"


if __name__ == "__main__":
    test()
    main()
