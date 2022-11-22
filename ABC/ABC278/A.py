def solve(n, k, a_list):
    if k >= n:
        return [0] * n
    else:
        return a_list[k:] + [0] * k


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(" ".join([str(r) for r in res]))


def test():
    assert solve(3, 2, [2, 7, 8]) == [8, 0, 0]
    assert solve(3, 4, [9, 9, 9]) == [0, 0, 0]
    assert solve(9, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [6, 7, 8, 9, 0, 0, 0, 0, 0]


if __name__ == "__main__":
    test()
    main()
