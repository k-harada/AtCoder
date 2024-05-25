def solve(n, m, ab_list):
    count = [1] * n
    for a, b in ab_list:
        count[b - 1] = 0
    if sum(count) > 1:
        return -1
    else:
        for i in range(n):
            if count[i] == 1:
                return i + 1
    return 0


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(3, 2, [(1, 2), (2, 3)]) == 1
    assert solve(3, 2, [(1, 3), (2, 3)]) == -1
    assert solve(6, 6, [(1, 6), (6, 5), (6, 2), (2, 3), (4, 3), (4, 2)]) == -1


if __name__ == "__main__":
    test()
    main()
