def solve(n, m, a):
    mat = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            mat[i][j] = 1
    for j in range(m):
        for i in range(n - 1):
            p, q = a[j][i] - 1, a[j][i + 1] - 1
            p, q = min(p, q), max(p, q)
            # print(p, q)
            mat[p][q] = 0
    # print(mat)
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            res += mat[i][j]
    return res


def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, a)
    print(res)


def test():
    assert solve(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]]) == 2
    assert solve(3, 3, [[1, 2, 3], [3, 1, 2], [1, 2, 3]]) == 0


if __name__ == "__main__":
    test()
    main()
