def solve(n):
    res = []
    for i in range(n + 1):
        r = 10
        for j in range(1, 10):
            if n % j == 0:
                if i % (n // j) == 0:
                    r = min(r, j)
        if r == 10:
            res.append("-")
        else:
            res.append(str(r))
    return "".join(res)


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(12) == "1-643-2-346-1"
    assert solve(7) == "17777771"
    assert solve(1) == "11"


if __name__ == "__main__":
    test()
    main()
