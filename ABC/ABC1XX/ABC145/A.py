def solve(r):
    return r * r


def main():
    r = int(input())
    res = solve(r)
    print(res)


def test():
    assert solve(2) == 4
    assert solve(100) == 10000


if __name__ == "__main__":
    main()
