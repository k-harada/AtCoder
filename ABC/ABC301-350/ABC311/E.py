def solve(h, w, n, ab_list):
    square = [[0] * w for _ in range(h)]
    for a, b in ab_list:
        square[a - 1][b - 1] = 1
    res_matrix = [[0] * w for _ in range(h)]
    res = 0

    for i in range(h):
        for j in range(w):
            if square[i][j] == 1:
                res_matrix[i][j] = 0
            elif i == 0 or j == 0:
                res_matrix[i][j] = 1
            else:
                res_matrix[i][j] = min([res_matrix[i - 1][j], res_matrix[i][j - 1], res_matrix[i - 1][j - 1]]) + 1
            res += res_matrix[i][j]
    return res


def main():
    h, w, n = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(h, w, n, ab_list)
    print(res)


def test():
    assert solve(2, 3, 1, [(2, 3)]) == 6
    assert solve(3, 2, 6, [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]) == 0
    assert solve(1, 1, 0, []) == 1
    assert solve(3000, 3000, 0, []) == 9004500500


if __name__ == "__main__":
    # test()
    main()
