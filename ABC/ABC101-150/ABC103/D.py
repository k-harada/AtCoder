def solve(n, m, ab_list):
    forbidden = [n + 1] * (n + 1)
    for a, b in ab_list:
        forbidden[a] = min(forbidden[a], b)
    forbidden_min = n + 1
    res = 0
    for i in range(n + 1):
        if i == forbidden_min:
            res += 1
            forbidden_min = n + 1
        forbidden_min = min(forbidden_min, forbidden[i])
    return res


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(5, 2, [(1, 4), (2, 5)]) == 1
    assert solve(9, 5, [(1, 8), (2, 7), (3, 5), (4, 6), (7, 9)]) == 2
    assert solve(5, 10, [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]) == 4


if __name__ == "__main__":
    test()
    main()
