def solve(b):
    for i in range(1, 18):
        if pow(i, i) == b:
            return i
    return -1


def main():
    b = int(input())
    res = solve(b)
    print(res)


def test():
    assert solve(27) == 3
    assert solve(100) == -1
    assert solve(10000000000) == 10


if __name__ == "__main__":
    test()
    main()
