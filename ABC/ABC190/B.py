def solve(n, s, d, xy_list):
    for x, y in xy_list:
        if x < s and y > d:
            return 'Yes'
    return 'No'


def main():
    n, s, d = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, s, d, xy_list)
    print(res)


def test():
    assert solve(4, 9, 9, [(5, 5), (15, 5), (5, 15), (15, 15)]) == 'Yes'
    assert solve(3, 691, 273, [(691, 997), (593, 273), (691, 273)]) == 'No'
    assert solve(7, 100, 100, [(10, 11), (12, 67), (192, 79), (154, 197), (142, 158), (20, 25), (17, 108)]) == 'Yes'


if __name__ == "__main__":
    test()
    main()
