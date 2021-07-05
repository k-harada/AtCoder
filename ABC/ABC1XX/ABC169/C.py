def solve(a, b):
    a_int = int(a)
    b_int = 0
    c = 0
    for i in range(len(b)):
        if b[- i - 1] == ".":
            continue
        b_int += int(b[- i - 1]) * (10 ** c)
        c += 1
    # print(a_int, b_int, a_int * b_int // 100)
    return a_int * b_int // 100


def main():
    a, b = input().split()
    res = solve(a, b)
    print(res)


def test():
    assert solve("198", "1.10") == 217
    assert solve("1", "0.01") == 0
    assert solve("1000000000000000", "09.99") == 9990000000000000


if __name__ == "__main__":
    test()
    main()
