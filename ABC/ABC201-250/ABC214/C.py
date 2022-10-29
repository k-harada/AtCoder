def solve(n, s_list, t_list):
    res = t_list.copy()
    for i in range(n):
        res[(i + 1) % n] = min(res[i] + s_list[i], res[(i + 1) % n])
    for i in range(n):
        res[(i + 1) % n] = min(res[i] + s_list[i], res[(i + 1) % n])
    return res


def main():
    n = int(input())
    s_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))
    res = solve(n, s_list, t_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [4, 1, 5], [3, 10, 100]) == [3, 7, 8]
    assert solve(4, [100, 100, 100, 100], [1, 1, 1, 1]) == [1, 1, 1, 1]
    assert solve(4, [1, 2, 3, 4], [1, 2, 4, 7]) == [1, 2, 4, 7]
    assert solve(8, [84, 87, 78, 16, 94, 36, 87, 93], [50, 22, 63, 28, 91, 60, 64, 27]) == [50, 22, 63, 28, 44, 60, 64, 27]


if __name__ == "__main__":
    test()
    main()
