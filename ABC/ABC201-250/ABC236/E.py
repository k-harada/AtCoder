def solve(n, a_list):
    res = []
    return res


def main():
    n = int(input())
    a_list = map(int, input().split())
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(6, [2, 1, 2, 1, 1, 10]) == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
