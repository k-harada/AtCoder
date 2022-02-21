def solve(n, c_list):
    for i in range(2 ** n):
        pass
    return 0


def main():
    n = int(input())
    c_list = list(map(int, input().split()))
    res = solve(n, c_list)
    print(res)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
