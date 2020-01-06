def solve(a, b, k):
    if a >= k:
        res_a = a - k
        res_b = b
    elif a + b >= k:
        res_a = 0
        res_b = a + b - k
    else:
        res_a = 0
        res_b = 0
    return "{} {}".format(res_a, res_b)


def main():
    a, b, k = map(int, input().split())
    res = solve(a, b, k)
    print(res)


def test():
    assert solve(2, 3, 3) == "0 2"
    assert solve(500000000000, 500000000000, 1000000000000) == "0 0"


if __name__ == "__main__":
    test()
    main()
