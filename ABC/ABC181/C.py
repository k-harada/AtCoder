def solve(n, xy_list):
    for i in range(n - 2):
        x_i, y_i = xy_list[i]
        for j in range(i + 1, n - 1):
            x_j, y_j = xy_list[j]
            for k in range(j + 1, n):
                x_k, y_k = xy_list[k]
                if (y_k - y_i) * (x_j - x_i) == (y_j - y_i) * (x_k - x_i) and x_j - x_i != 0 and x_k - x_i != 0:
                    # print(i, j, k)
                    return 'Yes'
                elif x_i == x_j == x_k:
                    return 'Yes'
    return 'No'


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    print(res)


def test():
    assert solve(4, [(0, 1), (0, 2), (0, 3), (1, 1)]) == 'Yes'
    # assert solve(100, [(i, i ** 2) for i in range(100)]) == 'No'


if __name__ == "__main__":
    test()
    main()
