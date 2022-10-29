def solve(a, b):
    for i in range(1, 1001):
        res_a = int(i * 0.08)
        res_b = int(i * 0.10)
        if res_a == a and res_b == b:
            return i
    return -1


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(2, 2) == 25
    assert solve(8, 10) == 100
    assert solve(19, 99) == -1


if __name__ == "__main__":
    test()
    main()
